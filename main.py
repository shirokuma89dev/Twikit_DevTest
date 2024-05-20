from twikit import Client
import json
import SECRETS

# Initialize client
client = Client('en-US')

if not client.is_logged_in():
    client.login(
        auth_info_1=SECRETS.USERNAME ,
        auth_info_2=SECRETS.EMAIL,
        password=SECRETS.PASSWORD
    )

    client.save_cookies('COOKIES.json')

with open('COOKIES.json', 'r', encoding='utf-8') as f:
    client.set_cookies(json.load(f))

client.create_tweet(
    text='こんにちは'
)
