import pytest
from car_insurance_premium import annual_premium, no_claim_bonus, claim_payout

# Lab 6 - Code (Line) Coverage test cases
# SRN: PES2UG24CS495  Name: SHRIRAM CHANDRASEKAR
# Goal: execute every line of car_insurance_premium.py at least once.


# ---------- annual_premium ----------
def test_sedan_no_claims():
    # base example: sedan, age 30, 0 claims, no anti-theft
    assert annual_premium("sedan", 30, 0, False) == 9600


def test_unknown_car_type_raises():
    # hits the "unknown car type" line
    with pytest.raises(ValueError):
        annual_premium("truck", 30, 0, False)


def test_driver_too_young_raises():
    # hits the "driver too young" line
    with pytest.raises(ValueError):
        annual_premium("sedan", 17, 0, False)


def test_young_driver_surcharge_with_anti_theft():
    # age < 25 surcharge (+4000), claims not 0 / not >2, anti-theft (-500)
    # hatchback 8000 + 4000 = 12000 - 500 = 11500
    assert annual_premium("hatchback", 20, 1, True) == 11500


def test_senior_driver_many_claims():
    # age >= 60 surcharge (+2000), claims > 2 doubles the premium
    # suv 15000 + 2000 = 17000 * 2 = 34000
    assert annual_premium("suv", 65, 3, False) == 34000


# ---------- no_claim_bonus ----------
def test_no_bonus():
    assert no_claim_bonus(0) == 0


def test_bonus_negative_raises():
    with pytest.raises(ValueError):
        no_claim_bonus(-1)


def test_bonus_tiers():
    assert no_claim_bonus(5) == 50   # >= 5
    assert no_claim_bonus(3) == 35   # >= 3
    assert no_claim_bonus(1) == 20   # >= 1


# ---------- claim_payout ----------
def test_payout_invalid_amount_raises():
    with pytest.raises(ValueError):
        claim_payout(-100, 50000, 1000, False)


def test_payout_total_loss():
    assert claim_payout(10000, 50000, 1000, True) == 50000


def test_payout_within_deductible():
    assert claim_payout(500, 50000, 1000, False) == 0


def test_payout_capped_at_insured_value():
    # damage - deductible exceeds insured value -> capped
    assert claim_payout(80000, 50000, 1000, False) == 50000


def test_payout_normal():
    # damage - deductible, below insured value
    assert claim_payout(20000, 50000, 1000, False) == 19000
