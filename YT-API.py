import sys, json, requests

vidCode = input('\nVideo Code Here: ')

url = requests.get("https://returnyoutubedislikeapi.com/votes?videoId="+vidCode)
text = url.text

data = json.loads(text)

print("\n-----------------------------")
print("YouTube Dislike API Script by: KorOwOzin")
print("-----------------------------\n")

if "id" in data:
  print(f'Video URL: youtube.com/watch?v={vidCode}')
  print('Date Created: '+ data['dateCreated'])
  print('Likes: '+ (str(data['likes'])))
  print('Dislikes: '+ (str(data['dislikes'])))
  print('Rating: '+ (str(data['rating'])))
  print('ViewCount: '+ (str(data['viewCount'])))
  print('Is Video Deleted?: '+ (str(data['deleted']))+'\n')
else:
  print("The video could not be found.\n")
