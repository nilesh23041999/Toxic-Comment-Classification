import json
from kafka import KafkaProducer
import requests
import sys
import time



# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = 'Your Twitter Bearer Token'
param = {
    "expansions": "attachments.media_keys,author_id,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id",
    "media.fields": "duration_ms,height,media_key,preview_image_url,type,url,width,public_metrics,alt_text",
    "place.fields": "contained_within,country,country_code,full_name,geo,id,name,place_type",
    "poll.fields": "duration_minutes,end_datetime,id,options,voting_status",
    "tweet.fields": "attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,public_metrics,possibly_sensitive,referenced_tweets,reply_settings,source,text,withheld",
    "user.fields": "created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld"
    }

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r


def get_rules():
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def delete_all_rules(rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))


def set_rules(delete,keyword):
    # You can adjust the rules if needed
    sample_rules = [{"value": f"{keyword} lang: en"},
        ]
    payload = {"add": sample_rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def get_stream(set,timeout):

    response = requests.get("https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True,params=param )
    #response = requests.get("https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    timeout_start = time.time()
    for response_line in response.iter_lines():
        if response_line:
            producer = KafkaProducer(bootstrap_servers='localhost:9092',
                                     value_serializer=lambda m: json.dumps(m).encode('utf-8'),
                                     batch_size=524288,api_version=(2,8,0) )
            future = producer.send('twitter', json.loads(response_line))
            if time.time() > timeout_start + timeout:
                break

    #sys.exit()

def main(keyword,timeout=2400):
    print(keyword)
    rules = get_rules()
    delete = delete_all_rules(rules)
    set = set_rules(delete,keyword)
    get_stream(set,timeout)


#if __name__ == "__main__":
#   main()
