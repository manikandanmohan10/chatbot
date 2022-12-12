# import speech_recognition as sr
# import pyttsx3

# listener = sr.Recognizer()
# # engine = pyttsx3.init()
# msg = {
# "greeting": "hi, How are you",
# }

# # def talk(text):
# #     engine.say(text)
# #     engine.runAndWait()
# try:
#     with sr.Microphone() as source:
#         print("listining.........")
#         voice = listener.listen(source)
#         cmd = listener.recognize_google(voice)

#         if (cmd=='hello'):
#             print(msg.get('greeting'))
#             # talk(msg.get('greeting'))
#         else:
#             print(cmd)
#             # talk(cmd)

# except:
#     pass
    
import speech_recognition as sr

listener = sr.Recognizer()

def get_text(command='Thanks'):
    try:
        with sr.Microphone() as source:
            print('Listening..............')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
            
    except Exception as e:
        command = str(e)
    
    return command

# while True:
get_text()


# Import the necessary libraries
# import os
# import pocketsphinx

# # Set the path to the PocketSphinx data directory
# data_path = "/path/to/pocketsphinx/data"

# # Create a decoder object
# decoder = pocketsphinx.Decoder(hmm=os.path.join(data_path, "en-us"), lm=os.path.join(data_path, "en-us.lm.bin"), dict=os.path.join(data_path, "cmudict-en-us.dict"))

# # Start the decoder
# decoder.start_utt()

# # Define a function to listen for speech
# def listen_for_speech():
#     # Prompt the user to speak
#     print("Say something...")

#     # Listen for speech using the microphone
#     audio = r.listen(mic)

#     # Try to recognize the speech
#     try:
#         # Process the audio data using PocketSphinx
#         decoder.process_raw(audio.get_raw_data(), False, False)

#         # Get the recognized text
#         recognized_text = decoder.hyp().hypstr

#         # Print the recognized text
#         print("I think you said: " + recognized_text)
#     except:
#         # Handle errors
#         print("Sorry, I couldn't understand what you said.")

# # Start listening for speech
# listen_for_speech()


# import speech_recognition as sr
# listener = sr.Recognizer()

# while True:
#     with sr.Microphone() as source:
#         print("listining.........")
#         listener.adjust_for_ambient_noise(source,duration=1)
#         voice = listener.listen(source)
#         cmd = listener.recognize_google(voice)
#         print(cmd)
#     if cmd == "end":
#         break