import requests

def main():
    """Run time code"""

    # create resp, which is our request object
    resp = requests.get("https://api.magicthegathering.io/v1/sets")

    # display the methods available to our new object
    print( dir(resp) )

if __name__ == "__main__":
    main()
