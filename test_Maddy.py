import pytest
import Madhavv_fun

@pytest.mark.parametrize("num1, num2",[(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,0), (8,1), (8,2)])
def test_case1(num1, num2):
    num3 = num1 + num2
    if num1 == 4:
        num3 = num3 + 1
    assert Madhavv_fun.Mad_fun(num1, num2) == num3

@pytest.mark.parametrize("num1, num2",[(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,0), (8,1), (8,2)])
@pytest.mark.test_case2 
def test_case2(num1, num2):
    num3 = num1 * num2
    if num1 == 5:
        num3 = num3 + 1
    assert Madhavv_fun.Mad_fun1(num1, num2) == num3    
