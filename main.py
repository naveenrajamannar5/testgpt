from testcases import test_sql_injection


def main():
    target = "http://localhost:3000"
    result = test_sql_injection.test_sql_injection(target)

    if result["vulnerable"]:
        print(f"\u2705 SQL Injection detected with payload: {result['payload']}")
    else:
        print("\u2705 Not vulnerable to SQL Injection")


if __name__ == "__main__":
    main()
