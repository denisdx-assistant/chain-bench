# Performance

Median server-side numbers per run: generation speed, prefill speed, tokens spent on
an answer, prompt size (including the cached prefix) and generation time.
These come from the `timings` block of the API response, so queueing and wall-clock
noise are excluded. **Prefill counts only requests that did not hit the prefix cache**
(`cache_n = 0`); the column `uncached reqs` says how many samples that is. In a run over
one document that is usually one request, since the rest reuse the prefix. Runs made
before the fields were captured show “—”.

| Run | Variant | n | gen tok/s | prefill tok/s | uncached reqs | answer tokens | prompt tokens | gen time |
|---|---|---|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q6_K_XL · chains en · 16k | 8tasks | 8 | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · chains ru · 16k | default | 17 | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · chains ru · 16k | 8tasks | 8 | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · chains zh · 16k | 8tasks | 8 | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · programs · 8k · v2_flow_8 | default | 8 | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · programs · 8k · v2_hard_8 | default | 8 | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · programs · 16k · v4_16k | default | 20 | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains en · 16k | default | 17 | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains en · 16k | 8tasks | 8 | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains ru · 16k | default | 17 | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains ru · 16k | 8tasks | 8 | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains zh · 16k | default | 17 | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains zh · 16k | 8tasks | 8 | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · programs · 16k · v4_16k | default | 20 | 40.3 | 722.1 | 2 | 4145 | 142558 | 103 s |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · chains ru · 32k | guarded | 17 | — | — | 0 | — | — | — |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · chains ru · 65535 | default | 17 | — | — | 0 | — | — | — |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains en · 16k | default | 17 | 78.0 | 1135.9 | 17 | 4112 | 14062 | 54 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains en · 16k | 8tasks | 8 | 81.6 | 1117.0 | 8 | 920 | 13735 | 11 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains ru · 16k | default | 17 | 73.6 | 1166.7 | 4 | 4605 | 19260 | 64 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains ru · 16k | 8tasks | 8 | 74.0 | 1162.8 | 1 | 1922 | 19112 | 26 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains zh · 16k | default | 17 | 78.6 | 1534.9 | 2 | 4964 | 38359 | 66 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains zh · 16k | 8tasks | 8 | 78.6 | 1529.1 | 2 | 1923 | 38141 | 23 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · programs · 16k · v4_16k | default | 20 | 84.8 | 1800.2 | 20 | 7434 | 142558 | 87 s |
