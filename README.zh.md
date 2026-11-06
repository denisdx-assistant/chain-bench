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

**结论。** 在链条上各模型**没有**拉开差距：Q6 10/17，Flash-Next 在大预算下 12/17、
32k 下 10/17，Q8 俄语 10/17、英语 11/17——在 17 题集合上相差一到两题，完全落在
区间内。YaRN 1M 与 262k 基础版相差一段程序，同样在噪声范围内。退化循环罕见，
由流式检测器而不是更大的预算控制。

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
结果文件生成。

<!-- summary:start -->
| Run | Overall (errors) | Test 1 en (correct) | Test 1 ru (correct) | Test 1 zh (correct) | Test 2 (correct) |
|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q6_K_XL · ctx 262k · no YaRN · T default · budget 16k | 150m36s · 43% err | 5m19s 4/8 (8) | 13m30s 10/17 | 10m08s 5/8 (8) | 121m39s 11/20 |
| Qwen3.8-27B-UD-Q6_K_XL · ctx 262k · no YaRN · T default · budget 8 · legacy 8-program set | 11m25s · 12% err | — | — | — | 11m25s 7/8 |
| Qwen3.8-27B-UD-Q8_K_XL · ctx 262k · no YaRN · T default · budget 16k · guard | 48m18s · 37% err | 14m42s 11/17 | 15m40s 10/17 | 17m56s 11/17 | — |
| Qwen3.8-27B-UD-Q8_K_XL · ctx 262k · no YaRN · T default · budget 32k · guard | 35m23s · 30% err | — | — | — | 35m23s 14/20 |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · ctx 1M · YaRN · T 0.3 · pen 0.3 · budget 32k · guard | 30m21s · 41% err | — | 30m21s 10/17 | — | — |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · ctx 1M · YaRN · T default · budget 65535 · provenance inferred | 27m58s · 29% err | — | 27m58s 12/17 | — | — |
| Qwen3.8-Flash-Next-UD-IQ4_XS · ctx 1M · YaRN · T default · pen 0.2 · budget 32k · guard | 25m08s · 35% err | — | 25m08s 11/17 | — | — |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · ctx 1M · YaRN · T default · pen 0.2 · budget 32k · guard | 124m23s · 27% err | 29m20s 13/17 | 26m59s 11/17 | 30m15s 14/17 | 37m49s 14/20 |
<!-- summary:end -->

**细节。**

- 逐题矩阵，含每题耗时与结果: [docs/results-by-task.md](docs/results-by-task.md)
- 逐次运行表格，含推理规模与长度截断: [results/README.md](results/README.md)
- 每次运行的性能（来自服务器计时）：生成与预填充速度、单题 token 消耗:
  [docs/performance.md](docs/performance.md)
- 长上下文预填充（261k / 512k / 1M token）:
  [docs/context-prefill.md](docs/context-prefill.md)
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

## 许可
## 许可

代码 — MIT。文本与数据集 — CC BY 4.0。
