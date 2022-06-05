import time
from winotify import Notification, audio

toast = Notification(app_id="fdlucifer",
                    title="Message Title",
                    msg="Hello World",
                    duration="short")

toast.add_actions(label="click me!", launch="https://fdlucifer.github.io/")
toast.set_audio(audio.SMS, loop=False)

toast.show()