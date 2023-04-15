def url(service):
    return f"https://site.com/{service}"


urlpatterns = list(map(url, ["api", "home", "login"]))

if __name__ == "__main__":
    print(urlpatterns)

    """
    [
      'https://site.com/api',
      'https://site.com/home',
      'https://site.com/login',
    ]
    """
