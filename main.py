import os


def main():
    print(f"Hello {os.getenv('TEST')}")


if __name__ == "__main__":
    main()
