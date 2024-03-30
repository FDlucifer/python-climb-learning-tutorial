# pip install speedtest-cli
import speedtest

test = speedtest.Speedtest()

print("loading server lists...")
test.get_servers() # -> get list of servers
print("Choosing best server...")
best = test.get_best_server() # -> choose best server

print(best)
print(f"Found: {best['host']} located in {best['country']}")

print("performing download test...")
download_result = test.download()
print(f"download speed: {download_result / 1024 / 1024:.2f} Mbit/s")
print("performing upload test...")
upload_result = test.upload()
print(f"upload speed: {upload_result / 1024 / 1024:.2f} Mbit/s")
print("performing ping test...")
ping_result = test.results.ping
print(f"ping: {ping_result:.2f} ms")