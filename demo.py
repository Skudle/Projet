# coding=utf-8
import rhasspy
from sense_hat import SenseHat
import random


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
code_secret = None
code_secret2 = None
lst = []

while state:

    sense.show_letter("T")
    # Introduction enoncee
    #rhasspy.text_to_speech("Enoncez votre phrase, s'il vous plait.")
    # Reception d'une commande vocale et affichage du resultat.
    intent = rhasspy.speech_to_intent()

    if intent["name"] == "Course":

        while state2:

            print("Commande course detectee.")
            article = rhasspy.speech_to_intent()
            if article["name"] == "Arret":
                print("stop working")
                state2 = False
                print(course_list)
                rhasspy.text_to_speech('Commande course arrete')
                print('Commande course arrete')
            elif article["name"] == "list":
                print(course_list)
                rhasspy.text_to_speech(str(course_list))

            elif article['name'] == 'Delete':
                course_list.clear()
                print("Liste videe")

            elif article['name'] == 'Ajout':
                print(article['variables']['article'])
                print(article['variables']['qty'])
                course_list.append((article['variables']['article'], article['variables']['qty']))

    elif intent["name"] == "Numero":
        print("Commande numéro détectée")
        choix = rhasspy.speech_to_intent()
        if code_secret is None:
            print("Voulez-vous encrypter ou decrypter un code?")
            if choix["name"] == "Encrypter":
                print("Veuillez entrer un numéro")
                code_secret = rhasspy.speech_to_intent()
                code_secret2 = random.choice(["vert", "rouge"])
                '''with open("codes.txt", 'w') as f:
                    f.write(code_secret2)'''
                lst.append(code_secret2)
                print(f"La clé est {code_secret2}")

        else:
            if choix["name"] == "Decrypter":
                print("Veuillez entrer la clé")
                inp = rhasspy.speech_to_intent()
                print("this is the inp")
                print(inp["raw_tokens"][0])
                #lst = []
                '''with open('codes.txt', 'r') as g:
                    for i in g.readlines():
                        lst.append(i.strip('\n'))'''
                if inp["raw_tokens"][0] in lst:
                    print("le if marche code secret")
                    print(">>> " + str(code_secret["raw_tokens"][0]) + " <<<")
                else:
                    print("error")

            elif choix["name"] == "Destruction":
                inp2 = rhasspy.speech_to_intent()
                code_secret = None
                print("Code secret supprimé")










    # Enonce la commande vocale recue et les variables.
    rhasspy.text_to_speech("Vous avez lance la commande {} avec les parametres {}".format(intent["name"], intent["variables"]))

    # Affiche la commande vocale recue.
    '''sense.show_message("Commande : {}".format(intent["name"]), scroll_speed=0.07)'''
