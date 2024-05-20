## According to the following URL, the code is based on the code in the URL.
## https://twikit.readthedocs.io/en/latest/index.html

## Note: Create a file named "SECRETS.py" in the same directory as this file and write the following code.
## USERNAME = "Your Twitter Username"
## EMAIL = "Your Twitter Email"
## PASSWORD = "Your Twitter Password"

from twikit import Client
import argparse
import traceback
import unicodedata
import SECRETS

def get_east_asian_width_count(text):
    count = 0
    for c in text:
        if unicodedata.east_asian_width(c) in "FWA":
            count += 2
        else:
            count += 1
    return count


def login_and_save_cookies(client):
    client.login(
        auth_info_1=SECRETS.USERNAME,
        auth_info_2=SECRETS.EMAIL,
        password=SECRETS.PASSWORD,
    )
    client.save_cookies("COOKIES.json")


def load_cookies(client):
    try :
        client.load_cookies("COOKIES.json")
    except:
        return False
    
    return True

def create_tweet(client, tweet_text, images):
    if get_east_asian_width_count(tweet_text) > 280:
        print("❌ Tweet is too long")
        return

    if len(tweet_text) == 0:
        print("❌ Tweet is empty")
        return

    MEDIA_IDS = []
    if images:
        for image in images:
            MEDIA_IDS.append(client.upload_media(image))

    try:
        client.create_tweet(text=tweet_text, media_ids=MEDIA_IDS)
    except:
        print("😭 An error occurred")
        ## 詳細
        traceback.print_exc()

        return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("tweet", help="the text of the tweet")
    parser.add_argument(
        "-i", "--images", nargs="*", help="the images to attach to the tweet"
    )
    args = parser.parse_args()

    client = Client("en-US")

    if not load_cookies(client):
        login_and_save_cookies(client)

    create_tweet(client, args.tweet, args.images)


if __name__ == "__main__":
    main()
