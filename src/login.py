from urllib.parse import urlencode

import config
import requests


async def login() -> None:
    session = requests.Session()

    url_params_dict = {
        "client_id": "https://istudent.urfu.ru",
        "redirect_uri": "https://istudent.urfu.ru",
        "resource": "https://istudent.urfu.ru",
        "type": "web_server",
        "response_type": "code"
    }
    url_params = urlencode(url_params_dict)
    login_url = "https://sts.urfu.ru/adfs/OAuth2/authorize?" + url_params

    username = config.Config.URFU_USERNAME
    password = config.Config.URFU_PASSWORD

    form = {"USERNAME": username, "PASSWORD": password, "AuthMethod": "FormsAuthentication"}
    data = urlencode(form)

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = session.post(
        login_url, data=data, headers=headers)
    
    expires_header = response.headers["expires"]
    if expires_header == "-1":
        return False, None
    return True, session