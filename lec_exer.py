from requests_oauthlib import OAuth1Session
import secrets
import json

client_key = secrets.client_key
client_secret = secrets.client_secret


request_token_url = 'https://api.twitter.com/oauth/request_token'

oauth = OAuth1Session(client_key, client_secret=client_secret)
fetch_response = oauth.fetch_request_token(request_token_url)
resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')

base_authorization_url = 'https://api.twitter.com/oauth/authorize'

authorization_url = oauth.authorization_url(base_authorization_url)
print ('Please go here and authorize,', authorization_url)
verifier = input('Paste the verification code here: ')


access_token_url = 'https://api.twitter.com/oauth/access_token'

oauth = OAuth1Session(client_key,client_secret=client_secret,resource_owner_key=resource_owner_key,resource_owner_secret=resource_owner_secret,verifier=verifier)
oauth_tokens = oauth.fetch_access_token(access_token_url)

resource_owner_key = oauth_tokens.get('oauth_token')
resource_owner_secret = oauth_tokens.get('oauth_token_secret')

print(resource_owner_key, resource_owner_secret)
protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,client_secret=client_secret,resource_owner_key=resource_owner_key,resource_owner_secret=resource_owner_secret)
r = oauth.get(protected_url)
print (r.text)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
r_text = r.text
r_json = json.loads(r_text)
r_contents = r_json["statuses"]
for ele in r_contents:
    if "screen_name" in ele:
        print(ele["screen_name"])
    print("--------------------------------")
    print(ele["text"])
