from typing import Mapping
from neuralintents import GenericAssistant
import pandas_datareader as web
import sys

stock_tickers = ['AAPL', 'FB', 'GS', 'TSLA']

todos = ['Wash car', 'Watch NeuralNine videos', 'Go shopping']

def stock_function():
    for ticker in stock_tickers:
        data = web.DataReader(ticker, 'yahoo')
        print(f"the last price of {ticker} was {data['Close'].iloc[-1]}")

def todo_show():
    print("your todo list:")
    for todo in todos:
        print(todo)

def todo_add():
    todo = input("what todo do you want to add: ")
    todos.append(todo)

def todo_remove():
    idx = int(input("whitch todo to remove (number): ")) - 1
    if idx < len(todos):
        print(f"removing {todos[idx]}")
        todos.pop(idx)
    else:
        print("there is no todo at this position")

def bye():
    print("bye")
    sys.exit(0)

mappings = {'stocks': stock_function, 'todoshow': todo_show, 'todoadd': todo_add, "todoremove": todo_remove, "goodbye": bye}

assistant = GenericAssistant("intents.json", mappings)

assistant.train_model()
assistant.save_model()

while True:
    message = input('Message: ')
    assistant.request(message)