import twitter
import json


def thing():
    with open('twitter_keys.json', 'r') as file:
        data = json.load(file)
    api = twitter.Api()#data["bearer_token"])
    print(api.UsersLookup(screen_name="RIT"))


