from pydantic import BaseModel
from typing import List, Dict, Optional, Union


# class Player(BaseModel):
#     name: str
#     deposit: int
#     items: List[Dict[str, int]]
#     friends: List[str] = 'Electronic'
#
# s1mple = Player(name='Tolik', items=[{'burger':1}], deposit = 3400)
# print(s1mple)
#
# class Coment(BaseModel):
#     user: Union[str, int]
#     comment: str
#     likes: int
# coments = Coment(user='Tolik', comment='qwerty', likes=12312)
# print(coments)

# class User(BaseModel):
#     name: str
#     followers: int
#     posts: int
# user2 = User(name = 'Ttt', followers = 1, posts = 2)
# print(user2)
# class Sbor(BaseModel):
#     user: User
#     comment: str
#     likes: int
# sbor = Sbor(user=user2, comment = 'qwerty', likes =23)
# print(sbor)

class User(BaseModel):
    username: str
    mail: str
    language: str
class Artist(BaseModel):
    user: User
    artist_name: str
    artist_followers: int = 0
class Song(BaseModel):
    artist: Artist
    song_name: str
    date_of_publish: str
class Playlist(BaseModel):
    user: Union[list, User]
    songs: Song
    likes: int = 0

user1 = User(username = 'Qwe', mail = 'qwer@req.com', language="ru")
user2 = User(username = 'Q2e', mail = 'q123@req.com', language="en")
artist1 = Artist(user=user1, artist_name = 'qwe', artist_followers = 123)
song1 = Song(artist=artist1, song_name = 'Sss', date_of_publish = '2015-2')
playlist1 = Playlist(user=[user1, user2], songs=song1, likes=23)

print(playlist1)