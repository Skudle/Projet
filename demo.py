import rhasspy
from sense_hat import SenseHat

sense = SenseHat()

# Lance l'apprentissage du fichier sentences.ini. Commentez cette partie si vous souhaitez ne pas le lancer
print("Hello")
sense.show_letter("A")
print("Lancement de l'apprentissage.")
rhasspy.train_intent_files("/home/pi/sentences.txt")
print("Apprentissage terminé.")
state = True
state2 = True
course_list = []

'''def encode(key, plain_text):
	"""
	Chiffre un texte en utilisant une clé de chiffrement.
	Les deux arguments sont fournis sous la forme d'une chaine de caractères.
	L'algorithme utilisé est le chiffrement de Vigenère.
	Attention : cette méthode est "craquée" depuis longtemps, mais elle illustre le fonctionnement d'un algorithme de chiffrement.

	:param (str) key: la clé symétrique
	:param (str) plain_text: le texte à chiffrer
	:return (str): le texte chiffré
	"""
	enc = []
	for i, e in enumerate(plain_text):
		key_c = key[i % len(key)]
		enc_c = chr((ord(e) + ord(key_c)) % 256)
		enc.append(enc_c)
	return "".join(enc)

def decode(key, cipher_text):
	"""
	Déchiffre le texte en utilisant la clé de déchiffrement.
	Les deux arguments sont fournis sous la forme d'une chaine de caractères.
	L'algorithme utilisé est le (dé)chiffrement de Vigenère.
	Attention : cette méthode est "craquée" depuis longtemps, mais elle illustre le fonctionnement d'un algorithme de (dé-)chiffrement.

	:param (str) key: la clé symétrique
	:param (str) cipher_text: le texte crypté
	:return (str): le texte décrypté
	"""
	dec = []
	for i, e in enumerate(cipher_text):
		key_c = key[i % len(key)]
		dec_c = chr((256 + ord(e) - ord(key_c)) % 256)
		dec.append(dec_c)
	return str("".join(dec))'''

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
    '''elif intent['name'] == 'Code':
        print("Commande code détecté")
        e_ou_d = rhasspy.speech_to_intent()
        if e_ou_d['name'] == "Encrypter":
            print("Quelle code voulez-vous soumettre")
            code = rhasspy.speech_to_intent()
            if code['name'] == 'encrypter':
                passwd = encode("m", code['variables']['code'])
        elif e_ou_d['name'] == "Decrypter":
            print("Quelle est le mot de passe?")
            input_ = rhasspy.speech_to_intent()
            if input_['name'] == 'Decrypter':
                print(passwd)'''





    # Enonce la commande vocale reçue et les variables.
    rhasspy.text_to_speech("Vous avez lancé la commande {} avec les paramètres {}".format(intent["name"], intent["variables"]))

    # Affiche la commande vocale reçue.
    sense.show_message("Commande : {}".format(intent["name"]), scroll_speed=0.07)
