# MiniTest — Custom Python Testing Framework

A lightweight testing framework built from scratch in Python, inspired by `pytest`.

---

## Features

- **Test Discovery** (`test_*.py`, `test_*` functions)
-  **Automatic Test Execution**
- **Assertions Handling**
- **Clean Output (PASS / FAIL / ERROR)**
-  **Execution Time Tracking**
- **Summary Report**
- **Fixtures Support**
  - Function & Session scope
  - Dependency Injection
  - `yield` based teardown
- **Multi-file Test Execution**

---

## Project Structure
```
Task-11/
│
├── minitest.py
├── run.py
│
└── tests/
    ├── test_auth.py
    ├── test_cart.py
    └── test_utils.py
```