# coding=utf-8
import rhasspy
'''from sense_hat import SenseHat'''


'''sense = SenseHat()'''

# Lance l'apprentissage du fichier sentences.ini. Commentez cette partie si vous souhaitez ne pas le lancer
print("Hello")
'''sense.show_letter("A")'''
print("Lancement de l'apprentissage.")
rhasspy.train_intent_files("/home/pi/sentences.txt")
print("Apprentissage termine.")
state = True
state2 = True
course_list = []
print('hi')
while state:

    '''sense.show_letter("T")'''
    # Introduction enoncee
    #rhasspy.text_to_speech("Enoncez votre phrase, s'il vous plait.")
    # Reception d'une commande vocale et affichage du resultat.
    intent = rhasspy.speech_to_intent()

    if intent["name"] == "Course":
        while state2:
            print("Commande course detectee. Quelle article voulez-vous ajouter dans la liste?")
            article = rhasspy.speech_to_intent()
            if article["name"] == "Arret":
                print("stop working")
                state2 = False
                print(course_list)
                #rhasspy.text_to_speech('Commande course arrete')
                print('Commande course arrete')
            elif article["name"] == "list":
                print(course_list)
                #rhasspy.text_to_speech(str(course_list))

            elif article['name'] == 'Delete':
                course_list.clear()
                print("Liste videe")

            elif article['name'] == 'Ajout':
                print(article['variables']['article'])
                print(article['variables']['qty'])
                print(article['variables']['article'])

                course_list.append((article['variables']['article'], article['variables']['qty']))





    # Enonce la commande vocale recue et les variables.
    rhasspy.text_to_speech("Vous avez lance la commande {} avec les parametres {}".format(intent["name"], intent["variables"]))

    # Affiche la commande vocale recue.
    '''sense.show_message("Commande : {}".format(intent["name"]), scroll_speed=0.07)'''
