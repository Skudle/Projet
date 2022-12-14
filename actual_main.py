import time

import rhasspy
from sense_hat import SenseHat
import crypto
import files_function
from playsound import playsound


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
    return bluelight


def talk(text):
    print(f"\n> {str(text)}")
    rhasspy.text_to_speech(str(text))

def talk2(text):
    print(f"> {str(text)}")
    rhasspy.text_to_speech(str(text))

def welcome(value):
    if value == False:
        return talk("Bienvenue dans le mode vocal, voici les commandes disponibles: 'magasin', 'numéro', 'Police', 'Mode Joystick'")
    else:
        return talk("Les commandes: 'magasin', 'numéro', 'Police', 'Mode Joystick'")

sense = SenseHat()

# Lance l'apprentissage du fichier sentences.ini. Commentez cette partie si vous souhaitez ne pas le lancer
sense.show_letter("A")
talk("Lancement de l'apprentissage.")
rhasspy.train_intent_files("/home/pi/sentences.txt")
talk("Apprentissage termine.")

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
welcom_ = False
hash_mdp_bool = files_function.code_existence('code_hash.txt')
def joystick():
    talk2("Augmenter: droite, Diminuer: gauche, Sauvegarder: haut, Quitter: bas")
    number = 0
    total_number = ""
    num = []
    run = True
    while run:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction == 'right':
                    if number == 9:
                        number = 0
                    else:
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
                    talk("Fini: Droite, Ajouter un autre numéro: Gauche")
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
                                    talk2("Augmenter: droite, Diminuer: gauche, Sauvegarder: haut, Quitter: bas")
                                    run2 = False
                sense.show_letter(str(number))

talk("Le programme est entrain de se charger. Merci de votre patience ")
print("Starting...")
talk("Demarrage en cours")
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
        talk(" Je possède 2 modes: Vocale ou Joystick. Quelle mode souhaitez-vous utiliser?")
        while True:
            mode = rhasspy.speech_to_intent()
            if mode["name"] == "Joystick":
                talk("Mode Joystick activé")
                sense.show_message('Joystick')
                joystick_on = True
                break
            elif mode["name"] == "Vocale":
                talk("Mode Vocale activé")
                sense.show_message('Vocale')
                joystick_on = False
                break
            else:
                talk("Erreur, recommencer.")

    while not joystick_on:
        welcome(welcom_)
        intent = rhasspy.speech_to_intent()
        if intent["name"] == "Course":
            talk("Commande course detectee.")

            state2 = True
            while state2:
                talk("Les commandes sont: 'list', 'ajoute qql chose', 'Stop', 'supprime la liste'")
                article = rhasspy.speech_to_intent()
                if article["name"] == "Arret":
                    state2 = False
                    talk('Commande course arrete')

                elif article["name"] == "list":
                    talk(f"Voici le contenu de la liste {course_list}")
                    rhasspy.text_to_speech(str(course_list))

                elif article['name'] == 'Delete':
                    course_list.clear()
                    talk("Liste vidée")
                
                elif article['name'] == 'Ajout':
                    talk("Quelle quantité d'article voulez-vous ajouter dans la liste?")
                    run3 = True
                    total_quantity = ""
                    while run3:
                        quantity = rhasspy.speech_to_intent()
                        total_quantity += str(quantity['raw_tokens'][0])
                        talk("Voulez-vous ajouter un autre chiffre??")
                        choix = rhasspy.speech_to_intent()
                        if choix["name"] == "Non":
                            talk("Quelle article voulez-vous ajouter dans la liste?")
                            item = rhasspy.speech_to_intent()
                            course_list.append((total_quantity, item['raw_tokens'][0]))
                            total_quantity = ""
                            run3 = False
                        elif choix["name"] == "Oui":
                            talk("Dites un chiffre entre zéro et neuf")
                '''elif article['name'] == 'Ajout':
                    talk(f"{article['variables']['qty']} {article['variables']['article']} ajouté dans la liste de course")
                    course_list.append((article['variables']['article'], article['variables']['qty']))'''

        elif intent["name"] == "Numero":
            running1 = True
            talk("Commande numéro détectée")
            while running1:
                if hash_mdp is None:
                    talk("Le système a detecté qu'aucun mot de passe n'a été défini.")
                    set_up_pwd = True
                    while set_up_pwd:
                        talk("Quelle mot de passe souhaitez-vous entré? ")
                        created_pwd = rhasspy.speech_to_intent()
                        talk(f"Votre mot de pass est: {created_pwd['raw_tokens'][0]}")
                        hash_mdp = crypto.hashing(str(created_pwd["raw_tokens"][0]))
                        del created_pwd
                        set_up_pwd = False
                else:
                    talk("Voici les commandes disponibles: 'encrypter', 'decrypter', 'delete code', 'changer', 'terminer' ")
                    choix = rhasspy.speech_to_intent()
                    if choix["name"] == "Encrypter":
                        talk("Veuillez entrer un numéro que vous souhaitez sauvegarder sur l'appareil")
                        code_secret = rhasspy.speech_to_intent()
                        encod = crypto.encode("pomme", str(code_secret["raw_tokens"][0]))
                        data_lst.append(encod)
                        del code_secret
                        talk("Votre code a été enregistré!")

                    elif choix["name"] == "Decrypter":
                        talk("Veuillez entrer votre mot de pass ")
                        inp = rhasspy.speech_to_intent()
                        if crypto.hashing(inp["raw_tokens"][0]) == hash_mdp:
                            talk("Mot de passe correcte")
                            print_lst = []
                            for i in range(len(data_lst)):
                                print_lst.append(crypto.decode("pomme", data_lst[i]))
                            talk2(f"{print_lst}")
                            print_lst.clear()
                        else:
                            talk("Mauvais mot de passe")

                    elif choix["name"] == "Fini":
                        talk("Commande numero arrete")
                        running1 = False

                    elif choix["name"] == "Destruction": 
                        data_lst.clear()
                        talk("Vos numéro ont été supprimé")

                    elif choix["name"] == "Changer":
                        talk("Entrez votre mot de pass actuelle")
                        current_pwd = rhasspy.speech_to_intent()
                        if crypto.hashing(current_pwd["raw_tokens"][0]) == hash_mdp:
                            talk("Mot de passe correcte")
                            del current_pwd
                            del hash_mdp
                            time.sleep(1)
                            talk("Veuillez entrer un nouveau mot de passe")
                            now_pwd = rhasspy.speech_to_intent()
                            talk(f"Votre nouveau mot de passe est: {now_pwd['raw_tokens'][0]}")
                            hash_mdp = crypto.hashing(now_pwd["raw_tokens"][0])
                            del now_pwd
                            talk("Nouveau mot de passe défini")
        
        elif intent['name'] == "Police":
            images = [police_red, police_blue]
            playsound('/home/pi/police-siren-21498.mp3') 
            count = 0
            while True:
                sense.set_pixels(images[count % len(images)]())
                time.sleep(.75)
                count += 1
        elif intent["name"] == "Joystick":
            talk("Mode Joystick activé")
            joystick_on = True
            j_ou_v = False
        else:
            talk("Commande invalide. Recommencer.")
        welcom_ = True
    talk("Mode Joystick: Magasin: Gauche, Numéro: Droite, Mode Vocale: Haut")


    while joystick_on:
        for event in sense.stick.get_events():
            if event.action == 'pressed':
                if event.direction == 'right':
                    running1 = True
                    talk("Commande numéro détectée")
                    while running1:
                        if hash_mdp_bool is False:
                            talk("Le système a detecté qu'aucun mot de passe n'a été défini.")
                            set_up_pwd = True
                            while set_up_pwd:
                                files_function.erase_all('code_hash.txt')
                                talk("Quelle mot de passe souhaitez-vous entrer? ")
                                sense.show_letter("0")
                                created_pwd = joystick()
                                talk(f"Votre mot de pass est: {created_pwd[0]}")
                                hash_mdp = crypto.hashing(str(created_pwd[0]))
                                files_function.write_in_file('code_hash.txt',[hash_mdp])
                                del created_pwd
                                del hash_mdp
                                set_up_pwd = False
                            hash_mdp_bool = True
                        else:
                            talk("Encrypter: 1, Decrypter: 2, Delete Numbers: 3, Changer mdp: 4, Quitter: 5")
                            count = joystick()
                            if count[0] == "1":
                                # Encrypter
                                talk("Veuillez entrer un numéro que vous souhaitez sauvegarder sur l'appareil")
                                code_secret = joystick()
                                for i in range(len(code_secret)):
                                    talk(f"Votre code {code_secret[i]} a été enregistré et encrypté!")
                                    encod = crypto.encode("pomme", str(code_secret[i]))
                                    data_lst.append(encod)
                                del code_secret

                            elif count[0] == "2":
                                # Decrypter
                                talk("Veuillez entrer votre mot de pass pour confirmer votre identité")
                                inp = joystick()
                                hash_mdp1 = files_function.read_file("code_hash.txt")
                                if type(hash_mdp1) == list:
                                    if crypto.hashing(str(inp[0])) == hash_mdp1[0]:
                                        talk("Mot de passe correcte")
                                        print_lst = []
                                        for i in range(len(data_lst)):
                                            print_lst.append(crypto.decode("pomme", data_lst[i]))
                                        for nmb in print_lst:
                                            print(f">>> {nmb} <<<")
                                            rhasspy.text_to_speech(nmb)
                                        print_lst.clear()
                                        del hash_mdp1
                                else:
                                    talk("Vous devez Encrypter au début")

                            elif count[0] == "5":
                                # Quitter
                                talk("Commande numero arrete")
                                talk("Magasin: Gauche, Numéro: Droite, Mode Vocale: Haut")
                                running1 = False

                            elif count[0] == "3":
                                # Delete Code
                                talk("Veuillez entrer votre mot de pass pour confirmer votre identité")
                                inp2 = joystick()
                                hash_mdp1 = files_function.read_file("code_hash.txt")
                                if type(hash_mdp1) == list:
                                    if crypto.hashing(str(inp2[0])) == hash_mdp1[0]:
                                        talk("Mot de passe correcte")
                                        data_lst.clear()
                                        talk("Vos numéro ont été supprimé")
                                        del hash_mdp1
                                else: talk("Vous devez Encrypter au début")

                            elif count[0] == "4":
                                # Changer mdp
                                talk("Entrez votre mot de pass actuelle")
                                current_pwd = joystick()
                                hash_mdp1 = files_function.read_file("code_hash.txt")
                                if type(hash_mdp1) == list:
                                    if crypto.hashing(str(current_pwd[0])) == hash_mdp1[0]:
                                        talk("Mot de passe correcte")
                                        del current_pwd
                                        del hash_mdp
                                        time.sleep(1)
                                        talk("Veuillez entrer un nouveau mot de passe")
                                        now_pwd = joystick()
                                        talk(f"Votre nouveau mot de passe est: {now_pwd[0]}")
                                        hash_mdp = crypto.hashing(str(now_pwd[0]))
                                        files_function.erase_all("code_hash.txt")
                                        files_function.write_in_file("code_hash.txt",[hash_mdp])
                                        del now_pwd
                                        del hash_mdp1
                                        talk("Nouveau mot de passe définie")
                                else: talk("Vous devez Encrypter au début")
                            else:
                                # Si on se trompe de num
                                talk("Commande invalide. Réessayer.")

                elif event.direction == "up":
                    talk("Mode Vocale activé")
                    sense.show_message("Vocale")
                    joystick_on = False
                    j_ou_v = False
                elif event.direction == 'left':
                    talk("Commande course detectee.")
                    print("Commande course detectee.")
                    state2 = True
                    while state2:
                        talk('list, ajoute qql chose, Stop, supprime la liste')
                        print("> 'list', 'ajoute qql chose', 'Stop', 'supprime la liste'")
                        article = rhasspy.speech_to_intent()
                        if article["name"] == "Arret":
                            state2 = False
                            talk('Commande course arrete')
                            print('Commande course arrete')
                            talk("Magasin: Gauche, Numéro: Droite")
                            print("> Magasin: Gauche, Numéro: Droite")

                        elif article["name"] == "list":
                            talk("Voici le contenu de la liste")
                            print("> Voici le contenu de la liste")
                            for a in course_list:
                                talk(str(a))

                        elif article['name'] == 'Delete':
                            course_list.clear()
                            talk("Liste vidée ")
                            print("Liste vidée ")

                        elif article['name'] == 'Ajout':
                            talk(f"{article['variables']['qty']} {article['variables']['article']} ajouté dans la liste de course")
                            print(f"{article['variables']['qty']} {article['variables']['article']} ajouté dans la liste de course")
                            course_list.append((article['variables']['article'], article['variables']['qty']))
                else:
                    talk("Commande invalide. Recommencer.")








    # Enonce la commande vocale recue et les variables.
    #rhasspy.text_to_speech("Vous avez lance la commande {} avec les parametres {}".format(intent["name"], intent["variables"]))

    # Affiche la commande vocale recue.
'''sense.show_message("Commande : {}".format(intent["name"]), scroll_speed=0.07)'''