from requests_oauthlib import OAuth1Session
import json
import urllib.parse
# Consumer Key (API Key)    
CK = "nvYq34Smyl8uHfv7Y1KaBjSwe"
# Consumer Secret (API Secret)   
CS = "SU8YL514uNim0jVPa2wrnuxj2HL5Yw3SFLyHy9Uqtfr7SSE872"
# Access Token    
AT = "2484987504-1244mmO860NvKpSR22g3ueNyAQZrALX9kZpb7nK"
# Access Token Secret   
AS =  "GJcvCFMhEMvgy6eQrnqENyImgjmsIBQfJA8BNvSzSxEkX"

# twitter = OAuth1Session(CK, CS, AT, AS)
def tweet_search(search_word):
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    params = {
        "q": search_word.encode('utf-8') ,
        "lang": "ja",
        "result_type": "mixed",
        "count": "100"
        }
    oath = OAuth1Session(CK, CS, AT, AS)
    responce = oath.get(url, params = params)
    if responce.status_code != 200:
        print("Error code: %d" %(responce.status_code))
        return None
    tweets = json.loads(responce.text)
    return tweets

tweets = tweet_search("二郎")
# print(tweets)
print(tweets)
# print(json.dumps(tweets, sort_keys = True, indent = 4))
j = 0
tweet = []
for i in tweets["statuses"]:
#     print(i['text'])
    tweet.append(i['text'])
    print(j)
    j += 1
print(tweet)
for i in tweet:
    print(i)