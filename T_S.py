import json
import http.client

def get_api_key():
    api_key = input("Please enter your API key: ")
    with open("api_key.txt", "w") as file:
        file.write(api_key)

def load_api_key():
    try:
        with open("api_key.txt", "r") as file:
            api_key = file.read().strip()
        return api_key
    except FileNotFoundError:
        return None
    
   
def get_text():
    return input("Enter the text you want to convert to speech: ")


def get_output_filename():
    return input("Enter the desired output file name (without extension): ")