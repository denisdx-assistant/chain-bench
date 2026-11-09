# chain-bench

**面向本地语言模型的自包含基准：噪声中的多跳链条与程序执行。**

语言: [English](README.md) · [Русский](README.ru.md) · **中文**

---

## 摘要

**为什么做这件事。** 两个目标：

1. 开发并验证一套廉价、可复现的本地模型比较方法，并带自动难度调节——整套测试
   被调到让参考模型大约错一半，因为只有在这个位置测试才仍有区分力。
2. 为 **2× V100 32 GB + 128 GB RAM** 的配置选出最好的模型，这里的取舍在于量化、
   上下文模式与速度之间。

**做了什么。** 构建并冻结了两项测试：2 万 token 噪声文档中的 17 道多跳算术链条
（三种语言），以及 20 段 Python 程序的脑内执行，其注释中含有永不执行的代码。
参考答案由程序计算。在 `Qwen3.8-27B-UD-Q6_K_XL` 上把难度校准到链条 41%、程序 45%
的错误率，接近 50% 的目标。随后对三种 Flash-Next 配置和
`Qwen3.8-27B-UD-Q8_K_XL` 分别运行了系列测试。

**结果说明。** 这些测试噪声很大。每种语言 17 道链条、20 段程序，一两题的差异没有意义：
同一模型的重复运行在集合层面相差不超过一题，而单题翻转大约每十题出现一次。这里给出
置信区间是不诚实的——测试彼此异质，相同配置的重复太少——所以请把表格当作排序，而不是
测量值。

在这个限度内，有四点值得说明：

- **4 比特量化没有带来可测量的损失。** 在同一台机器上，Q4_K_M、Q6_K_XL 与 Q8_K_XL 分别
  得到 51 题中的 35、34、32 道正确链条，以及 20 段程序中的 15、13、15 段。Q4_K_M 甚至
  领先，但它在当前设置下**只完整跑过一次**：复跑已排队，领先也可能是小样本的偶然。
- **1 比特 coder 版本恰好在编码所在之处崩溃。** IQ1_M 在短链条上保持 34/51，但 20 段
  程序只完成 8 段——12 段撞上预算上限，而完成的每一段都答错。它听得懂俄语却用英语回答，
  所以它的俄语链条测的是推理，不是语言。
- **Flash-Next 与稠密 27B 质量相当，速度却成倍领先，长上下文时尤其明显。** IQ4_XS：
  链条 35/51、程序 16.5/20，与 Q4_K_M 的 35 和 15 相同，但生成 85–96 t/s 对 23–26，
  250k 预填 2427 t/s 对 431，250k 生成 84 t/s 对约 10。
- **程序能区分模型，链条不能。** 六款模型在链条上挤在 51 题中的 32–35，而程序从 0 到
  20 题中的 18。程序意味着长提示加真实代码，最接近实际工作，这一列最值得相信。

完整论证、噪声估计与注意事项见 [docs/conclusions.md](docs/conclusions.md)。

## 1. 方法学

**测试 1 —— 噪声中的链条。** 约 2 万 token 的语义中性噪声文档（300 行，约 7.2 万
字符）包含陈述链条与 17 道问题。答案为单个整数。每种语言使用同一生成器与同一种子，
因此噪声彼此平行，只有语言不同。

**测试 2 —— 冻结程序。** 20 段 Python 程序（种子 300–319）构建 10 元素数组：交换、
分支、循环、递归、正则、类型转换与别名。注释和字符串中含诱饵代码。模型返回最终
数组与总和，两者都必须完全匹配。

**校准。** 优先用结构复杂度提升难度，其次才是噪声体量；故意不把很小的 token 预算
当作难度杠杆。参考模型被调到约 50% 错误。逐步骤表格见
[docs/calibration.md](docs/calibration.md)。

**控制项。** 每次请求一题；按模型级别固定预算；流式循环检测；长度截断以四倍预算
重跑；每次运行记录来源。规则见 [docs/methodology.md](docs/methodology.md)。

**产物。**

- 数据集与 SHA-256: [datasets/MANIFEST.json](datasets/MANIFEST.json)
- 生成器: [scripts/gen_noise.py](scripts/gen_noise.py),
  [scripts/gen_program_v3.py](scripts/gen_program_v3.py),
  [scripts/build_i18n_all.py](scripts/build_i18n_all.py)
- 运行器: [scripts/run_chains_guarded.py](scripts/run_chains_guarded.py),
  [scripts/run_frozen_guarded.py](scripts/run_frozen_guarded.py)
- 循环检测: [scripts/guard.py](scripts/guard.py)

## 2. 测试系列

**数据集。** 测试 1：俄语、英语、中文各一份 17 题的完整文档，另保留 8 题翻译子集以
延续早期运行。测试 2：一套 20 段程序的冻结集合，不做语言划分。所有集合均已冻结；
新变体以新文件加入。

**系列如何执行。** 每个模型都通过同一个本地端点提供，因此运行严格串行。一次运行
为每次请求一题，预算与采样记录在 [results/run-configs.json](results/run-configs.json)。
当模型以不同上下文、YaRN、温度或预算提供服务时，它在下表中会占多行——除非名称
另有说明（`+ YaRN 1M`），上下文一律为 262k。

**难度调整的实际做法。** 链条通过增加规则组合类题目来调整，噪声保持在 2 万 token：
扫描显示 4 万与 6 万并不改变准确率。程序通过四代增加操作数、嵌套与诱饵来调整，
直到参考模型降到大约一半错误。

### 汇总

每个单元格是一次测试系列：总耗时与得分。`(8)` 表示 8 题子集而非完整集合。表格由
结果文件生成。若同一配置运行多次，单元格显示各次有效运行的平均值，因此可能出现
小数（`11.5/17`）：首次运行与复现运行都计入。

<!-- summary:start -->
| 运行 | 总计（错误） | 每题中位 token 数 | 测试 1 en（正确） | 测试 1 ru（正确） | 测试 1 zh（正确） | 测试 1 子集 8（全部语言） | 测试 2（正确） |
|---|---|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q4_K_M | 442m14s · 30% 错误率 | 4144 | 108m21s 12/17 | 93m16s 11/17 | 91m48s 12/17 | 22m14s 12/24 | 148m49s 15/20 |
| ⚠ Qwen3.8-27B-UD-Q4_K_M · 未完成 1 | 57m03s · 34% 错误率 | 4099 | 17m20s 11/16 | 18m24s 10/17 | 21m19s 12/17 | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · t 0.3 · pen 0.2 | 154m57s · 38% 错误率 | 4100 | 14m14s 12/17 | 21m10s 10/17 | 19m10s 9/17 | 28m39s 14/24 | 100m23s 13/20 |
| Qwen3.8-27B-UD-Q6_K_XL | 169m28s · 35% 错误率 | 4099 | 15m37s 12/17 | 17m22s 10.5/17 | 21m12s 12/17 | 22m21s 13/24 | 115m16s 12/20 |
| Qwen3.8-27B-UD-Q8_K_XL | 146m44s · 33% 错误率 | 4100 | 14m14s 11/17 | 14m45s 10/17 | 17m43s 11.5/17 | 15m10s 13/24 | 100m03s 15/20 |
| ⚠ Qwen3.8-Flash-Next-Abiray-Coder-IQ1_M · 未完成 14 | 340m56s · 40% 错误率 | 8743 | 43m39s 12/17 | 56m48s 11/15 | 21m49s 11/17 | 22m50s 15/24 | 218m40s 0/8 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · t 0.3 · pen 0.3 | 140m18s · 36% 错误率 | 5448 | 28m40s 12/17 | 26m18s 11/17 | 29m57s 11/17 | 17m31s 15/24 | 55m22s 11.5/20 |
| Qwen3.8-Flash-Next-UD-IQ4_XS · pen 0.2 | 138m21s · 27% 错误率 | 5511 | 31m20s 11.5/17 | 27m22s 11/17 | 24m52s 12.5/17 | 18m21s 15.5/24 | 54m47s 16.5/20 |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · pen 0.2 | 154m10s · 27% 错误率 | 5616 | 34m18s 12.5/17 | 28m21s 11/17 | 33m41s 13.5/17 | 24m28s 15.5/24 | 57m50s 15/20 |
| ⚠ Ripple-65B-Preview-Q6_K · 未完成 6 | 120m57s · 25% 错误率 | 4684 | 120m57s 12/16 | — | — | — | 121m49s 0/7 / 20 |
| ⚠ deepseek-v4.1-flash | 16m48s · 30% 错误率 | — | 7m04s 12/17 | — | — | — | 9m44s 14/20 |
| gemma-4-31B-it-UD-Q8_K_XL | 168m44s · 58% 错误率 | 1601 | 11m40s 9/17 | 7m24s 10/17 | 8m22s 11/17 | 11m17s 14/24 | 141m18s 0/20 |

⚠ — 该行并非所有题目都已计算（缺少部分集合、文件不完整或存在未完成题目）：其质量百分比无法与其他行比较。
<!-- summary:end -->

**细节。**

- 逐题矩阵，含每题耗时与结果: [docs/results-by-task.md](docs/results-by-task.md)
- 逐次运行表格，含推理规模与长度截断: [results/README.md](results/README.md)
- 每次运行的性能（来自服务器计时）：生成与预填充速度、单题 token 消耗:
  [docs/performance.md](docs/performance.md)
- 长上下文预填充（261k / 512k / 1M token）:
  [docs/context-prefill.md](docs/context-prefill.md)
- 各主机的硬件与 KV 缓存设置:
  [docs/hardware.md](docs/hardware.md)
- 运行与校准的时间顺序日志: [docs/run-log.md](docs/run-log.md)

## 3. 模型

名称与运行配置完全一致；表格中不使用简写。

| 模型 | 状态 |
|---|---|
| `Qwen3.8-27B-UD-Q6_K_XL` | 已测量 |
| `Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S + YaRN 1m` | 已测量 |
| `Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S` | 已测量 |
| `Qwen3.8-27B-UD-Q8_K_XL` | 进行中 |
| `Qwen3.8-Flash-Next-UD-Q4_K_XL` | 队列中：YaRN 1M，32k 带检测器 |
| `Qwen3.8-Flash-Next-UD-IQ4_XS` | 队列中：YaRN 1M，32k 带检测器 |
| `Qwen3.8-Flash-Next-IQ3_M` | 计划中 |

## 4. 复现一次运行

```bash
python3 scripts/run_chains_guarded.py \
    --dataset datasets/chains/ru/dataset_20k_17tasks.json \
    --model local-only --max-tokens 16000 --timeout 2400 --temp -1 \
    --out results/<model>/chains_ru_20k_16k.json

python3 scripts/run_frozen_guarded.py --dir datasets/programs/v4 \
    --model local-only --max-tokens 16000 --timeout 2400 --temp -1 \
    --out results/<model>/programs_v4_16k.json
```

`--temp -1` 表示默认采样：字段被省略，而不是设成某个值。生成器按种子确定。

## 5. 局限

- 样本量小：17 道链条题与 20 段程序。价值在错误画像与相对次序，而非精确比例。
- 单一硬件配置与单一本地端点；耗时中位数含排队时间。
- 8 题三语子集是历史交叉校验，而不是第一代的完整翻译。
- 三个计划中的量化尚无运行。

## 6. 仓库结构

```
README.md            英文，主版本
README.ru.md         俄语翻译
README.zh.md         中文翻译
docs/                方法学、校准、逐题结果、运行日志（英文）
datasets/            冻结数据 + 带 SHA-256 的 MANIFEST.json
results/             每个模型一个目录，目录名即精确模型名
  <model>/series.json    机器可读的运行索引
  <model>/*.json         每次运行一个文件
results/run-configs.json  每次运行的服务配置
results/_invalid/    批量实验留档，不计入表格
scripts/             生成器、运行器、循环检测、表格构建
```

**关于程序得分。** 早期的受保护运行器用 `array`/`sum` 键比较，而数据集里是
`expected_array`/`expected_sum`，因此那些运行中的每段程序都被判为错误。受影响的
运行（Flash-Next 各变体）已从表格中撤回，并正以修正后的比较重新运行；Q6 的程序
得分可由其保存的回答复现。

## 7. 备注

**挑衅性题目。** 第 11 题（ship-15 与 ship-18）和第 12 题（heron-09）问的是文档中并不存在的实体，
两者都靠规则而非记录得出。它们被有意保留在题集中——见
[docs/methodology.md](docs/methodology.md#provocative-tasks-frozen-in-the-dataset)。
第 12 题因预算被截断并不表示出现循环，英语或中文得分低也不表示测试环境坏了。

### 速度

汇总表中容易混淆两件事：「每任务 token 数」表示模型写了多少，而不是写得多快。按提示长度
分组的预填充与生成速度（仅取自服务器计时）见 [docs/speed.md](docs/speed.md)。

## 公开数据

仓库是公开的：包含冻结的数据集、测试框架与全部结果。脚本中的端点地址只是本地模型服务器的
占位符；仓库中不含任何凭据、密钥或私有语料。

## 许可

代码 MIT；文本与数据集 CC BY 4.0。
