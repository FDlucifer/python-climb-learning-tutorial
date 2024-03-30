from pynput import mouse

def on_move(x, y):
    print(f'Mouse moved to {x}, {y}')

def start_listening():
    with mouse.Listener(on_move=on_move) as listener:
        listener.join()

start_listening()