import pytest
from recycling_rewards import reward_points, collection_accepted, slot_status

# Example test cases:
def test_below_minimum_weight():
    assert reward_points("paper", 3, False) == 0

def test_collection_accepted():
    assert collection_accepted(20, 2, False) is True

# Write the rest of the test cases so that the code is 90-100% covered.


def test_paper_above_minimum_without_bonus():
    assert reward_points("paper", 8, False) == 18

def test_metal_high_weight():
    assert reward_points("metal", 25, False) == 414


def test_morning_slot_open():
    assert slot_status(25, True, False) == "open"

def test_hazardous_collection_within_limit():
    assert collection_accepted(4, 2, True) is True

def test_evening_holiday_slot_statuses():
    assert slot_status(25, False, True) == "open"
    assert slot_status(15, False, True) == "late"
    assert slot_status(5, False, True) == "missed"

def test_overweight_collection_rejected():
    assert collection_accepted(55, 2, False) is False

# branch coverage

def test_invalid_material():
    with pytest.raises(ValueError, match="unknown material"):
        reward_points("glass", 10, False)

def test_negative_weight():
    with pytest.raises(ValueError, match="invalid weight"):
        reward_points("paper", -1, False)
