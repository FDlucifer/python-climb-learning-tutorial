# pip install win10toast
# pip install winotify

from win10toast import ToastNotifier

toaster = ToastNotifier()

toaster.show_toast("Title", "Message", duration=2)