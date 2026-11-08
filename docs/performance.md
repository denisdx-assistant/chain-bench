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
| Qwen3.8-27B-UD-Q4_K_M · chains en · 16k | default | 17 | 24.0 | 20.7 | — | 0 | 8515 | 14062 | 419 s |
| Qwen3.8-27B-UD-Q4_K_M · chains en · 16k | 8tasks | 8 | 52.3 | 49.8 | — | 0 | 1103 | 13735 | 22 s |
| Qwen3.8-27B-UD-Q4_K_M · chains ru · 16k | default | 17 | 23.1 | 22.8 | — | 0 | 15722 | 19259 | 692 s |
| Qwen3.8-27B-UD-Q4_K_M · chains ru · 16k | 8tasks | 8 | 50.3 | 47.9 | 921.7 | 1 | 2469 | 19112 | 52 s |
| Qwen3.8-27B-UD-Q4_K_M · chains zh · 16k | default | 17 | 23.4 | 22.3 | 862.4 | 1 | 4391 | 38359 | 222 s |
| Qwen3.8-27B-UD-Q4_K_M · chains zh · 16k | 8tasks | 8 | 45.4 | 40.9 | — | 0 | 2854 | 38141 | 68 s |
| Qwen3.8-27B-UD-Q4_K_M · programs · 16k · v4_16k | default | 20 | 26.5 | 25.9 | 434.0 | 6 | 4145 | 142558 | 161 s |
| Qwen3.8-27B-UD-Q6_K_XL · chains en · 16k | default | 17 | 69.0 | 62.4 | 1556.5 | 1 | 4099 | 14062 | 64 s |
| Qwen3.8-27B-UD-Q6_K_XL · chains en · 16k | 8tasks | 8 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · chains ru · 16k | default | 17 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · chains ru · 16k | 8tasks | 8 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · chains zh · 16k | default | 17 | 63.9 | 54.3 | 1341.9 | 1 | 4099 | 38359 | 75 s |
| Qwen3.8-27B-UD-Q6_K_XL · chains zh · 16k | 8tasks | 8 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q6_K_XL · programs · 16k · v4_16k | default | 20 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains en · 16k | default | 17 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains en · 16k | 8tasks | 8 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains en · 32k | rerun | 17 | 64.0 | 57.8 | — | 0 | 4099 | 14062 | 70 s |
| Qwen3.8-27B-UD-Q8_K_XL · chains en · 32k | rerun_8tasks | 8 | 63.1 | 59.2 | — | 0 | 1436 | 13735 | 24 s |
| Qwen3.8-27B-UD-Q8_K_XL · chains ru · 16k | default | 17 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains ru · 16k | 8tasks | 8 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains ru · 32k | rerun | 17 | 62.0 | 58.1 | 1327.0 | 1 | 4099 | 19260 | 66 s |
| Qwen3.8-27B-UD-Q8_K_XL · chains ru · 32k | rerun_8tasks | 8 | 67.7 | 59.2 | — | 0 | 1865 | 19112 | 32 s |
| Qwen3.8-27B-UD-Q8_K_XL · chains zh · 16k | default | 17 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains zh · 16k | 8tasks | 8 | — | — | — | 0 | — | — | — |
| Qwen3.8-27B-UD-Q8_K_XL · chains zh · 32k | rerun | 17 | 55.9 | 52.4 | — | 0 | 4099 | 38359 | 77 s |
| Qwen3.8-27B-UD-Q8_K_XL · chains zh · 32k | rerun_8tasks | 8 | 56.2 | 53.4 | — | 0 | 1718 | 38141 | 32 s |
| Qwen3.8-27B-UD-Q8_K_XL · programs · 16k · v4_16k | default | 20 | 44.1 | 40.3 | 722.9 | 2 | 4145 | 142558 | 103 s |
| Qwen3.8-27B-UD-Q8_K_XL · programs · 32k · v4_32k_rerun | default | 20 | 41.5 | 40.2 | 723.8 | 7 | 4145 | 142558 | 103 s |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · chains en · 32k | guarded | 17 | 102.1 | 90.7 | 1510.7 | 16 | 4596 | 14062 | 57 s |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · chains en · 32k | guarded_8tasks | 8 | 107.3 | 94.1 | 1503.2 | 8 | 1059 | 13735 | 11 s |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · chains ru · 32k | guarded | 17 | — | — | — | 0 | — | — | — |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · chains ru · 32k | guarded_8tasks | 8 | 87.0 | 83.7 | 1655.2 | 1 | 2121 | 19112 | 26 s |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · chains zh · 32k | guarded | 17 | 97.4 | 88.9 | — | 0 | 5600 | 38359 | 65 s |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · chains zh · 32k | guarded_8tasks | 8 | 98.5 | 89.4 | 2084.9 | 1 | 1976 | 38141 | 21 s |
| Qwen3.8-Flash-Next-GSQ-RCO-IQ3_S · programs · 32k · v4_32k_guarded | guarded | 20 | 99.4 | 97.8 | 2456.1 | 20 | 6688 | 142558 | 70 s |
| Qwen3.8-Flash-Next-UD-IQ4_XS · chains en · 16k | default | 17 | 102.2 | 89.9 | 1495.4 | 17 | 5469 | 14062 | 57 s |
| Qwen3.8-Flash-Next-UD-IQ4_XS · chains en · 16k | 8tasks | 8 | 94.5 | 90.0 | 1471.5 | 8 | 1379 | 13735 | 15 s |
| Qwen3.8-Flash-Next-UD-IQ4_XS · chains ru · 16k | default | 17 | 94.4 | 83.5 | 1602.8 | 2 | 6739 | 19260 | 86 s |
| Qwen3.8-Flash-Next-UD-IQ4_XS · chains ru · 16k | 8tasks | 8 | 91.1 | 81.7 | 1592.7 | 1 | 1985 | 19112 | 25 s |
| Qwen3.8-Flash-Next-UD-IQ4_XS · chains zh · 16k | default | 17 | 93.3 | 87.1 | 2032.6 | 4 | 6016 | 38359 | 69 s |
| Qwen3.8-Flash-Next-UD-IQ4_XS · chains zh · 16k | 8tasks | 8 | 101.6 | 90.1 | 2032.2 | 2 | 1601 | 38141 | 18 s |
| Qwen3.8-Flash-Next-UD-IQ4_XS · programs · 16k · v4_16k | default | 20 | 98.2 | 95.7 | 2405.4 | 20 | 6905 | 142558 | 72 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains en · 16k | default | 17 | 88.9 | 78.0 | 1140.0 | 17 | 4112 | 14062 | 54 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains en · 16k | 8tasks | 8 | 87.6 | 81.6 | 1121.3 | 8 | 920 | 13735 | 11 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains en · 32k | rerun | 17 | 90.5 | 79.5 | 1136.6 | 16 | 5425 | 14062 | 74 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains en · 32k | rerun_8tasks | 8 | 84.7 | 81.5 | 1119.7 | 8 | 1228 | 13735 | 15 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains ru · 16k | default | 17 | 82.2 | 73.6 | 1168.8 | 4 | 4605 | 19260 | 64 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains ru · 16k | 8tasks | 8 | 83.2 | 74.0 | 1162.8 | 1 | 1922 | 19112 | 26 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains ru · 32k | rerun | 17 | 84.1 | 75.2 | 1153.4 | 1 | 5892 | 19260 | 80 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains ru · 32k | rerun_8tasks | 8 | 79.5 | 75.3 | 1150.5 | 1 | 2063 | 19112 | 27 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains zh · 16k | default | 17 | 92.6 | 78.6 | 1537.3 | 2 | 4964 | 38359 | 66 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains zh · 16k | 8tasks | 8 | 85.0 | 78.6 | 1530.4 | 2 | 1923 | 38141 | 23 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains zh · 32k | rerun | 17 | 85.3 | 77.9 | 1524.1 | 1 | 6501 | 38359 | 82 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · chains zh · 32k | rerun_8tasks | 8 | 87.0 | 81.3 | 1528.9 | 1 | 1061 | 38141 | 13 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · programs · 16k · v4_16k | default | 20 | 88.8 | 84.2 | 1802.7 | 19 | 6961 | 142558 | 81 s |
| Qwen3.8-Flash-Next-UD-Q4_K_XL · programs · 32k · v4_32k_rerun | default | 20 | 105.2 | 83.2 | 1800.8 | 19 | 6795 | 142558 | 83 s |
| Ripple-65B-Preview-Q6_K · chains en · 16k | default | 17 | 20.6 | 20.5 | 482.4 | 1 | 4684 | 12913 | 230 s |
| Ripple-65B-Preview-Q6_K · programs · 16k · v4_16k | default | 7 | 13.7 | 13.7 | 371.9 | 3 | 12358 | 162746 | 902 s |
| deepseek-v4.1-flash · chains en · 16k | default | 17 | — | — | — | 0 | — | — | — |
| deepseek-v4.1-flash · programs · 16k · v4_16k | default | 20 | — | — | — | 0 | — | — | — |
| gemma-4-31B-it-UD-Q8_K_XL · chains en · 16k | default | 17 | 80.0 | 70.6 | — | 0 | 1473 | 13909 | 19 s |
| gemma-4-31B-it-UD-Q8_K_XL · chains en · 16k | 8tasks | 8 | 80.1 | 77.1 | — | 0 | 477 | 13575 | 6 s |
| gemma-4-31B-it-UD-Q8_K_XL · chains ru · 16k | default | 17 | 77.6 | 69.6 | 1041.1 | 1 | 986 | 19050 | 15 s |
| gemma-4-31B-it-UD-Q8_K_XL · chains ru · 16k | 8tasks | 8 | 77.4 | 72.3 | — | 0 | 685 | 18780 | 9 s |
| gemma-4-31B-it-UD-Q8_K_XL · chains zh · 16k | default | 17 | 64.4 | 58.5 | — | 0 | 1005 | 42057 | 17 s |
| gemma-4-31B-it-UD-Q8_K_XL · chains zh · 16k | 8tasks | 8 | 67.7 | 62.1 | — | 0 | 712 | 41936 | 12 s |
| gemma-4-31B-it-UD-Q8_K_XL · programs · 16k · v4_16k | default | 20 | 44.2 | 42.8 | 494.1 | 10 | 6509 | 142704 | 151 s |
