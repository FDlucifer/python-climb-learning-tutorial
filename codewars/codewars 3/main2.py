# The Hashtag Generator

def generate_hashtag(s):
    result = "#" + s.title().replace(" ", "")
    if result == "#":
        return False
    if len(result) > 140:
        return False
    return result