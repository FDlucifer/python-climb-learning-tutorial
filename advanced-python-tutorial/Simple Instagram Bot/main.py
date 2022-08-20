# pip install instagrapi

import random
from instagrapi import Client

with open("credentials.txt", "r") as f:
    username, password = f.read().splitlines()

client = Client()
client.login(username, password)

hashtag = "programming"
comments = ["awesome", "great", "nice"]

medias = client.hashtag_medias_recent(hashtag, 20)

for i, media in enumerate(medias):
    client.media_like(media.id)
    print(f"liked post number {i+1} of hashtag {hashtag}")
    if i % 5 == 0:
        client.user_follow(media.user.pk)
        print(f"followed user {media.user.username}")
        client.media_comment(media.id, "awesome post")
        comment = random.choice(comments)
        print(f"commented {comment} under post number {i+1}")
