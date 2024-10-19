# main file
import urllib.request
import json
import os

# get username
username = input("Enter Scratch username: ")

while True:
  # get api wrapping utility
  utility = input("Utility [user-projects-wrapper, follower-wrapping-utility, exit]: ")
  
  if utility == "user-projects-wrapper":
    # url
    url = f"https://api.scratch.mit.edu/users/{username}/projects/"
    
    # fetch daaataaaa
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    
    # display info
    for project in data:
        title = project.get('title', 'N/A')
        description = project.get('description', 'No description available')
        loves = project.get('stats', {}).get('loves', 0)
        favorites = project.get('stats', {}).get('favorites', 0)
        views = project.get('stats', {}).get('views', 0)
        remixes = project.get('remix', {}).get('count', 0)
        
        print("=" * 50)
        print("PROJECT NAME")
        print("-" * 50)
        print(f"{title}")
        
        print("\nDESCRIPTION")
        print("-" * 50)
        print(f"{description}")
        
        print("\nSTATS")
        print("-" * 50)
        print(f"Hearts: {loves}")
        print(f"Stars: {favorites}")
        print(f"Views: {views}")
        print(f"Remixes: {remixes}")
        print("=" * 50)
        print("\n")
  
  elif utility == "follower-wrapping-utility":
    # url
    url = f"https://api.scratch.mit.edu/users/{username}/followers/"
    # get data
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    # display info
    print("=" * 50)
    print(f"Followers for {username}")
    print("=" * 50)
    
    for follower in data:
        follower_name = follower.get('username', 'Unknown')
        
        print("FOLLOWER USERNAME")
        print("-" * 50)
        print(f"{follower_name}")
        
        # If you want to fetch and display more follower details, add additional fields here
        print("=" * 50)
        print("\n")
    
  elif utility == "exit":
    os.exit()
    
  else:
    print("thats not an option right now!")
