# LAB6 — Code and Branch Coverage Analysis

**Name:** Shriram Chandrasekar
**SRN:** PES2UG24CS495
**SEC:** H
**Application:** Car Insurance Premium Calculator (`car_insurance_premium.py`)

## Overview
Measure and improve test coverage of the assigned module using Python's `coverage`
tool, achieving at least 90% **code (line)** coverage and at least 90% **branch**
coverage by writing additional targeted test cases.

## Files
| File | Description |
|------|-------------|
| `car_insurance_premium.py` | Module under test |
| `CodeCoverageTest_PES2UG24CS495_car_insurance_premium.py` | Line-coverage test cases (13 tests) |
| `BranchCoverageTest_PES2UG24CS495_car_insurance_premium.py` | Branch-coverage test cases (16 tests) |
| `CodeCoverage_PES2UG24CS495.png` | Line-coverage report screenshot |
| `BranchCoverage_PES2UG24CS495.png` | Branch-coverage report screenshot |
| `PES2UG24CS495_SE_LAB6.pdf` | Full lab report |

## Commands
```bash
pip install coverage pytest

# Code (line) coverage
coverage run -m pytest CodeCoverageTest_PES2UG24CS495_car_insurance_premium.py
coverage report -m

# Branch coverage
coverage run --branch -m pytest BranchCoverageTest_PES2UG24CS495_car_insurance_premium.py
coverage report -m
```

## Results
| Metric | Tests | Coverage |
|--------|-------|----------|
| Code (line) coverage | 13 | 100% |
| Branch coverage | 16 | 100% (30/30 branches) |

Both exceed the 90% requirement.
