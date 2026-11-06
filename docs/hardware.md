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
use `turbo3` for values (and default or `q8_0` keys). This is one candidate
explanation for speed differences that the weights alone do not explain: the
KV format changes memory traffic and dequantisation cost per token.

## Flash-Next models (IQ3_S, IQ4_XS, Q4_K_XL)

Served with YaRN scaling to a 1M context on 2×V100. KV-cache settings for these
runs were not recorded at the time and are marked as unknown in the config
registry; they should be captured before the next series.

## Where this is stored

Per-run configuration lives in `results/run-configs.json` (`ctx`, `yarn`,
`temp`, `penalty`, `budget`, `guard`, and now `kv_k` / `kv_v` where known).
