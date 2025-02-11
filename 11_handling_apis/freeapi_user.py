import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    res = requests.get(url)
    data = res.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        country = user_data["location"]["country"]
        
        return user_name, country
    else:
        raise Exception("Failed to fetch random user")



def main():
    try:
        user_name, country = fetch_random_user()
        print(f"User Name: {user_name}")
        print(f"Country: {country}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()