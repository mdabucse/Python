import inspect
import time
import os
import importlib.util

def fixture(func):
    func._is_fixture = True
    return func

def load_module_from_path(file_path):
    """Dynamically load a Python module from file path"""
    module_name = os.path.basename(file_path).replace(".py", "")
    
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    return module


def run_tests_in_module(module):
    functions = inspect.getmembers(module, inspect.isfunction)

    results = {
        "total": 0,
        "passed": 0,
        "failed": 0,
        "errors": 0
    }

    for name, func in functions:
        if name.startswith("test_"):
            results["total"] += 1
            start_time = time.time()

            error_message = ""
            error_type = ""

            try:
                func()
                status = "PASS"
                results["passed"] += 1

            except AssertionError as e:
                status = "FAIL"
                results["failed"] += 1
                error_message = str(e)
                error_type = "AssertionError"

            except Exception as e:
                status = "ERROR"
                results["errors"] += 1
                error_message = str(e)
                error_type = type(e).__name__

            duration = time.time() - start_time

            print(f"  {status:<5} {name:<30} [{duration:.4f}s]")

            if error_message:
                print(f"        {error_type}: {error_message}")

    return results


def discover_and_run(test_dir):
    print("=== Test Discovery ===\n")

    test_files = []

    for file in os.listdir(test_dir):
        if file.startswith("test_") and file.endswith(".py"):
            test_files.append(os.path.join(test_dir, file))

    print(f"Found {len(test_files)} test files\n")

    total_results = {
        "total": 0,
        "passed": 0,
        "failed": 0,
        "errors": 0
    }

    total_start = time.time()

    print("=== Running Tests ===\n")

    for file_path in test_files:
        print(f"{file_path}")

        module = load_module_from_path(file_path)
        results = run_tests_in_module(module)

        # Aggregate results
        for key in total_results:
            total_results[key] += results[key]

    total_time = time.time() - total_start

    print("\n=== Summary ===")
    print(f"{total_results['total']} tests | "
          f"{total_results['passed']} passed | "
          f"{total_results['failed']} failed | "
          f"{total_results['errors']} errors")
    print(f"Total time: {total_time:.4f}s")