# Серии прогонов

| Файл | Модель (resolved_provider) | Контекст | Бюджет | Результат |
|---|---|---|---|---|
| `programs_q6_v4` -> `programs_v4_20.json` | Qwen3.8-27b-Q6_K_XL | 150k | 16k | 11/20 (45% ошибок) |
| `programs_next_guarded.json` | llama_local_flash_next-1m (YaRN до 1M) | 1M | 32k | 3/20 (85% ошибок) |
| `programs_flash262_guarded.json` | llama_local_flash_next (262k, без YaRN) | 262k | 32k | 2/20 (90% ошибок) |

Правило: новая серия — новый файл; завершённые файлы не перезаписываются.
