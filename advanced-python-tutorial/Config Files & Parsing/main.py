from configparser import ConfigParser

config = ConfigParser()

config["DEFAULT"] = {
    "numberdigits": 6,
    "numbertries": 8,
    "playername": "Player"
}

config["luci11"] = {
    "numberdigits": 10,
    "numbertries": 8,
    "playername": "Florian"
}

config["SUDO"] = {
    "numberdigits": 6,
    "numbertries": 8,
    "playername": "Cheater",
    "cheets": "on"
}

with open("number_guessing.ini", "w") as f:
    config.write(f)