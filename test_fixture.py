import pytest

@pytest.mark.xfail
def test_divisible_by_three(input_value):
    assert input_value % 3 == 0

@pytest.mark.skip
def test_divisible_by_nine(input_value):
    assert input_value % 9 == 0