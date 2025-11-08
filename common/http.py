import requests

def get_session(user_agent: str = "NayeAPIs/1.0") -> requests.Session:
    s = requests.Session()
    s.headers.update({
        "User-Agent": user_agent
    })
    return s