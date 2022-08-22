import sys, json, requests

vidCode = input('\nVideo Code Here: ')

url = requests.get("https://returnyoutubedislikeapi.com/votes?videoId="+vidCode)
text = url.text

data = json.loads(text)

dateCreated = data['dateCreated']
likes = data['likes']
dislikes = data['dislikes']
rating = data['rating']
viewCount = data['viewCount']
deleted = data['deleted']

print("\n-----------------------------")
print("YouTube Dislike API Script by: KorOwOzin")
print("-----------------------------\n")

if "id" in data:
  print(f'Video URL: youtube.com/watch?v={vidCode}')
  print(f'Date Created: {dateCreated}')
  print(f'Likes: {likes}')
  print(f'Dislikes: {dislikes}')
  print(f'Rating: {rating}')
  print(f'ViewCount: {viewCount}')
  print(f'Is Video Deleted?: {deleted}\n')
else:
  print("The video could not be found.\n")