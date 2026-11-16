# LAB7 — Fuzzing for Input Validation Bugs

**Name:** Shriram Chandrasekar
**SRN:** PES2UG24CS495
**SEC:** H
**Repository:** L6_L7_55_car_insurance_premium
**Module:** `car_insurance_premium_parser.py`

## Overview
Property-based fuzz testing with Hypothesis on three input parsers (registration number,
semicolon-separated claim amounts, DD/MM/YYYY date of birth). The fuzz tests exposed six
crashes on the original module; the fixed module handles any input without crashing.

## Files
| File | Description |
|------|-------------|
| `car_insurance_premium_parser.py` | Fixed module |
| `test_car_insurance_premium_parser.py` | Completed Hypothesis tests (one per function) |
| `PES2UG24CS495_SHRIRAM_CHANDRASEKAR_LAB7.pdf` | Report with SS1-SS4 and reflection answers |
| `screenshots/` | C0 setup, C1-C3 code, SS1 buggy run, SS2 failing tests (5 parts), SS3 fixed run, SS4 passing tests |

## Commands
```bash
pip install hypothesis pytest
python car_insurance_premium_parser.py
python -m pytest test_car_insurance_premium_parser.py
```

## Bugs found and fixed
| Function | Failing input | Crash | Fix |
|----------|---------------|-------|-----|
| `normalize_registration` | `None` | AttributeError | non-string returns `""`; all whitespace removed |
| `total_claim_amount` | `''`, `"1;;2"` | ValueError | blank/non-numeric/negative parts skipped |
| `total_claim_amount` | `None` | AttributeError | non-string returns `0` |
| `driver_age` | `''` | IndexError | must have exactly 3 parts, else `None` |
| `driver_age` | `'//'` | ValueError | numeric parts, valid day/month, year 1900-2026, else `None` |
| `driver_age` | `None` | AttributeError | non-string returns `None` |

## Results
Buggy module: 3 failed. Fixed module: 3 passed.
