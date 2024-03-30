# pip install pystray pillow

import pystray
import PIL.Image

image = PIL.Image.open("palms.png")

def on_clicked(icon, item):
    if str(item) == "Say Hello":
        print("Hello World")
    elif str(item) == "Exit":
        icon.stop()
    elif str(item) == "Subitem 1":
        print("sub 1")
    else:
        print("not implemented yet!")

icon = pystray.Icon("Neural", image, menu=pystray.Menu(
    pystray.MenuItem("Say Hello", on_clicked),
    pystray.MenuItem("Exit", on_clicked),
    pystray.MenuItem("Submenu", pystray.Menu(
        pystray.MenuItem("Subitem 1", on_clicked),
        pystray.MenuItem("Subitem 2", on_clicked)
    ))
))

icon.run()