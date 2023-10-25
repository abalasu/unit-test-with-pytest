import module1
import pytest

@pytest.mark.complete
@pytest.mark.parametrize("num, result",[(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,0), (8,1), (8,2)])
def test_case1(num, result):
    assert module1.mod_7(num) == result

@pytest.mark.first_two
def test_case2():
    my_list = [1,2,3,4,5,6,7]
    results = [1,3,3,4,5,5,0]
    assert module1.mod_7(my_list[1]) == results[1]

@pytest.mark.other_two
def test_case3():
    my_list = [1,2,3,4,5,6,7]
    results = [1,3,3,4,5,5,0]
    assert module1.mod_7(my_list[2]) == results[2]

@pytest.mark.other_two
def test_case4():
    my_list = [1,2,3,4,5,6,7]
    results = [1,3,3,4,5,5,0]
    assert module1.mod_7(my_list[3]) == results[3]

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

@pytest.mark.xfail
def test_divisible_by_6(input_value):
   assert input_value % 6 == 0