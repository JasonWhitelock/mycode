#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
from pprint import pprint

x= 3
URL= f"https://opentdb.com/api.php?amount={3}&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    pprint(data)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print('Question: '+data["results"][0]["question"])
    print('Answer: '+data["results"][0]["correct_answer"])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print('Question: '+data["results"][1]["question"])
    print('Answer: '+data["results"][1]["correct_answer"])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print('Question: '+data["results"][2]["question"])
    print('Answer: '+data["results"][2]["correct_answer"])

if __name__ == "__main__":
    main()
