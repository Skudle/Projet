# coding=utf-8
import time

import rhasspy
from sense_hat import SenseHat
import crypto
import random


sense = SenseHat()

# Lance l'apprentissage du fichier sentences.ini. Commentez cette partie si vous souhaitez ne pas le lancer
sense.show_letter("A")
print("Lancement de l'apprentissage.")
rhasspy.train_intent_files("/home/pi/sentences.txt")
print("Apprentissage termine.")
state = True
state2 = True
course_list = []
code_secret = None
code_secret2 = None
lst = []

print("> Le programme est entrain de se charger. Merci de votre patience :p")
print("Starting...")
time.sleep(2)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
while state:
    state2 = True
    running = True
    sense.show_letter("T")
    # Introduction enoncee
    #rhasspy.text_to_speech("Enoncez votre phrase, s'il vous plait.")
    # Reception d'une commande vocale et affichage du resultat.
    print("> Bienvenue, voici les commandes disponibles: 'magasin', 'numéro'")
    intent = rhasspy.speech_to_intent()

    if intent["name"] == "Course":
        print("Commande course detectee.")
        while state2:
            print("> Voici les commandes disponibles: 'list', 'ajoute qql chose', 'Stop', 'supprime la liste'")
            article = rhasspy.speech_to_intent()
            if article["name"] == "Arret":
                state2 = False
                rhasspy.text_to_speech('Commande course arrete')
                print('Commande course arrete')

            elif article["name"] == "list":
                print(f"> Voici le contenu de la liste {course_list}")
                rhasspy.text_to_speech(str(course_list))

            elif article['name'] == 'Delete':
                course_list.clear()
                print("Liste vidée ")

            elif article['name'] == 'Ajout':
                print(f"{article['variables']['qty']} {article['variables']['article']} ajouté dans la liste de course")
                course_list.append((article['variables']['article'], article['variables']['qty']))

    elif intent["name"] == "Numero":
        running = True
        print("Commande numéro détectée")
        while running:
            print("> Voici les commandes disponibles: 'encrypter', 'decrypter', 'supprimer le code secret', 'fini' ")
            choix = rhasspy.speech_to_intent()
            if code_secret is None:
                if choix["name"] == "Encrypter":
                    print("> Veuillez entrer un numéro")
                    code_secret = rhasspy.speech_to_intent()
                    code_secret2 = random.choice(["vert", "rouge", "jaune", "noir", "blanc"])
                    encod = crypto.encode(code_secret2, str(code_secret["raw_tokens"][0]))
                    lst.append(code_secret2)
                    print("> Votre code secret a été enregistré!")
                    print(f"> La clé est {code_secret2}")

                elif choix["name"] == "Fini":
                    print("Commande numero arrete")
                    running = False

            else:
                if choix["name"] == "Decrypter":
                    print("> Veuillez entrer la clé ")
                    inp = rhasspy.speech_to_intent()
                    if inp["raw_tokens"][0] in lst:
                        decod = crypto.decode(code_secret2, encod)
                        print(">>> " + decod + " <<<")
                    else:
                        print("!!! Clé incorrecte !!!")

                elif choix["name"] == "Destruction":
                    code_secret = None
                    print("Code secret supprimé")

                elif choix["name"] == "Fini":
                    print("Commande numero arrete")
                    running = False










    # Enonce la commande vocale recue et les variables.
    rhasspy.text_to_speech("Vous avez lance la commande {} avec les parametres {}".format(intent["name"], intent["variables"]))

    # Affiche la commande vocale recue.
    '''sense.show_message("Commande : {}".format(intent["name"]), scroll_speed=0.07)'''
