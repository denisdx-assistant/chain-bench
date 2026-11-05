# Invalid runs

Kept for the record, excluded from every table.

- `chains_ru_batch_chunked*.json` — all tasks in one request; parsing, not the
  model, decided the score.
- `programs_yarn1m_32k_no_raw.json`, `programs_iq3s_32k_no_raw.json` — program
  runs scored by a parser that kept neither the raw answer nor the parsed array,
  so the score cannot be reproduced. Withdrawn on 2026-11-05 and queued for a
  re-run that stores the raw answer.
