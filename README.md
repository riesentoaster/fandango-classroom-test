# This is a README

## Installation
1. `python3 -m venv .venv && source .venv/bin/activate`
2. `pip install -r requirements.txt`

## Tasks

Write a Fandango spec file in nested.fan that will
- parse
  - `123`
  - `23` if only the symbol `<a>` is parsed
  - `3` if only the symbol `<b>` is parsed
- produce
  - only `123`