import os
import subprocess
import sys

TEST_DIR = os.path.join(os.path.dirname(__file__), 'testcases')


def discover_tests(directory):
    for root, _, files in os.walk(directory):
        for fname in files:
            if fname.endswith('.py'):
                yield os.path.join(root, fname)


def run_test(test_file):
    result = subprocess.run([sys.executable, test_file])
    return result.returncode


def main():
    if not os.path.isdir(TEST_DIR):
        print(f'No testcases directory found at {TEST_DIR}')
        sys.exit(1)
    tests = list(discover_tests(TEST_DIR))
    if not tests:
        print('No testcases found.')
        return

    failures = 0
    for test in tests:
        print(f'Running {test}...')
        code = run_test(test)
        if code != 0:
            print(f'Failed: {test}')
            failures += 1
    if failures:
        print(f"\n{failures} test(s) failed.")
        sys.exit(1)
    print('\nAll tests passed!')

if __name__ == '__main__':
    main()
