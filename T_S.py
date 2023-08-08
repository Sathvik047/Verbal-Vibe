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

def select_voice(voices):
    print("Available voices:")
    for index, voice in enumerate(voices):
        print(f"{index+1}. {voice['name']}")
    voice_index = int(input("Enter the number corresponding to the desired voice: ")) - 1
    return voices[voice_index]['voice_id']

def generate_speech(api_key, text, voice_id, output_filename):
    conn = http.client.HTTPSConnection("api.elevenlabs.io")