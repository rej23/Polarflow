from accesslink import AccessLink

CLIENT_ID = 
CLIENT_SECRET = 
REDIRECT_URL = "https://localhost/"

accesslink = AccessLink(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_url=REDIRECT_URL)

# Obtain the authorization code from the redirect URL
authorization_code = 

# Exchange the authorization code for an access token
token_response = accesslink.get_access_token(authorization_code)
ACCESS_TOKEN = token_response["access_token"]
USER_ID = token_response["x_user_id"]
