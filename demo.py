# coding=utf-8
import time

import rhasspy
from sense_hat import SenseHat
import crypto



'''fichier = "/home/pi/sound.zip"
sounds = "mixkit-ambulance-siren-uk-1640"
sense = SenseHat()

pygame.mixer.init()
speaker = 0.8
pygame.mixer.music.set_volume(speaker)

red = (255, 0, 0)
blue = (0, 0, 255)

def police_red():
    R = red
    redlight = [
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    ]
    return redlight

def police_blue():
    B = blue
    bluelight = [
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    ]
    return bluelight'''
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
hash_mdp = None
lst = []
data_lst = []
joystick_on = False
j_ou_v = True


def joystick():
    print("Augmenter: droite, Diminuer: gauche, Sauvegarder: haut, Quitter: bas")
    number = 0
    total_number = ""
    num = []
    run = True
    while run:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction == 'right':
                    number += 1
                    sense.show_message(str(number))
                elif event.direction == 'left':
                    number -= 1
                    sense.show_message(str(number))
                elif event.direction == 'up':
                    total_number += str(number)
                    print(total_number)
                    number = 0
                else:
                    print("Fini: Droite, Ajouter un autre numéro: Gauche")
                    run2 = True
                    while run2:
                        for event2 in sense.stick.get_events():
                            if event2.action == 'pressed':
                                if event2.direction == 'right':
                                    num.append(total_number)
                                    return num
                                elif event2.direction == 'left':
                                    num.append(total_number)
                                    total_number = ""
                                    print("Augmenter: droite, Diminuer: gauche, Sauvegarder: haut, Quitter: bas")
                                    run2 = False

print("> Le programme est entrain de se charger. Merci de votre patience :p")
print("Starting...")
time.sleep(1)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
while state:
    state2 = True
    running = True
    sense.show_letter("T")
    # Introduction enoncee
    #rhasspy.text_to_speech("Enoncez votre phrase, s'il vous plait.")
    # Reception d'une commande vocale et affichage du resultat.
    if j_ou_v:
        print("> Le programme possède 2 modes: Vocale et Joystick. Quelle mode souhaitez-vous utiliser?")
        while True:
            mode = rhasspy.speech_to_intent()
            if mode["name"] == "Joystick":
                print("Mode Joystick activé")
                joystick_on = True
                break
            elif mode["name"] == "Vocale":
                print("Mode Vocale activé")
                joystick_on = False
                break
            else:
                print("Erreur, veuillez recommencer.")

    while not joystick_on:
        print("> Bienvenue dans le mode vocal, voici les commandes disponibles: 'magasin', 'numéro', 'Mode Joystick'")
        intent = rhasspy.speech_to_intent()
        if intent["name"] == "Course":
            print("Commande course detectee.")
            state2 = True
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
            running1 = True
            print("Commande numéro détectée")
            while running1:
                if hash_mdp is None:
                    print("> Le système a detecté qu'aucun mot de passe n'a été défini.")
                    set_up_pwd = True
                    while set_up_pwd:
                        print("> Quelle mot de passe souhaitez-vous entré? ")
                        created_pwd = rhasspy.speech_to_intent()
                        print(f"> Votre mot de passe est: {created_pwd['raw_tokens'][0]}")
                        hash_mdp = crypto.hashing(str(created_pwd["raw_tokens"][0]))
                        del created_pwd
                        set_up_pwd = False
                else:
                    print("> Voici les commandes disponibles: 'encrypter', 'decrypter', 'delete code', 'changer', 'terminer' ")
                    choix = rhasspy.speech_to_intent()
                    if choix["name"] == "Encrypter":
                        print("> Veuillez entrer un numéro que vous souhaitez sauvegarder sur l'appareil")
                        code_secret = rhasspy.speech_to_intent()
                        encod = crypto.encode("pomme", str(code_secret["raw_tokens"][0]))
                        data_lst.append(encod)
                        del (code_secret)
                        print("> Votre code a été enregistré!")

                    elif choix["name"] == "Decrypter":
                        print("> Veuillez entrer votre mot de passe ")
                        inp = rhasspy.speech_to_intent()
                        if crypto.hashing(inp["raw_tokens"][0]) == hash_mdp:
                            print("Mot de passe correcte")
                            print_lst = []
                            for i in range(len(data_lst)):
                                print_lst.append(crypto.decode("pomme", data_lst[i]))
                            print(f">>> {print_lst} <<<")
                            print_lst.clear()

                    elif choix["name"] == "Fini":
                        print("Commande numero arrete")
                        running1 = False

                    elif choix["name"] == "Destruction":
                        data_lst.clear()
                        print("Vos numéro ont été supprimé")

                    elif choix["name"] == "Changer":
                        print("> Entrez votre mot de passe actuelle")
                        current_pwd = rhasspy.speech_to_intent()
                        if crypto.hashing(current_pwd["raw_tokens"][0]) == hash_mdp:
                            print("Mot de passe correcte")
                            del current_pwd
                            del hash_mdp
                            time.sleep(1)
                            print("> Veuillez entrer un nouveau mot de passe")
                            now_pwd = rhasspy.speech_to_intent()
                            print(f"Votre nouveau mot de passe est: {now_pwd['raw_tokens'][0]}")
                            hash_mdp = crypto.hashing(now_pwd["raw_tokens"][0])
                            del now_pwd
                            print("Nouveau mot de passe défini")

        elif intent["name"] == "Joystick":
            print("Mode Joystick activé")
            joystick_on = True
            j_ou_v = False
        else:
            print("Commande invalide. Veuillez recommencer.")

    print("> Mode Joystick: Magasin: Gauche, Numéro: Droite, Mode Vocale: Haut")
    while joystick_on:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction == 'right':
                    running1 = True
                    print("Commande numéro détectée")
                    while running1:
                        if hash_mdp is None:
                            print("> Le système a detecté qu'aucun mot de passe n'a été défini.")
                            set_up_pwd = True
                            while set_up_pwd:
                                print("> Quelle mot de passe souhaitez-vous entrer? ")
                                created_pwd = joystick()
                                print(f"> Votre mot de passe est: {created_pwd[0]}")
                                hash_mdp = crypto.hashing(str(created_pwd[0]))
                                del created_pwd
                                set_up_pwd = False
                        else:
                            print("> Encrypter: 1, Decrypter: 2, Delete Code: 3, Changer mdp: 4, Quitter: 5")
                            count = joystick()
                            if count[0] == "1":
                                # Encrypter
                                print("> Veuillez entrer un numéro que vous souhaitez sauvegarder sur l'appareil")
                                code_secret = joystick()
                                for i in range(len(code_secret)):
                                    print(f"> Votre code {code_secret[i]} a été enregistré et encrypté!")
                                    encod = crypto.encode("pomme", str(code_secret[i]))
                                    data_lst.append(encod)
                                del code_secret

                            elif count[0] == "2":
                                # Decrypter
                                print("> Veuillez entrer votre mot de passe pour confirmer votre identité")
                                inp = joystick()
                                if crypto.hashing(str(inp[0])) == hash_mdp:
                                    print("Mot de passe correcte")
                                    print_lst = []
                                    for i in range(len(data_lst)):
                                        print_lst.append(crypto.decode("pomme", data_lst[i]))
                                    print(f">>> {print_lst} <<<")
                                    print_lst.clear()

                            elif count[0] == "5":
                                # Quitter
                                print("Commande numero arrete")
                                print("> Magasin: Gauche, Numéro: Droite, Mode Vocale: Haut")
                                running1 = False

                            elif count[0] == "3":
                                # Delete Code
                                print("> Veuillez entrer votre mot de passe pour confirmer votre identité")
                                inp2 = joystick()
                                if crypto.hashing(str(inp2[0])) == hash_mdp:
                                    print("Mot de passe correcte")
                                    data_lst.clear()
                                    print("Vos numéro ont été supprimé")

                            elif count[0] == "4":
                                # Changer mdp
                                print("> Entrez votre mot de passe actuelle")
                                current_pwd = joystick()
                                if crypto.hashing(str(current_pwd[0])) == hash_mdp:
                                    print("Mot de passe correcte")
                                    del current_pwd
                                    del hash_mdp
                                    time.sleep(1)
                                    print("> Veuillez entrer un nouveau mot de passe")
                                    now_pwd = joystick()
                                    print(f"Votre nouveau mot de passe est: {now_pwd[0]}")
                                    hash_mdp = crypto.hashing(str(now_pwd[0]))
                                    del now_pwd
                                    print("Nouveau mot de passe définie")
                            else:
                                # Si on se trompe de num
                                print("Commande invalide. Veuillez réessayer.")

                elif event.direction == "up":
                    print("Mode Vocale activé")
                    joystick_on = False
                    j_ou_v = False
                elif event.direction == 'left':
                    print("Commande course detectee.")
                    state2 = True
                    while state2:
                        print("> 'list', 'ajoute qql chose', 'Stop', 'supprime la liste'")
                        article = rhasspy.speech_to_intent()
                        if article["name"] == "Arret":
                            state2 = False
                            rhasspy.text_to_speech('Commande course arrete')
                            print('Commande course arrete')
                            print("> Magasin: Gauche, Numéro: Droite")

                        elif article["name"] == "list":
                            print(f"> Voici le contenu de la liste {course_list}")
                            rhasspy.text_to_speech(str(course_list))

                        elif article['name'] == 'Delete':
                            course_list.clear()
                            print("Liste vidée ")

                        elif article['name'] == 'Ajout':
                            print(
                                f"{article['variables']['qty']} {article['variables']['article']} ajouté dans la liste de course")
                            course_list.append((article['variables']['article'], article['variables']['qty']))
                else:
                    print("Commande invalide. Veuillez recommencer.")


    '''elif intent['name'] == "Police":
        images = [police_red, police_blue]
        count = 0
        for sound in sounds:
            pygame.mixer.music.load(fichier + sounds)
            pygame.mixer.music.play()
            while True:
                sense.set_pixels(images[count % len(images)]())
                time.sleep(.75)
                count += 1'''












    # Enonce la commande vocale recue et les variables.
    #rhasspy.text_to_speech("Vous avez lance la commande {} avec les parametres {}".format(intent["name"], intent["variables"]))

    # Affiche la commande vocale recue.
    '''sense.show_message("Commande : {}".format(intent["name"]), scroll_speed=0.07)'''
