# JCW.SSW567

Fall 2025: SSW 657 - Software Testing, Quality Assurance and Maintenance

## COURSE DESCRIPTION
This course introduces students to systematic testing of software systems, software
verification, symbolic execution, software debugging, quality assurance, measurement and
prediction of software reliability, project management, software maintenance, software reuse
and reverse engineering.

## Course Workflow
For this course, I will be using conda to create a virtual environment (venv) in order to install pytest and other needed modules for this course. This will be my first time using pytest, so I have included a step-by-step tutorial on how to test python programs. All files and their changes will be stored using GitHub.

Before starting any code, activate the env in the VS Code integreated Terminal 
1. Open Anaconda Prompt or Terminal
2. Navigate to your GitHub repo:
   `cd -> repo`
3. Activate your environment:
   `conda activate SSW567`

Writing pyTest files
1. Create a sample main.py file with a function using def:

```
def get_weather(temp):
    if temp > 30:
        return "It's a hot day"
    elif temp > 20:
        return "It's a nice day"
    elif temp > 10:
        return "It's a bit chilly"
    else:
        return "It's cold"
```

2. Next, create a new file for the testing code. Usually we are testing one python file at a time. It needs to follow the same naming convention so PyTest can find it. If we are using main.py, the testing file needs to be named `test_main.py`.
3. Inside the `test_main.py` file, all you need to do to initialize it is to import the code you want to test, and then write a function contains an asserrtion..
```
from main import get_weather

def test_get_weather():
    assert get_weather(35) == "It's a hot day"
    assert get_weather(25) == "It's a nice day"
    assert get_weather(15) == "It's a bit chilly"
    assert get_weather(5) == "It's cold"
```
4. An assewrtion is going to tell us if something is true or false. So we're satying insert, some condition to be true or false. If it's true, the test passes. If it is false, it fails.
5. To run the tets, make sure you are in the directory with the test file. Then in the integreated terminal, type the following: `pytest test_main.py`

Helpful vidoe regarding unit testing. Incliudes defintions, how-to examples, test driven development, etc: [PyTest Tutorial]([https://pages.github.com/](https://youtu.be/EgpLj86ZHFQ?si=kxXrjy8FQTjtnmTj))
