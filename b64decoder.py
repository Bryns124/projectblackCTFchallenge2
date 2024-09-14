import base64
import requests

content = requests.get("https://projectblack.io/ctf/challenge2.txt").text

with open("CTFchallenge.zip", "wb") as file:
    file.write(base64.b64decode(content))