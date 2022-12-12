import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder

import colorama 
colorama.init()
from colorama import Fore, Style, Back

import random
import pickle
import time
from audio_to_text import get_text

with open("content.json") as file:
    data = json.load(file)


# def chat(inp=None):
while True:
    # load trained model
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20
    
    # while True:
    print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
    inp = input()
    # inp = get_text()
    # inp = inp
    if inp.lower() == "quit":
        # break
        pass

    result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                            truncating='post', maxlen=max_len))
    tag = lbl_encoder.inverse_transform([np.argmax(result)])

    for i in data['intents']:
        if i['tag'] == tag:
            response = np.random.choice(i['responses'])
            print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL , np.random.choice(i['responses']))
        # print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL,random.choice(responses))

    # return response
    print(Fore.YELLOW + "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)
    # time.sleep(5)
# chat()