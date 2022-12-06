from sense_hat import SenseHat
import rhasspy
import time
s = SenseHat()
course_list = []
state = True
[Name]
Mon nom est {user_name}

[Course]
Course

[Arret]
Stop




rhasspy.text_to_speech("Bienvenue, quelle est votre nom?")
user_name = speech_to_intent()
rhasspy.text_to_speech(f"Bonjour {user_name}")
command = speech_to_intent()

if command == "Course":
    while state:
        article = speech_to_intent()
        if article == "Arret":
            State = False
        else:
            course_list.append(article)
