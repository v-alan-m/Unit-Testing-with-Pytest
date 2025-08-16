from datetime import datetime
import pytest

a = 103

actual_result = 'Hello'


def pytest_sessionstart(session):
    session.session_start_time = datetime.now()


@pytest.fixture(scope='module')
def fixture_code():
    print("This is our fixture code to execute before the test case")
    print("-"*26)
    yield
    print('\nFunction to run after the test case comes after the word yield')
    print("-" * 26)


@pytest.mark.Smoke
def test_case_1(fixture_code):
    print('First test case - Smoke')
    assert actual_result != 'Hello', "These 2 values are expected to not be the same."


@pytest.mark.Sanity
@pytest.mark.skip("Test to be fixed at a later date.")
def test_case_3(fixture_code):
    print('Third test case - Sanity')


@pytest.mark.Smoke
@pytest.mark.skipif(a > 100, reason="Test to be fixed at a later date.")
def test_case_4(fixture_code):
    print('Fourth test case = Smoke')
