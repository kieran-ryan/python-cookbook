BASE_URL = "https://site.com/"
ENDPOINTS = ["api", "home", "login"]


def url(service):
    return f"{BASE_URL}{service}"


urls_map = list(map(url, ENDPOINTS))
urls_lambda = list(map(lambda endpoint: BASE_URL + endpoint, ENDPOINTS))
urls_comprehension = [BASE_URL + endpoint for endpoint in ENDPOINTS]

if __name__ == "__main__":
    print(urls_map)
    print(urls_lambda)
    print(urls_comprehension)

    """
    [
      'https://site.com/api',
      'https://site.com/home',
      'https://site.com/login',
    ]
    """
