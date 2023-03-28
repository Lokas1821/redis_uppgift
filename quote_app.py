import redis
import json
import requests
import random

redis_connection = redis.Redis(
    host='localhost',
    port=6379,
    charset='utf-8',
    decode_responses=True
)

def store_quotes():
    response = requests.get("https://dummyjson.com/quotes")
    quotes = json.loads(response.text)
    redis_connection.set('quotes', json.dumps(quotes))

def get_quote():
    quotes = json.loads(redis_connection.get('quotes'))
    quote = random.choice(quotes['quotes'])
    return quote

def add_quote(quote, author):
    new_quote = {"quote": quote, "author": author}
    quotes = json.loads(redis_connection.get('quotes'))
    quotes['quotes'].append(new_quote)
    redis_connection.set('quotes', json.dumps(quotes))

if __name__ == '__main__':
    store_quotes()

    while True:
        print("1. Get a random quote")
        print("2. Add a new quote")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            quote = get_quote()
            print(f'"{quote["quote"]}" - {quote["author"]}\n')
        elif choice == '2':
            quote = input("Enter the quote: ")
            author = input("Enter the author: ")
            add_quote(quote, author)
            print("Quote added successfully!\n")
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.\n")