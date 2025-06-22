import os
import subprocess
import sys
import argparse

TEST_DIR = os.path.join(os.path.dirname(__file__), 'testcases')


def discover_tests(directory):
    for root, _, files in os.walk(directory):
        for fname in files:
            if fname.endswith('.py'):
                yield os.path.join(root, fname)


def run_test(test_file, base_url):
    result = subprocess.run([sys.executable, test_file, "--base-url", base_url])
    return result.returncode


def main():
    parser = argparse.ArgumentParser(description="Run all security testcases")
    parser.add_argument("--base-url", default="http://localhost:3000",
                        help="Base URL for the target application")
    args = parser.parse_args()

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
        code = run_test(test, args.base_url)
        if code != 0:
            print(f'Failed: {test}')
            failures += 1
    if failures:
        print(f"\n{failures} test(s) failed.")
        sys.exit(1)
    print('\nAll tests passed!')

if __name__ == '__main__':
    main()
