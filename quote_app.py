import redis
import json
import requests


redis_connection = redis.Redis(
    host='localhost',
    port=6379,
    charset='utf-8',
    decode_responses=True
)


def rand_quote():
    get_quote = input("If you would like a random quote, type 'y' and enter: ")
    if get_quote == 'y':
        print(redis_connection.randomkey())
    else: pass

def add_quote():
    add_quote = input("If you would like to add your own quote, type 'y' and enter: ")
    if add_quote == 'y':
        new_quote = input("Please enter your quote followed by enter: ")
        new_author = input("Please enter your name followed by enter: ")
        print("Thank you for your input!")
    else: pass
    redis_connection.set(new_quote, new_author)

rand_quote()
add_quote()