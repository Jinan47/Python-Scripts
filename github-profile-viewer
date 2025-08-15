import requests

def get_github_user(user):
    url = f"https://api.github.com/users/{user}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    user = input("Enter GitHub username: ")
    user_info = get_github_user(user)
    if user_info:
        print(f"Username: {user_info['login']}")
        print(f"Name: {user_info['name']}")
        print(f"Public Repos: {user_info['public_repos']}")
    else:
        print("User not found.")
