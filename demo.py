import rhasspy
from sense_hat import SenseHat

sense = SenseHat()

# Lance l'apprentissage du fichier sentences.ini. Commentez cette partie si vous souhaitez ne pas le lancer
print("Hello")
sense.show_letter("A")
print("Lancement de l'apprentissage.")
rhasspy.train_intent_files("/home/pi/sentences.txt")
print("Apprentissage termine.")
state = True
state2 = True
course_list = []
print("hi")

while state:

    sense.show_letter("T")
    # Introduction énoncée
    rhasspy.text_to_speech("Énoncez votre phrase, s'il vous plait.")
    # Réception d'une commande vocale et affichage du résultat.
    intent = rhasspy.speech_to_intent()

    if intent["name"] == "Course":
        while state2:
            print("Commande course detectée. Quelle article voulez-vous ajouter dans la liste?")
            article = rhasspy.speech_to_intent()
            if article["name"] == "Arret":
                print("stop working")
                state2 = False
                print(course_list)
                rhasspy.text_to_speech('Commande course arreté')
                print('Commande course arreté')
            elif article["name"] == "list":
                print(course_list)
                rhasspy.text_to_speech(str(course_list))

            elif article['name'] == 'Delete':
                course_list.clear()
                print("Liste vidée")

            elif article['name'] == 'Ajout':
                print(article['variables']['article'])
                print(article['variables']['qty'])
                print(article['variables']['article'])

                course_list.append((article['variables']['article'], article['variables']['qty']))





    # Enonce la commande vocale reçue et les variables.
    rhasspy.text_to_speech("Vous avez lancé la commande {} avec les paramètres {}".format(intent["name"], intent["variables"]))

    # Affiche la commande vocale reçue.
    sense.show_message("Commande : {}".format(intent["name"]), scroll_speed=0.07)
