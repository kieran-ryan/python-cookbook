def url(service):
    return f"https://site.com/{service}"


urlpatterns = [*map(url, ["api", "home", "login"])]

if __name__ == "__main__":
    print(urlpatterns)
