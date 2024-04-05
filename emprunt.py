from tabulate import tabulate
import datetime
Livres = [
    {"idL": 1, "Titre": "The Clean Coder", "Pages": "256", "Auteur": "Robert Martin", "Disponible": True},
    {"idL": 2, "Titre": "Introduction to Algorithms", "Pages": "1292", "Auteur": "Thomas H Cormen",
     "Disponible": False},
    {"idL": 3, "Titre": "Structure and Interpretation of Computer Programs", "Pages": "657", "Auteur": "Harold Abelson",
     "Disponible": True},
    {"idL": 4, "Titre": "Code Complete", "Pages": "960", "Auteur": "Steve McConnell", "Disponible": False},
    {"idL": 5, "Titre": "Design Patterns", "Pages": "416", "Auteur": "Erich Gamma", "Disponible": True},
    {"idL": 6, "Titre": "The Pragmatic Programmer", "Pages": "352", "Auteur": "Andrew Hunt", "Disponible": True},
    {"idL": 7, "Titre": "Refactoring", "Pages": "448", "Auteur": "Martin Fowler", "Disponible": True},
]
Adherents = [
    {"idA": 1, "Nom": "Muslih Elmandjra", "Tel": "0673637721", "Email": "muslihelmandjra@gmail.com"},
    {"idA": 2, "Nom": "Asil Tawil", "Tel": "0662953814", "Email": "asiltawil@gmail.com"},
    {"idA": 3, "Nom": "Samir Bikri", "Tel": "0642918065", "Email": "samirbikri@gmail.com"},
    {"idA": 4, "Nom": "Moosa Ibn Qasim", "Tel": "0673698401", "Email": "moosaibnqasim@gmail.com"},
]
Emprunts = [
    {"idL": 2, "idA": 1, "Titre-Livre": "Introduction to Algorithms", "Date_Emprunt": "1/11/2023", "Status": "S"},
    {"idL": 2, "idA": 1, "Titre-Livre": "Introduction to Algorithms", "Date_Emprunt": "30/11/2023", "Status": "E"},
    {"idL": 4, "idA": 2, "Titre-Livre": "Code Complete", "Date_Emprunt": "13/09/2023", "Status": "S"},
]


# ============Fonction pour afficher les tables============
def affiche(L):
    data = []
    temp = []
    heading = []
    for key, value in L[0].items():
        heading.append(key)
    for i in L:
        for key, value in i.items():
            temp.append(value)
        data.append(temp.copy())
        temp.clear()
    print(tabulate(data, headers=heading, tablefmt="rounded_outline"))


# ======================================================MENU======================================================
def menu():
    while True:
        print(" " * 70, "╭──────────────────────────╮")
        print(" " * 70, "│           MENU           │")
        print(" " * 70, "├──────────────────────────┤")
        print(" " * 70, "│       1 - Livre          │")
        print(" " * 70, "│       2 - Adherent       │")
        print(" " * 70, "│       3 - Emprunt        │")
        print(" " * 70, "│       4 - Quitter        │")
        print(" " * 70, "╰──────────────────────────╯\n")
        while True:
            x = input("choisir votre choix dans le menu precendent: ")
            x = x.strip()
            if x == "1" or x == "2" or x == "3" or x == "4":
                x = int(x)
                break
            print("─" * 100)
            print("Choix invalide, tapez une choix valide")
            print("─" * 100)
        if x == 1:
            livre()
        elif x == 2:
            adherent()
        elif x == 3:
            emprunt()
        elif x == 4:
            bye()
            exit()


# ======================================================LIVRE======================================================

def livre():
    while True:
        print(" " * 70, "╭──────────────────────────╮")
        print(" " * 70, "│           LIVRE          │")
        print(" " * 70, "├──────────────────────────┤")
        print(" " * 70, "│       1 - Lister         │")
        print(" " * 70, "│       2 - Ajouter        │")
        print(" " * 70, "│       3 - Recherche      │")
        print(" " * 70, "│       4 - Quitter        │")
        print(" " * 70, "╰──────────────────────────╯\n")
        while True:
            n = input("choisir votre choix dans le menu precendent: ")
            n = n.strip()
            if n == "1" or n == "2" or n == "3" or n == "4":
                n = int(n)
                break
            print("─" * 100)
            print("Choix invalide, tapez une choix valide")
            print("─" * 100)
        # ============Afficher la liste des livres============
        if n == 1:
            print("ٍٍٍٍٍٍVoici la liste des livres :")
            affiche(Livres)
        # ============Ajouter un nouveau livre============
        elif n == 2:
            s = '[§@_!#$%^&*()<>?/\\|}{~^]'
            while True:
                c = 0
                titre = input("Entrez le titre de livre: ")
                for i in titre:
                    if i in s:
                        c += 1
                if c > 0:
                    print("─" * 100)
                    print("Le titre doit être composée de brûlés ou de chiffres")
                    print("─" * 100)
                elif c == 0 and len(titre) > 1:
                    break
            while True:
                pages = input("Entrez le nombre de pages: ")
                pages = pages.strip()
                if pages.isdecimal():
                    pages = int(pages)
                    if pages > 2:
                        break
                print("─" * 100)
                print("Choix invalide, Entrez un nombre décimal")
                print("─" * 100)
            s = '[§@_!#$%^&*()<>?/\\|}{~^]1234567890-°+='
            while True:
                c = 0
                auteur = input("Entrez l'auteur du livre: ")
                for i in auteur:
                    if i in s:
                        c += 1
                if c > 0 or len(auteur) < 2:
                    print("─" * 100)
                    print("Faux nom, Entrez un nom correct")
                    print("─" * 100)
                elif c == 0 and len(auteur) > 1:
                    break
            new = {"idL": len(Livres) + 1,
                   "Titre": titre,
                   "Pages": pages,
                   "Auteur": auteur,
                   "Disponible": True}
            print(new)
            Livres.append(new.copy())
            print("─" * 100)
            print("ٍٍٍٍٍٍVoici la liste des livres :")
            affiche(Livres)
            print("─" * 100)
            print("Le livre a été ajouté avec succès")
            print("─" * 100)
        # ============Rechercher un livre============
        elif n == 3:
            r = input("Entrez le titre ou l'auteur du livre que vous recherchez: ")
            livres_recherches = list(filter(lambda x: r.lower() in x['Titre'].lower() or r.lower() in x['Auteur'].lower(), Livres))
            if(len(livres_recherches) > 0):
                affiche(livres_recherches)
            else:
                print("─" * 100)
                print("Aucun livre avec ce titre ou auteur")
                print("─" * 100)
        # ============Quitter============
        elif n == 4:
            break


# ======================================================ADHERENT======================================================

def adherent():
    while True:
        print(" " * 70, "╭──────────────────────────╮")
        print(" " * 70, "│          ADHERENT        │")
        print(" " * 70, "├──────────────────────────┤")
        print(" " * 70, "│       1 - Lister         │")
        print(" " * 70, "│       2 - Ajouter        │")
        print(" " * 70, "│       3 - Recherche      │")
        print(" " * 70, "│       4 - Quitter        │")
        print(" " * 70, "╰──────────────────────────╯\n")
        while True:
            x = input("choisir votre choix dans le menu precendent: ")
            x = x.strip()
            if x == "1" or x == "2" or x == "3" or x == "4":
                x = int(x)
                break
            print("─" * 100)
            print("Choix invalide, tapez une choix valide")
            print("─" * 100)
        # ============Afficher la liste des adherents============
        if x == 1:
            print("ٍٍٍٍٍٍVoici la liste des adherents :")
            affiche(Adherents)
        # ============Ajouter un nouveau adherent============
        elif x == 2:
            s = '[§@_!#$%^&*()<>?/\\|}{~^]1234567890-°+='
            while True:
                c = 0
                nom = input("Entrez le nom d'adherent: ")
                for i in nom:
                    if i in s:
                        c += 1
                if c > 0 or len(nom) < 2:
                    print("─" * 100)
                    print("nom invalide, Entrez un nom correct")
                    print("─" * 100)
                elif c == 0 and len(nom) > 1:
                    break
            while True:
                tel = input("Entrez le numéro de téléphone: ")
                tel = tel.strip()
                if tel.isdecimal() and len(tel) == 10 and (
                        tel.startswith("06") or tel.startswith("07") or tel.startswith("05")):
                    break
                print("─" * 100)
                print("Vous devez entrer un numéro de téléphone à 10 chiffres commençant par 06, 07 ou 05")
                print("─" * 100)
            while True:
                email = input("Entrez l'adresse e-mail: ")
                email = email.strip()
                if "@" in email and "." in email and len(email) > 2 and not email.startswith("@") and not email.startswith(".") and not email.endswith("@") and not email.endswith("."):
                    break
                print("─" * 100)
                print("E-mail incorrect, entrez un e-mail valide")
                print("─" * 100)

            new = {"idA": len(Adherents) + 1,
                   "Nom": nom,
                   "Tel": tel,
                   "Email": email}
            Adherents.append(new.copy())
            print("ٍٍٍٍٍٍVoici la liste des adherents :")
            affiche(Adherents)
            print("─" * 100)
            print("L'adherent a été ajouté avec succès")
            print("─" * 100)
        # ============Rechercher une adherent============
        elif x == 3:
            r = input("Entrez le nom ou telephone d'adherent: ")
            adherents_recherches = list(
                filter(lambda x: r.lower() in x['Nom'].lower() or r in x['Tel'], Adherents))
            if (len(adherents_recherches) > 0):
                affiche(adherents_recherches)
            else:
                print("─" * 100)
                print("Aucun adherent avec ce nom ou telephone")
                print("─" * 100)
        # ============Quitter============
        elif x == 4:
            break


# ======================================================EMPRUNT======================================================

def emprunt():
    global cont, idl, ida, bk, date
    while True:
        print(" " * 70, "╭──────────────────────────╮")
        print(" " * 70, "│          EMPRUNT         │")
        print(" " * 70, "├──────────────────────────┤")
        print(" " * 70, "│       1 - Lister         │")
        print(" " * 70, "│       2 - Ajouter        │")
        print(" " * 70, "│       3 - Recherche      │")
        print(" " * 70, "│       4 - Quitter        │")
        print(" " * 70, "╰──────────────────────────╯\n")
        while True:
            n = input("choisir votre choix dans le menu precendent: ")
            n = n.strip()
            if n == "1" or n == "2" or n == "3" or n == "4":
                n = int(n)
                break
            print("─" * 100)
            print("Choix invalide, tapez une choix valide")
            print("─" * 100)
        # ============Afficher la liste des emprunts============
        if n == 1:
            print("ٍٍٍٍٍٍVoici la liste des emprunts :")
            affiche(Emprunts)
        # ============Ajouter un nouveau emprunt============
        elif n == 2:
            status = input("Si vous voulez prendre un livre écrivez \"S\", en cas de retour d'un livre écrivez \"E\": ")
            if status.upper() == "S":
                print("─" * 100)
                date_format = '%d/%m/%Y'
                while True:
                    try:
                        date = input("saisir la date de reception Sous la forme suivante JJ/MM/AAAA:")
                        date_reception = datetime.datetime.strptime(date, date_format)
                        if date_reception >= datetime.datetime.now():
                            break
                        print("─" * 100)
                        print("la date saisie est incorrecte,Entrez une date valide.")
                        print("─" * 100)
                    except:
                        continue
                while True:
                    print("─" * 100)
                    print("ٍٍٍٍٍٍVoici la liste des adherents :")
                    affiche(Adherents)
                    condition = input("Êtes-vous inscrit? Écrivez \"oui\" ou \"non\": ")
                    if condition.lower() == "oui":
                        print("ٍٍٍٍٍٍVoici la liste des adherents :")
                        affiche(Adherents)
                        cont = True
                        while cont:
                            while True:
                                ida = input("Veuillez taper votre id qui apparaît dans la liste ci-dessus: ")
                                if ida.isdecimal():
                                    ida = int(ida)
                                    break
                                print("─" * 100)
                                print("l'id doit être composé uniquement de chiffres")
                                print("─" * 100)
                            for i in Adherents:
                                if i['idA'] == ida:
                                    cont = False
                            if cont:
                                print("─" * 100)
                                print("l'id saisi est introuvable, Veuiller saisi une id correcte")
                                print("─" * 100)
                            else:
                                break
                        break
                    elif condition.lower() == "non":
                        s = '[§@_!#$%^&*()<>?/\\|}{~^]1234567890-°+='
                        while True:
                            c = 0
                            nom = input("Entrez votre nom: ")
                            for i in nom:
                                if i in s:
                                    c += 1
                            if c > 0 or len(nom) < 2:
                                print("─" * 100)
                                print("Faux nom, Entrez un nom correct")
                                print("─" * 100)
                            elif c == 0 and len(nom) > 1:
                                break
                        while True:
                            tel = input("Entrez votre numéro de téléphone: ")
                            tel = tel.strip()
                            if tel.isdecimal() and len(tel) == 10 and (
                                    tel.startswith("06") or tel.startswith("07") or tel.startswith(
                                "06") or tel.startswith(
                                "05")):
                                break
                            print("─" * 100)
                            print("Vous devez entrer un numéro de téléphone à 10 chiffres commençant par 06, 07 ou 05")
                            print("─" * 100)
                        while True:
                            email = input("Entrez votre adresse e-mail: ")
                            email = email.strip()
                            if "@" in email and "." in email and len(email) > 2:
                                break
                            print("─" * 100)
                            print("E-mail incorrect, entrez un e-mail valide")
                            print("─" * 100)
                        new = {"idA": len(Adherents) + 1,
                               "Nom": nom,
                               "Tel": tel,
                               "Email": email}
                        Adherents.append(new.copy())
                        print("ٍٍٍٍٍٍVoici la liste des adherents :")
                        affiche(Adherents)
                        print("─" * 100)
                        print("L'adherent a été ajouté avec succès")
                        print("─" * 100)
                        ida = len(Adherents)
                        break
                    else:
                        print("─" * 100)
                        print("choix invalide, tapez une choix valide.")
                        print("─" * 100)
                print("ٍٍٍٍٍٍVoici la liste des livres disponibles :")
                data = []
                temp = []
                heading = []
                for key, value in Livres[0].items():
                    heading.append(key)
                for i in Livres:
                    if i["Disponible"]:
                        for key, value in i.items():
                            temp.append(value)
                        data.append(temp.copy())
                    temp.clear()
                print(tabulate(data, headers=heading, tablefmt="rounded_outline"))
                cont = True
                while cont:
                    while True:
                        idl = input(
                            "Veuillez saisir l'id du livre que vous souhaitez emprunter qui apparaît dans la liste ci-dessus: ")
                        if idl.isdecimal():
                            idl = int(idl)
                            break
                        print("─" * 100)
                        print("l'id doit être composé uniquement de chiffres")
                        print("─" * 100)
                    for i in data:
                        if i[0] == idl:
                            cont = False
                    if cont:
                        print("─" * 100)
                        print("l'id saisi est introuvable, Veuiller saisi une id correcte")
                        print("─" * 100)
                    else:
                        break
                for i in Livres:
                    if i["idL"] == idl:
                        bk = i["Titre"]
                        i["Disponible"] = False
                emprunt_temp = {"idL": int(idl), "idA": int(ida), "Titre-Livre": str(bk), "Date_Emprunt": str(date),
                                "Status": "S"}
                Emprunts.append(emprunt_temp)
                print("─" * 100)
                print("L'opération a réussi")
                print("─" * 100)
                affiche(Emprunts)
            elif status.upper() == "E":
                print("─" * 100)
                date_format = '%d/%m/%Y'
                while True:
                    try:
                        date = input("saisir la date de reception Sous la forme suivante JJ/MM/AAAA:")
                        date_reception = datetime.datetime.strptime(date, date_format)
                        if date_reception >= datetime.datetime.now():
                            break
                        print("─" * 100)
                        print("la date saisie est incorrecte,Entrez une date valide.")
                        print("─" * 100)
                    except:
                        continue
                print("─" * 100)
                print("ٍٍٍٍٍٍVoici la liste des adherents :")
                affiche(Adherents)
                cont = True
                while cont:
                    while True:
                        ida = input("Veuillez taper votre id qui apparaît dans la liste ci-dessus: ")
                        if ida.isdecimal():
                            ida = int(ida)
                            break
                        print("─" * 100)
                        print("l'id doit être composé uniquement de chiffres")
                        print("─" * 100)

                    for i in Adherents:
                        if i['idA'] == ida:
                            cont = False
                    if cont:
                        print("─" * 100)
                        print("l'id saisi est introuvable, Veuiller saisi une id correcte")
                        print("─" * 100)
                    else:
                        break
                c = 0
                for i in Emprunts:
                    if i['idA'] == ida:
                        if i['Status'] == "S":
                            c += 1
                        elif i['Status'] == "E":
                            c -= 1
                if c <= 0:
                    print("─" * 100)
                    print("L'adherent que vous avez choisi n'a pas emprunté de livre")
                    print("─" * 100)
                    emprunt()
                print("Voici la liste des livres qui ont été empruntés par l'adherent sélectionné :")
                data = []
                temp = []
                heading = []
                for key, value in Livres[0].items():
                    heading.append(key)
                for i in Livres:
                    if i["Disponible"] is False:
                        for j in Emprunts:
                            if j['idA'] == ida and i['idL'] == j['idL']:
                                for key, value in i.items():
                                    temp.append(value)
                        if temp:
                            data.append(temp.copy())
                    temp.clear()
                print(tabulate(data, headers=heading, tablefmt="rounded_outline"))
                cont = True
                while cont:
                    while True:
                        idl = input("Écrivez l'id du livre que vous souhaitez retourner: ")
                        if idl.isdecimal():
                            idl = int(idl)
                            break
                        print("─" * 100)
                        print("l'id doit être composé uniquement de chiffres")
                        print("─" * 100)
                    for i in data:
                        try:
                            if i[0] == idl:
                                cont = False
                        except:
                            continue
                    if cont:
                        print("─" * 100)
                        print("l'id saisi est introuvable, Veuiller saisi une id correcte")
                        print("─" * 100)
                    else:
                        break
                for i in Livres:
                    if i["idL"] == idl:
                        bk = i["Titre"]
                        i["Disponible"] = True
                emprunt_temp = {"idL": int(idl), "idA": int(ida), "Titre-Livre": str(bk), "Date_Emprunt": str(date),
                                "Status": "E"}
                Emprunts.append(emprunt_temp)
                print("─" * 100)
                print("L'opération a réussi")
                print("─" * 100)
                print("voici la liste des emprunts:")
                print("*s= sortie")
                print("*e= entrée")
                affiche(Emprunts)
            else:
                print("─" * 100)
                print("choix invalide")
                print("─" * 100)
        # ============Rechercher un emprunt============
        elif n == 3:

            r = input("Entrez le titre du livre que vous recherchez: ")
            emprunts_recherches = list(
                filter(lambda x: r.lower() in x['Titre-Livre'].lower(), Emprunts))
            if (len(emprunts_recherches) > 0):
                affiche(emprunts_recherches)
            else:
                print("─" * 100)
                print("Il n'y a aucun emprunt avec ce titre de livre")
                print("─" * 100)
        # ============Quitter============
        elif n == 4:
            break


# ============Function pour afficher le titre ============
def title():
    print(
        "====     ██████╗ ███████╗███████╗████████╗██╗ ██████╗ ███╗   ██╗    ██████╗ ███████╗███████╗    ███████╗███╗   ███╗██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗     ====")
    print(
        "====    ██╔════╝ ██╔════╝██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║    ██╔══██╗██╔════╝██╔════╝    ██╔════╝████╗ ████║██╔══██╗██╔══██╗██║   ██║████╗  ██║╚══██╔══╝     ====")
    print(
        "====    ██║  ███╗█████╗  ███████╗   ██║   ██║██║   ██║██╔██╗ ██║    ██║  ██║█████╗  ███████╗    █████╗  ██╔████╔██║██████╔╝██████╔╝██║   ██║██╔██╗ ██║   ██║        ====")
    print(
        "====    ██║   ██║██╔══╝  ╚════██║   ██║   ██║██║   ██║██║╚██╗██║    ██║  ██║██╔══╝  ╚════██║    ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██╔══██╗██║   ██║██║╚██╗██║   ██║        ====")
    print(
        "====    ╚██████╔╝███████╗███████║   ██║   ██║╚██████╔╝██║ ╚████║    ██████╔╝███████╗███████║    ███████╗██║ ╚═╝ ██║██║     ██║  ██║╚██████╔╝██║ ╚████║   ██║        ====")
    print(
        "====     ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═════╝ ╚══════╝╚══════╝    ╚══════╝╚═╝     ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝        ====")
    print(
        "=======                                         ██████╗ ███████╗███████╗    ██╗     ██╗██╗   ██╗██████╗ ███████╗███████╗                                         =======")
    print(
        "=======================================         ██╔══██╗██╔════╝██╔════╝    ██║     ██║██║   ██║██╔══██╗██╔════╝██╔════╝         =======================================")
    print(
        "=======================================         ██║  ██║█████╗  ███████╗    ██║     ██║██║   ██║██████╔╝█████╗  ███████╗         =======================================")
    print(
        "=======================================         ██║  ██║██╔══╝  ╚════██║    ██║     ██║╚██╗ ██╔╝██╔══██╗██╔══╝  ╚════██║         =======================================")
    print(
        "=======================================         ██████╔╝███████╗███████║    ███████╗██║ ╚████╔╝ ██║  ██║███████╗███████║         =======================================")
    print(
        "=======================================         ╚═════╝ ╚══════╝╚══════╝    ╚══════╝╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝╚══════╝         =======================================")

def creation():
    print(" " * 57, "    ______________________   ______________________")
    print(" " * 57, ".-/|                      \\ /                      |\\-.")
    print(" " * 57, "||||                       |                       ||||")
    print(" " * 57, "||||                       |                       ||||")
    print(" " * 57, "||||                       |                       ||||")
    print(" " * 57, "||||                       |        ABDELLAH       ||||")
    print(" " * 57, "||||       CE PROJET       |        KHOUDEN        ||||")
    print(" " * 57, "||||    A ETE CREE PAR:    |           &           ||||")
    print(" " * 57, "||||                       |       ABDERRAHIM      ||||")
    print(" " * 57, "||||                       |        BENSAID        ||||")
    print(" " * 57, "||||                       |                       ||||")
    print(" " * 57, "||||                       |                       ||||")
    print(" " * 57, "||||                       |                       ||||")
    print(" " * 57, "||||                       |                       ||||")
    print(" " * 57, "||||______________________ | ______________________||||")
    print(" " * 57, "||/=======================\\|/=======================\\||")
    print(" " * 57, "`------------------------~___~-----------------------''")

def bye():
    print(" " * 64, "             ▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄   ")
    print(" " * 64, "             █▒▒░░░░░░░░░▒▒█   ")
    print(" " * 64, "              █░░█░░░░░█░░█    ")
    print(" " * 64, "           ▄▄  █░░░▀█▀░░░█  ▄▄ ")
    print(" " * 64, "          █░░█ ▀▄░░░░░░░▄▀ █░░█")
    print(" " * 64, "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
    print(" " * 64, "█░░                                    ░░█")
    print(" " * 64, "█░░             AU REVOIR              ░░█")
    print(" " * 64, "█░░                                    ░░█")
    print(" " * 64, "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")

creation()
title()
menu()
