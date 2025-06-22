import requests


def test_sql_injection(target: str):
    """Simple SQL injection test that tries a generic payload."""
    payload = "' OR '1'='1"
    url = target
    try:
        response = requests.get(url, params={"q": payload}, timeout=5)
        if response.status_code == 200 and payload in response.text:
            return {"vulnerable": True, "payload": payload}
    except Exception:
        pass
    return {"vulnerable": False, "payload": None}
