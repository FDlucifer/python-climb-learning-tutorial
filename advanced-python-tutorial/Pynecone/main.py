# pip install pynecone
# pc init
# pc run

import pynecone as pc

class State(pc.State):
    count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

def index():
    return pc.hstack(
        pc.button("-", color_schema="red", border_radius="1em", on_click=State.decrement),
        pc.heading(State.count, font_size="2em")
        pc.button("+", color_schema="green", border_radius="1em", on_click=State.increment),
    )

app = pc.App(state=State)
app.add_page(index, path="/")
app.compile()
