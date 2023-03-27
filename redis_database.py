import redis
import json
import requests



redis_connection = redis.Redis(
    host='localhost',
    port=6379,
    charset='utf-8',
    decode_responses=True
)

response = requests.get("https://dummyjson.com/quotes")
list_quote = response.text
quote = json.loads(response.text)

'''
Below we can move the data to the redis database, but we cannot find a way to navigate the data, like we can
in the commented out section below. I think it might be the wrong format.  
'''
for k, v in quote:
    my_key = k
    my_value = v
    redis_connection.set(my_key, my_value)


'''
# navigate quotes in python
print(type(quote))
print((quote['quotes'][2]))
'''


