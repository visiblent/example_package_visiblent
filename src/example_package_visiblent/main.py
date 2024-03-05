import requests


def make_get_request(url):
    return requests.get(url)


if __name__ == '__main__':
    make_get_request("https://www.google.com/")
