from instagrapi import Client

username = input('Username: ')
password = input('Password: ')
client = Client()
client.login(username, password)

hashtag = input("heashtag: ")
amount = int(input("amount: "))
post = client.hashtag_medias_recent(hashtag, amount)

for i in range(amount):
    print("Post " + str(i+i))
    client.media_like(post[i].id)
    print("Liked Post")
    client.user_follow(post[i].user.pk)
    print("Followed User" + post[i].user.username)

    




