## Introduction to Pytest
- Unit testing framework for python
- Options to conditionally execute cases
- Can setup pre-requisite and post scripts
    - E.g: Pre-requisite scripts: Connect to database
    - E.g. Post scripts - Disconnect from database
- Can add assertions
    - Compare the expected and real output result
- Options to generate report


# Setup
- Install Pytest:
```shell
pip install pytest
```


## How to Write Test Cases in Pytest
- Test must be written within functions
- Where test functions must begin with the string 'test'
    - For Pytest to detect them as test

- Run a test:
```shell
pyest <filename.py>
```


## Grouping(Tagging)
- Test cases should be created within specific folders for ease of organisation.


## Running multiple tests
- To run multiple test files, the folder can be used within the terminal command.
    - Note: In order for this to work, the test filename(s) must begin with the string 'test_'.
```shell
pyest <test_folder_name>
```


## Show the test comparison results within the output:
```shell
pyest -v <test_folder_name>
```
```shell
automated_tests/test_case_one.py::test_case_1 PASSED
automated_tests/test_case_one.py::test_case_3 PASSED
automated_tests/test_case_two.py::test_case_2 PASSED
```

## Show print statements within the output:
```shell
pyest -s -v <test_folder_name>
```
```shell
automated_tests/test_case_one.py::test_case_1 PASSED
automated_tests/test_case_one.py::test_case_3 PASSED
automated_tests/test_case_two.py::test_case_2 PASSED
```

## Skip tests
- Use decorator to skip specific tests:
```shell
@pytest.mark.skip
def test_case_3():
    print('Third test case')
```
```shell
automated_tests/test_case_one.py::test_case_1 PASSED
automated_tests/test_case_one.py::test_case_3 SKIPPED (unconditional skip)
automated_tests/test_case_two.py::test_case_2 PASSED
```
- Write comment on why the test was skipped:
```shell
@pytest.mark.skip("Test to be fixed at a later date.")
def test_case_3():
    print('Third test case')
```
```shell
automated_tests/test_case_one.py::test_case_1 PASSED
automated_tests/test_case_one.py::test_case_3 SKIPPED (Test to be fixed at a later date.)
automated_tests/test_case_two.py::test_case_2 PASSED
```

### Skip the test case for given condition in the code
- Scenario 1: 
  - Condition not met ->  Test is not skipped
```shell
a = 80

@pytest.mark.skipif(a > 100, reason="Test to be fixed at a later date.")
def test_case_3():
    print('Third test case')
```
```shell
automated_tests/test_case_one.py::test_case_1 PASSED
automated_tests/test_case_one.py::test_case_3 SKIPPED (Test to be fixed at a later date.)
automated_tests/test_case_one.py::test_case_4 PASSED
automated_tests/test_case_two.py::test_case_2 PASSED
```
- Scenario 2: 
  - Condition is met -> Test is skipped

```shell
a = 103

@pytest.mark.skipif(a > 100, reason="Test to be fixed at a later date.")
def test_case_3():
    print('Third test case')
```
```shell
automated_tests/test_case_one.py::test_case_1 PASSED
automated_tests/test_case_one.py::test_case_3 SKIPPED (Test to be fixed at a later date.)
automated_tests/test_case_one.py::test_case_4 SKIPPED (Test to be fixed at a later date.)
automated_tests/test_case_two.py::test_case_2 PASSED
```

### Run a single test, from a file with multiple test, without skipping
- Use test name:
```shell
pytest s -v -k  <test_name> <folder_name>
pytest -s -v -k test_case_1 automated_tests
```
```shell
automated_tests/test_case_one.py::test_case_1 First test case
PASSED
============================ 1 passed, 3 deselected in 0.02s ============================
```

### Run runs with a given partial string within the function names
```shell
pytest s -v -k  <string> <folder_name>
pytest -s -v -k case automated_tests
```
```shell
automated_tests/test_case_one.py::test_case_1 First test case
PASSED
automated_tests/test_case_one.py::test_case_3 SKIPPED (Test to be fixed at a later date.)
automated_tests/test_case_one.py::test_case_4 SKIPPED (Test to be fixed at a later date.)
automated_tests/test_case_two.py::test_case_2 Second test case
PASSED
```

## Fixtures and Assertions


## Project Implementation

