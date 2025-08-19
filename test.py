import requests

login_url = "https://intranet.ise.eng.chula.ac.th/?mod=user&op=login"

def test_username(username):
    payload = {
        "username": username,
        "password": "fakepassword",
        "redirect": "mod=welcome"
    }

    session = requests.Session()
    res = session.post(login_url, data=payload)

    if "Incorrect Username or Password" in res.text:
        print(f"🟡 {username}: Login failed — generic error.")
    else:
        print(f"🔍 {username}: Something unusual in response — investigate further.")

test_username("2510263")
