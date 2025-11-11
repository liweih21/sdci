import requests

def get_status(url):
    response = requests.get(url)
    return response.status_code
