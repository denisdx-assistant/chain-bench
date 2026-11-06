# Context-length prefill

Measured with `scripts/context_count.py`: one long prompt of filler words, a word-count
question, and the server's own timings. Prompt size is the actual token count reported by
the server, not the requested one. Prefill speed is the mean over the whole prompt, so it
rises with context length and should be compared at equal sizes.

| Model (provider) | Target | Prompt tokens | Prefill tok/s | Prefill time | Answer tokens | Gen tok/s | Wall | Count |
|---|---|---|---|---|---|---|---|---|
| Qwen3.8-Flash-Next-UD-Q4_K_XL-1m | 261k | 261238 | 1850.6 | 141 s | 8192 | 152.5 | 195 s | ✗ |
| Qwen3.8-Flash-Next-UD-Q4_K_XL-1m | 512k | 512236 | 1758.2 | 291 s | 8192 | 127.5 | 356 s | ✗ |
| Qwen3.8-Flash-Next-UD-Q4_K_XL-1m | 1M | 1000236 | 1583.0 | 632 s | 8192 | 74.2 | 744 s | ✗ |

**Generation speed here is indicative only.** The prompt asks for a long story after the
count, so generation differs from the short-answer work in the main benchmark; treat the
*prefill* column as the reliable measurement and use `docs/performance.md` for generation
speed on real tasks.
