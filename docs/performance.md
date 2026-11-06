# Performance

Server-side numbers per run: generation speed, prefill speed, tokens spent on an
answer, prompt size (including the cached prefix) and generation time.
These come from the `timings` block of the API response, so queueing and wall-clock
noise are excluded. Two speeds are given: **best** (the fastest task, i.e. a run
without stalls — the figure to quote) and **median** (typical, pulled down by any
stall). **Prefill counts only requests that did not hit the prefix cache**
(`cache_n = 0`); the column `uncached reqs` says how many samples that is. In a run
over one document that is usually one request, since the rest reuse the prefix. Runs
made before the fields were captured show —.

| Run | Variant | n | gen tok/s (best) | gen tok/s (median) | prefill tok/s (best) | uncached reqs | answer tokens | prompt tokens | gen time |
|---|---|---|---|---|---|---|---|---|---|
| Qwen3.8-27B-UD-Q4_K_M · chains ru · 16k | default | 17 | 23.1 | 22.8 | — | 0 | 15722 | 19259 | 692 s |
| Qwen3.8-27B-UD-Q6_K_XL · chains en · 16k | 8tasks | 8 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · chains ru · 16k | default | 17 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · chains ru · 16k | 8tasks | 8 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · chains zh · 16k | 8tasks | 8 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · programs · 16k · v4_16k | default | 20 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains en · 16k | default | 17 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains en · 16k | 8tasks | 8 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains ru · 16k | default | 17 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains ru · 16k | 8tasks | 8 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains zh · 16k | default | 17 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains zh · 16k | 8tasks | 8 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · programs · 16k · v4_16k | default | 20 | 44.1 | 40.3 | 722.9 | 2 | 4145 | 142558 | 103 s |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · chains en · 32k | guarded | 17 | 102.1 | 90.7 | 1510.7 | 16 | 4596 | 14062 | 57 s |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · chains en · 32k | guarded_8tasks | 8 | 107.3 | 94.1 | 1503.2 | 8 | 1059 | 13735 | 11 s |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · chains ru · 32k | guarded | 17 | — | — | — | 0 | — | — | — |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · chains ru · 32k | guarded_8tasks | 8 | 87.0 | 83.7 | 1655.2 | 1 | 2121 | 19112 | 26 s |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · chains zh · 32k | guarded | 17 | 97.4 | 88.9 | — | 0 | 5600 | 38359 | 65 s |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · chains zh · 32k | guarded_8tasks | 8 | 98.5 | 89.4 | 2084.9 | 1 | 1976 | 38141 | 21 s |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S+YaRN-1M · programs · 32k · v4_32k_guarded | guarded | 20 | 99.4 | 97.8 | 2456.1 | 20 | 6688 | 142558 | 70 s |
| Qwen3.8-Flash-Next-UD-IQ4_XS · chains en · 16k | default | 17 | 102.2 | 89.9 | 1495.4 | 17 | 5469 | 14062 | 57 s |
| Qwen3.8-Flash-Next-UD-IQ4_XS · chains en · 16k | 8tasks | 8 | 94.5 | 90.0 | 1471.5 | 8 | 1379 | 13735 | 15 s |
| Qwen3.8-Flash-Next-UD-IQ4_XS · chains ru · 16k | default | 17 | 94.4 | 83.5 | 1602.8 | 2 | 6739 | 19260 | 86 s |
| Qwen3.8-Flash-Next-UD-IQ4_XS · chains ru · 16k | 8tasks | 8 | 91.1 | 81.7 | 1592.7 | 1 | 1985 | 19112 | 25 s |
| Qwen3.8-Flash-Next-UD-IQ4_XS · chains zh · 16k | default | 17 | 93.3 | 87.1 | 2032.6 | 4 | 6016 | 38359 | 69 s |
| Qwen3.8-Flash-Next-UD-IQ4_XS · chains zh · 16k | 8tasks | 8 | 101.6 | 90.1 | 2032.2 | 2 | 1601 | 38141 | 18 s |
| Qwen3.8-Flash-Next-UD-IQ4_XS · programs · 16k · v4_16k | default | 20 | 98.2 | 95.7 | 2405.4 | 20 | 6905 | 142558 | 72 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains en · 16k | default | 17 | 88.9 | 78.0 | 1140.0 | 17 | 4112 | 14062 | 54 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains en · 16k | 8tasks | 8 | 87.6 | 81.6 | 1121.3 | 8 | 920 | 13735 | 11 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains ru · 16k | default | 17 | 82.2 | 73.6 | 1168.8 | 4 | 4605 | 19260 | 64 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains ru · 16k | 8tasks | 8 | 83.2 | 74.0 | 1162.8 | 1 | 1922 | 19112 | 26 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains zh · 16k | default | 17 | 92.6 | 78.6 | 1537.3 | 2 | 4964 | 38359 | 66 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains zh · 16k | 8tasks | 8 | 85.0 | 78.6 | 1530.4 | 2 | 1923 | 38141 | 23 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · programs · 16k · v4_16k | default | 20 | 101.5 | 84.8 | 1802.7 | 20 | 7434 | 142558 | 87 s |
