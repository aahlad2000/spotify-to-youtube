from fastapi import APIRouter, Request
import urllib.parse
from lib.utils import generate_random_string
import requests
import base64
from fastapi.responses import RedirectResponse

router = APIRouter()
redirect_uri = 'http://localhost:8000/callback'
client_id = 'aa770cc608e74d229b8f89175cae58b5'
client_secret = 'e3999d3771274eabbe9e43e8356f3c6e'

@router.get("/login")
def redirect():
    try:
        state = generate_random_string(16)
        scope = 'user-read-private user-read-email'

        query_params = {
            'response_type': 'code',
            'client_id': client_id,
            'scope': scope,
            'redirect_uri': redirect_uri,
            'state': state
        }
        authorization_url = 'https://accounts.spotify.com/authorize?' + urllib.parse.urlencode(query_params)
        print(f"authorization_url : {authorization_url}")
        return RedirectResponse(url= authorization_url, status_code=302)
    except Exception as e:
        print(f"Failed to login: {e}")

@router.get("/callback")
def callback(request: Request):
    code = request.query_params.get('code') or None
    state = request.query_params.get('state') or None

    query_params = urllib.parse.urlencode({
    'error': 'state_mismatch'
    })

    if(state == None):
        print("State is null")
        return RedirectResponse(url=f"/#?{query_params}")
    else:
        auth_url = 'https://accounts.spotify.com/api/token'
        auth_headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode('utf-8')
        }
        auth_form = {
        'code': code,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
        }
        response = requests.post(auth_url, data=auth_form, headers=auth_headers)
        response_data = response.json()
        return response_data