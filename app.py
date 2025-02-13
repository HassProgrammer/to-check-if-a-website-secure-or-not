import requests
def website_secure_or_not(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.url.startswith("https://")
    except requests.exceptions.RequestException:
        return False
if __name__ == "__main__":
    website_url = input("Enter the website URL:\t")

    if website_secure_or_not(website_url):
        print(f"{website_url} is a secure website\nThank you!")
    else:
        print(f"{website_url} is not a secure website!\nSorry!")