## 📘 Introduction to Pytest
- Unit testing framework for python
- Options to conditionally execute cases
- Can setup pre-requisite and post scripts
    - E.g: Pre-requisite scripts: Connect to database
    - E.g. Post scripts - Disconnect from database
- Can add assertions
    - Compare the expected and real output result
- Options to generate report


# ⚙️ Setup
- Install Pytest:
```shell
pip install pytest
```


## ✍️ How to Write Test Cases in Pytest
- Test must be written within functions
- Where test functions must begin with the string 'test'
    - For Pytest to detect them as test

- Run a test:
```shell
pyest <filename.py>
```

## 📂 Running multiple tests
- Test cases should be created within specific folders for ease of organisation.
- To run multiple test files, the folder can be used within the terminal command.
    - Note: In order for this to work, the test filename(s) must begin with the string 'test_'.
```shell
pyest <test_folder_name>
```


## 📊 Show the test comparison results within the output:
```shell
pyest -v <test_folder_name>
```
```shell
automated_tests/test_case_one.py::test_case_1 PASSED
automated_tests/test_case_one.py::test_case_3 PASSED
automated_tests/test_case_two.py::test_case_2 PASSED
```

## 🖨️ Show print statements within the output:
```shell
pyest -s -v <test_folder_name>
```
```shell
automated_tests/test_case_one.py::test_case_1 PASSED
automated_tests/test_case_one.py::test_case_3 PASSED
automated_tests/test_case_two.py::test_case_2 PASSED
```

## ⏭️ Skip tests
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

### 🔄 Skip the test case for given condition in the code
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

### 🎯 Run a single test, from a file with multiple test, without skipping
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

### 🔍 Run runs with a given partial string within the function names
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

## 🏷️ Grouping(Tagging)
- Test a sub set for all tests for a given reason.
- **Tags** are used to create groups, for testing specific groups of tests.
  - Use decorator `@pytest.mark.<string>`
```shell
@pytest.mark.Smoke
@pytest.mark.Sanity
```
- Create `pytest.ini` file to add new tags, to prevent warnings and errors:
```shell
[pytest]
markers =
    Smoke: mark a test as part of the smoke test suite
    Sanity: mark a test as part of the sanity test suite
```
- Execute test cases based on tags:
  - Use `pytest -s -v -m <tag> <test_folder_name>`
```shell
pytest -s -v -m Smoke automated_tests
```
```shell
automated_tests/test_case_four.py::test_case_7 Seventh test case - Smoke
PASSED
automated_tests/test_case_one.py::test_case_1 First test case - Smoke
PASSED
automated_tests/test_case_one.py::test_case_4 SKIPPED (Test to be fixed at a later date.)
automated_tests/test_case_three.py::test_case_5 Fifth test case - Smoke
PASSED

============================ 3 passed, 1 skipped, 3 deselected in 0.03s ============================
```

### 🚫 Skip test cases based on tags
  - Use `pytest -s -v -m <"not tag"> <test_folder_name>`
```shell
pytest -s -v -m "not Smoke" automated_tests
```
```shell
automated_tests/test_case_one.py::test_case_3 SKIPPED (Test to be fixed at a later date.)
automated_tests/test_case_three.py::test_case_6 Sixth test case - Sanity
PASSED
automated_tests/test_case_two.py::test_case_2 Second test case - Sanity
PASSED
============================ 2 passed, 1 skipped, 4 deselected in 0.03s ============================
```
### ➕ Run test on a set of tags
  - Use `pytest -s -v -m <"tag_1 or tag_2"> <test_folder_name>`
```shell
pytest -s -v -m "Smoke or Sanity" automated_tests
```
```shell
automated_tests/test_case_four.py::test_case_7 Seventh test case - Smoke
PASSED
automated_tests/test_case_one.py::test_case_1 First test case - Smoke
PASSED
automated_tests/test_case_one.py::test_case_3 SKIPPED (Test to be fixed at a later date.)
automated_tests/test_case_one.py::test_case_4 SKIPPED (Test to be fixed at a later date.)
automated_tests/test_case_three.py::test_case_5 Fifth test case - Smoke
PASSED9
automated_tests/test_case_three.py::test_case_6 Sixth test case - Sanity
PASSED
automated_tests/test_case_two.py::test_case_2 Second test case - Sanity
PASSED
============================ 5 passed, 2 skipped in 0.03s ============================
```
### ⚖️ Run test on compound tags
```shell
pytest -s -v -m "Smoke and Regression" automated_tests
```
```shell
automated_tests/test_case_four.py::test_case_7 Seventh test case - Smoke
PASSED
============================ 1 passed, 6 skipped in 0.02s ============================
```

## ✅ Assertions
### 🔁 Compare data - To be the same 
- Use `assert actual_result == 'Hello'`
- Run using `-v`
- Not the same:
```shell
actual_result = 'Testing'

@pytest.mark.Smoke
def test_case_1():
    print('First test case - Smoke')
    assert actual_result == 'Hello'
```
```shell
E       AssertionError: assert 'Testing' == 'Hello'
E         
E         - Hello
E         + Testing
```
- Same:
```shell
actual_result = 'Hello''

@pytest.mark.Smoke
def test_case_1():
    print('First test case - Smoke')
    assert actual_result == 'Hello'
```
```shell
automated_tests/test_case_one.py::test_case_1 PASSED
```
### 🚫 Compare data - To be bot the same 
- Use `assert actual_result != 'Hello'`
- Not the same
```shell
actual_result = 'Testing'

@pytest.mark.Smoke
def test_case_1():
    print('First test case - Smoke')
    assert actual_result != 'Hello'
```
### 📝 Compare data - custom message in case of failure
- Use `actual_result != 'Hello', "<message>"`
  - E.g: `actual_result != 'Hello', "These 2 values are expected to not be the same."`
```shell
actual_result = 'Hello'


@pytest.mark.Smoke
def test_case_1():
    print('First test case - Smoke')
    assert actual_result != 'Hello', "These 2 values are expected to not be the same."
```
```shell
E       AssertionError: These 2 values are expected to not be the same.
E       assert 'Hello' != 'Hello'
```

## 🧩 Fixtures
### ⏩ Run code before the test case
- Define a fixture method, using: `@pytest.fixture()`
  - Then insert the fixture function name as an argument, into the target test cases functions
- Run using `-s`
```shell
@pytest.fixture()
def fixture_code():
    print("This is our fixture code to execute before the test case")
    print("-"*26)

@pytest.mark.Smoke
def test_case_1(fixture_code):
    print('First test case - Smoke')
    assert actual_result != 'Hello', "These 2 values are expected to not be the same."
```
```shell
automated_tests/test_case_one.py::test_case_1 This is our fixture code to execute before the test case
--------------------------
First test case - Smoke
PASSED
```
### ⏹️ Run code after the test case
- The function to run after the test case comes after the word yield
```shell
@pytest.fixture()
def fixture_code():
    print("This is our fixture code to execute before the test case")
    print("-"*26)
    yield
    print('\nFunction to run after the test case comes after the word yield')
    print("-" * 26)
```
```shell
automated_tests/test_case_one.py::test_case_1 This is our fixture code to execute before the test case
--------------------------
First test case - Smoke
PASSED
Function to run after the test case comes after the word yield
--------------------------
```
### 🔄 Run the fixture code only once before and after all the test cases, not before and after each test case
- Use `@pytest.fixture(scope='module')`
```shell
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
    assert actual_result == 'Hello', "These 2 values are expected to not be the same."


@pytest.mark.Sanity
@pytest.mark.skip("Test to be fixed at a later date.")
def test_case_3(fixture_code):
    print('Third test case - Sanity')


@pytest.mark.Smoke
@pytest.mark.skipif(a > 100, reason="Test to be fixed at a later date.")
def test_case_4(fixture_code):
    print('Fourth test case = Smoke')
```
```shell
automated_tests/test_case_one.py::test_case_1 This is our fixture code to execute before the test case
--------------------------
First test case - Smoke
PASSED
automated_tests/test_case_one.py::test_case_3 SKIPPED (Test to be fixed at a later date.)
automated_tests/test_case_one.py::test_case_4 SKIPPED (Test to be fixed at a later date.)
Function to run after the test case comes after the word yield
--------------------------
```
## 📑 Reporting
- Advanced HTML formatted report
- High level execution status in tabular format
- Display graphical trend by comparing execution status with previous build
- Display low level information at the level of test cases
- Display clear information, about the reason for the FAILURE, if any
- Install: `pip install pytest-html`
Example
- If we use:
```shell
actual_result = 'Hello'

@pytest.mark.Smoke
def test_case_1(fixture_code):
    print('First test case - Smoke')
    assert actual_result != 'Hello', "These 2 values are expected to not be the same."
```
- Run test: `pytest automated_tests --html=./report.html`
  - An HTML file named report.html is created
  - Open in a browser, to see the results