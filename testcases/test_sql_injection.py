import requests
import argparse
import sys


def test_sql_injection(base_url):
    payload = "' OR 1=1--"
    r = requests.get(f"{base_url}/rest/products/search", params={"q": payload})

    if r.status_code == 200 and "error" not in r.text.lower():
        return {"vulnerable": True, "payload": payload}
    return {"vulnerable": False}


def main():
    parser = argparse.ArgumentParser(description="SQL injection test")
    parser.add_argument("--base-url", default="http://localhost:3000",
                        help="Base URL of the target application")
    args = parser.parse_args()

    result = test_sql_injection(args.base_url)
    if result["vulnerable"]:
        print("SQL Injection vulnerability detected with payload:", result["payload"])
        sys.exit(1)
    else:
        print("No SQL Injection vulnerability detected.")
        sys.exit(0)


if __name__ == "__main__":
    main()
