"""
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
redis_connection.ping()
print(quote['quotes'][0]['author'])
redis_connection.jsonset('quotes', '.', json.dumps(quote))
"""

'''
Below we can move the data to the redis database, but we cannot find a way to navigate the data, like we can
in the commented out section below. I think it might be the wrong format.  
'''
#my_quotes = quote['quotes']
#dict.fromkeys(my_quotes)
#print(type(my_quotes)){
#redis_connection.mset(my_quotes)
#for k, v in my_quotes:
#    my_key = k
#    my_value = v
#    redis_connection.mset(my_key, my_value)

'''
# navigate quotes in python
print(type(quote))
print((quote['quotes'][2]))
'''


