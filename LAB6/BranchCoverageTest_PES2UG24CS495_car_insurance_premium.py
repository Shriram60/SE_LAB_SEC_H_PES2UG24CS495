import pytest
from car_insurance_premium import annual_premium, no_claim_bonus, claim_payout

# Lab 6 - Branch Coverage test cases
# SRN: PES2UG24CS495  Name: SHRIRAM CHANDRASEKAR
# Goal: make every decision (if / elif) evaluate to BOTH True and False.


# ---------- annual_premium ----------
def test_unknown_car_type_true():
    # car_type not in BASE_PREMIUM -> True
    with pytest.raises(ValueError):
        annual_premium("truck", 30, 0, False)


def test_known_car_type_false_and_age_too_young_true():
    # car_type not in BASE_PREMIUM -> False, driver_age < 18 -> True
    with pytest.raises(ValueError):
        annual_premium("sedan", 17, 0, False)


def test_young_driver_age_lt_25_true():
    # driver_age < 18 -> False, driver_age < 25 -> True,
    # claims == 0 -> False, claims > 2 -> False, has_anti_theft -> True
    # hatchback 8000 + 4000 = 12000 - 500 = 11500
    assert annual_premium("hatchback", 20, 1, True) == 11500


def test_senior_driver_age_ge_60_true():
    # driver_age < 25 -> False, driver_age >= 60 -> True,
    # claims == 0 -> False, claims > 2 -> True, has_anti_theft -> False
    # suv 15000 + 2000 = 17000 * 2 = 34000
    assert annual_premium("suv", 65, 3, False) == 34000


def test_middle_age_both_age_branches_false_claims_zero_true():
    # driver_age < 25 -> False, driver_age >= 60 -> False (25..59),
    # claims == 0 -> True, has_anti_theft -> False
    # sedan 12000 - 2400 = 9600
    assert annual_premium("sedan", 30, 0, False) == 9600


def test_middle_age_claims_gt_2_false_but_not_zero():
    # claims == 0 -> False, claims > 2 -> False (1 or 2 claims)
    # sedan 12000, no adjustments, no anti-theft
    assert annual_premium("sedan", 40, 2, False) == 12000


# ---------- no_claim_bonus ----------
def test_bonus_years_negative_true():
    # claim_free_years < 0 -> True
    with pytest.raises(ValueError):
        no_claim_bonus(-1)


def test_bonus_ge_5_true():
    # < 0 False, >= 5 True
    assert no_claim_bonus(5) == 50


def test_bonus_ge_3_true():
    # >= 5 False, >= 3 True
    assert no_claim_bonus(3) == 35


def test_bonus_ge_1_true():
    # >= 3 False, >= 1 True
    assert no_claim_bonus(1) == 20


def test_bonus_all_false_returns_zero():
    # >= 5 False, >= 3 False, >= 1 False
    assert no_claim_bonus(0) == 0


# ---------- claim_payout ----------
def test_payout_invalid_amount_true():
    # damage_cost < 0 or deductible < 0 -> True
    with pytest.raises(ValueError):
        claim_payout(-100, 50000, 1000, False)


def test_payout_total_loss_true():
    # invalid -> False, is_total_loss -> True
    assert claim_payout(10000, 50000, 1000, True) == 50000


def test_payout_within_deductible_true():
    # is_total_loss -> False, damage_cost <= deductible -> True
    assert claim_payout(500, 50000, 1000, False) == 0


def test_payout_over_insured_value_true():
    # damage_cost <= deductible -> False, payout > insured_value -> True
    assert claim_payout(80000, 50000, 1000, False) == 50000


def test_payout_normal_all_remaining_false():
    # payout > insured_value -> False
    assert claim_payout(20000, 50000, 1000, False) == 19000
