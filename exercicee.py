# Liste pour stocker les todos sous forme de dictionnaires
todos = []

# Fonction pour lister les todos avec leur statut
def lister_todos():
    if not todos:  # Vérifie si la liste est vide
        print("Aucune tâche à afficher.")
    else:
        print("\n=== Liste des tâches ===")
        for i, todo in enumerate(todos, 1):
            print(f"{i}. {todo['titre']} - Statut : {todo['statut']}")  # Affiche le titre et le statut

# Fonction pour créer un todo
def creer_todo():
    titre = input("Entrez le titre de la tâche : ")
    todo = {"titre": titre, "statut": "À faire"}  # Ajout automatique du statut "À faire"
    todos.append(todo)  # Ajout du todo dans la liste
    print(f"Tâche '{titre}' créée avec le statut '{todo['statut']}'.")

# Fonction pour vérifier et inverser le statut d'un todo
def verifier_et_inverser_statut():
    if not todos:  # Vérifie si la liste est vide
        print("Aucune tâche à modifier.")
        return

    # Lister les todos pour permettre le choix
    lister_todos()
    try:
        choix = int(input("Entrez le numéro de la tâche à modifier : "))
        if 1 <= choix <= len(todos):  # Vérifie si le choix est valide
            todo = todos[choix - 1]  # Récupère le todo sélectionné
            # Vérifie et inverse le statut
            if todo['statut'] == "À faire":
                todo['statut'] = "Fait"  # Passe le statut à "Fait"
                print(f"Le statut de la tâche '{todo['titre']}' a été changé en 'Fait'.")
            elif todo['statut'] == "Fait":
                todo['statut'] = "À faire"  # Passe le statut à "À faire"
                print(f"Le statut de la tâche '{todo['titre']}' a été changé en 'À faire'.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")

# Fonction pour supprimer un todo
def supprimer_todo():
    print('Fonctionnalité "supprimer un todo" à venir')

# Menu principal
choix = ''
while choix != 'q':
    # Affichage des choix
    print('\n==== Menu principal ====')
    print('1: Lister les todos')
    print('2: Créer un todo')
    print('3: Vérifier et changer le statut d\'un todo')
    print('4: Supprimer un todo')
    print('q: quitter')
    print('========================')

    # Actions suivant le choix
    choix = input('=> Choix : ')
    match choix:
        case '1':
            lister_todos()
        case '2':
            creer_todo()
        case '3':
            verifier_et_inverser_statut()
        case '4':
            supprimer_todo()
        case 'q':
            print('Au revoir')
        case _:
            print('Choix invalide')


