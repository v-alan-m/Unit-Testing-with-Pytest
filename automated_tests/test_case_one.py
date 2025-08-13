import pytest

a = 103


def test_case_1():
    print('First test case')


@pytest.mark.skip("Test to be fixed at a later date.")
def test_case_3():
    print('Third test case')


@pytest.mark.skipif(a > 100, reason="Test to be fixed at a later date.")
def test_case_4():
    print('Fourth test case')
