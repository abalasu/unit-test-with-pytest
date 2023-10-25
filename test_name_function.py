import pytest
from name_function import get_formatted_name

@pytest.mark.name
@pytest.mark.parametrize("fname, lname",[("Arul", "balasubramanian"), ("Madhavv", "Arul")])
def test_get_formatted_name(fname, lname):
    formatted_name = get_formatted_name(fname, lname)
    assert formatted_name == fname + ' ' + lname

@pytest.mark.name
def test_get_formatted_name1():
    formatted_name = get_formatted_name('Madhavv','arul')
    assert formatted_name == 'Madhavv Arul'

@pytest.mark.others
def test_get_formatted_name2():
    formatted_name = get_formatted_name('Madhavv','arul')
    assert formatted_name == 'Madhavv Arul'