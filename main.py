import os


def main():
    test = os.getenv('TEST')
    print(f"Hello {test=}")
    print(f"Len of test {len(test) if test else 'None'}")


if __name__ == "__main__":
    main()
