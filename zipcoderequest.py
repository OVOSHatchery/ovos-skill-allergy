import requests


def get_zip_from_ip(ipaddress):
    url = "http://ip-api.com/json/" + ipaddress
    response = requests.get(url)
    data = response.json()
    zipcode = data['zip']
    return zipcode

def get_my_ip():
    ipaddress = requests.get('https://ident.me')
    return ipaddress.text