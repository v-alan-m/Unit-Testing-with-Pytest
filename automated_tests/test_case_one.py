import pytest

a = 103


@pytest.mark.Smoke
def test_case_1():
    print('First test case - Smoke')


@pytest.mark.Sanity
@pytest.mark.skip("Test to be fixed at a later date.")
def test_case_3():
    print('Third test case - Sanity')


@pytest.mark.Smoke
@pytest.mark.skipif(a > 100, reason="Test to be fixed at a later date.")
def test_case_4():
    print('Fourth test case = Smoke')
