### Initial Run - initial py
```
(SSW567) PS C:\Users\icecr\JCW.SSW567\HW\HW03C-Coverage> pylint .\HW00b.py
************* Module HW00b
HW00b.py:7:0: C0303: Trailing whitespace (trailing-whitespace)
HW00b.py:15:0: C0303: Trailing whitespace (trailing-whitespace)
HW00b.py:20:0: C0303: Trailing whitespace (trailing-whitespace)
HW00b.py:1:0: C0114: Missing module docstring (missing-module-docstring)
HW00b.py:1:0: C0103: Module name "HW00b" doesn't conform to snake_case naming style (invalid-name)
HW00b.py:1:0: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 5.71/10
```

### post modifications - initial py
```
(SSW567) PS C:\Users\icecr\JCW.SSW567\HW\HW03C-Coverage> pylint .\HW03C_modification.py
************* Module HW03C_modification
HW03C_modification.py:1:0: C0114: Missing module docstring (missing-module-docstring)
HW03C_modification.py:1:0: C0103: Module name "HW03C_modification" doesn't conform to snake_case naming style (invalid-name)
HW03C_modification.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 8.12/10

(SSW567) PS C:\Users\icecr\JCW.SSW567\HW\HW03C-Coverage> pylint .\hw03c_modification.py

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 8.12/10, +1.88)
```

### inital run - test file
```
(SSW567) PS C:\Users\icecr\JCW.SSW567\HW\HW03C-Coverage> pylint .\test_HW00b.py
************* Module test_HW00b
test_HW00b.py:1:0: C0114: Missing module docstring (missing-module-docstring)
test_HW00b.py:1:0: C0103: Module name "test_HW00b" doesn't conform to snake_case naming style (invalid-name)
test_HW00b.py:12:0: C0116: Missing function or method docstring (missing-function-docstring)
test_HW00b.py:23:0: C0116: Missing function or method docstring (missing-function-docstring)
test_HW00b.py:36:0: C0116: Missing function or method docstring (missing-function-docstring)     
test_HW00b.py:47:0: C0116: Missing function or method docstring (missing-function-docstring)     
test_HW00b.py:61:0: C0116: Missing function or method docstring (missing-function-docstring)

-----------------------------------
Your code has been rated at 4.17/10
```

### post modifications - test file
```
(SSW567) PS C:\Users\icecr\JCW.SSW567\HW\HW03C-Coverage> pylint .\test_hw03c.py
************* Module test_hw03c
test_hw03c.py:57:0: C0301: Line too long (105/100) (line-too-long)
test_hw03c.py:1:0: C0114: Missing module docstring (missing-module-docstring)

-----------------------------------
Your code has been rated at 8.33/10

(SSW567) PS C:\Users\icecr\JCW.SSW567\HW\HW03C-Coverage> pylint .\test_hw03c.py

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 8.33/10, +1.67)
```

### coverage test
```
(SSW567) PS C:\Users\icecr\JCW.SSW567\HW\HW03C-Coverage> coverage report -m
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
hw03c_modification.py      17      0   100%
-----------------------------------------------------
TOTAL                      17      0   100%
```