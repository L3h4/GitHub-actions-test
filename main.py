import os


def main():
    test = os.getenv('TEST')
    print(f"Hello {test=}")


if __name__ == "__main__":
    main()
