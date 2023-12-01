import requests


def request_mapping(url):
    def fixer(func):
        def wrapper(self, *args, **kwargs):
            params = func(self, *args, **kwargs)
            response = requests.get(self.host + url, params=params)
            return response.json()

        return wrapper

    return fixer
