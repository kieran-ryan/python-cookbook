def clip(num, minimum, maximum):
    return max(minimum, min(num, maximum))


if __name__ == "__main__":
    print(clip(12, minimum=5, maximum=10))  # 10
    print(clip(-1, minimum=5, maximum=10))  # 5
