# Serving hardware and KV-cache settings

Speed in this benchmark depends not only on the weights but on how the serving
stack stores the KV cache. The table records what each measured configuration
actually used, so that a difference in tokens per second can be attributed.

## Qwen3.8-27B-UD-Q4_K_M.gguf

| Host | Context | Parallel | Batch / ubatch | KV K | KV V | Note |
|---|---|---|---|---|---|---|
| 192.168.1.111 (2×V100 32 GB) | 262 144 | 1 | 4096 / 4096 | `q8_0` | `turbo3` | full-size context host |
| 192.168.1.110 (RTX 3090 24 GB) | 200 000 | 1 | default | default (f16) | `turbo3` | same model, smaller context, otherwise interchangeable |

The two hosts run the same weights on purpose, so results stay comparable up to
the context limit; only the context size and the K-cache type differ.

## Qwen3.8-27B-UD-Q8_K_XL.gguf

| Host | Context | Parallel | Batch / ubatch | KV K | KV V | Draft K | Draft V |
|---|---|---|---|---|---|---|---|
| 192.168.1.111 (2×V100 32 GB) | 262 144 | 1 | 8192 / 2048 | `q8_0` | `q8_0` | `q8_0` | `turbo4` |

Q8 compresses **both** keys and values with `q8_0`, while the Flash-Next models
run `k8v4` (q8 keys, turbo4 values). This is one candidate explanation for speed
differences that the weights alone do not explain: the KV format changes memory
traffic and dequantisation cost per token. Note also that Q8 runs on the
llama.cpp-style stack while Flash-Next runs on strata, so engine differences are
mixed in with the format difference.

## Flash-Next models (IQ3_S, IQ4_XS, Q4_K_XL)

All three are served by the same engine configuration on 2×V100; only the packed
weights differ. Launch parameters, taken from the sanitised configs in
`configs/strata/`:

| Parameter | Value | Meaning |
|---|---|---|
| `--max-context` | 1 048 576 | 1M tokens |
| `--kv` | `k8v4` | keys q8, values turbo4 |
| `--kv-resident` | 49 152 | tokens kept resident in VRAM |
| `--rope-scaling` / `--rope-scale` / `--yarn-orig-ctx` | yarn / 4 / 262 144 | 262k native context scaled 4× to 1M |
| `--vram-reserve-mib` | 2 048 | headroom left to the driver |
| `--spec` / `--mtp-hnorm` | 4 / stream | speculative decoding with MTP |
| `--pipeline-windows` | 2 | pipeline depth |
| `--prompt-cache` | 4 | prompt cache slots |
| `--conversation-cache-mib` / `-slots` | 16 384 / 8 | cross-request KV reuse |

Because the serving configuration is identical, differences between IQ3_S,
IQ4_XS and Q4_K_XL in this benchmark come from the weights, not from the stack.
The KV format (`k8v4`) is the same in all three.

## Where this is stored

Per-run configuration lives in `results/run-configs.json` (`ctx`, `yarn`,
`temp`, `penalty`, `budget`, `guard`, and now `kv_k` / `kv_v` where known).
