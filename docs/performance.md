# Performance

Median server-side numbers per run: generation speed, prefill speed, tokens spent on
an answer, prompt size (including the cached prefix) and generation time.
These come from the `timings` block of the API response, so queueing and wall-clock
noise are excluded. Runs made before the fields were captured show “—”.

| Run | Variant | n | gen tok/s | prefill tok/s | answer tokens | prompt tokens | gen time |
|---|---|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q6_K_XL · chains en · 16k | 8tasks | 8 | — | — | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · chains ru · 16k | default | 17 | — | — | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · chains ru · 16k | 8tasks | 8 | — | — | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · chains zh · 16k | 8tasks | 8 | — | — | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · programs · 8k · v2_flow_8 | default | 8 | — | — | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · programs · 8k · v2_hard_8 | default | 8 | — | — | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · programs · 16k · v4_16k | default | 20 | — | — | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains en · 16k | default | 17 | — | — | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains en · 16k | 8tasks | 8 | — | — | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains ru · 16k | default | 17 | — | — | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains ru · 16k | 8tasks | 8 | — | — | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains zh · 16k | default | 17 | — | — | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains zh · 16k | 8tasks | 8 | — | — | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · programs · 16k · v4_16k | default | 1 | 40.2 | cached | 4146 | 142737 | 103 s |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · chains ru · 32k | guarded | 17 | — | — | — | — | — |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · chains ru · 65535 | default | 17 | — | — | — | — | — |
