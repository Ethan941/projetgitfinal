



# Liste des todos
todos = []

# Fonction pour créer un todo
def creer_todo():
    titre = input("Entrez le titre du todo : ")
    todos.append({"titre": titre, "statut": "À faire"})
    print(f"Todo '{titre}' créé avec succès avec le statut 'À faire'.")

# Fonction pour lister les todos
def lister_todos():
    print("\nListe des todos :")
    if not todos:
        print("Aucun todo disponible.")
        return
    for index, todo in enumerate(todos):
        print(f"{index + 1}. {todo['titre']} - Statut : {todo['statut']}")

# Fonction pour modifier le statut d'un todo
def modifier_statut_todo():
    if not todos:
        print("Aucun todo disponible pour modification.")
        return

    lister_todos()
    try:
        choix = int(input("Choisissez le numéro du todo à modifier : ")) - 1
        if choix < 0 or choix >= len(todos):
            print("Numéro invalide.")
            return
        
        # Logique pour changer le statut
        todo = todos[choix]
        if todo["statut"] == "À fair":
            todo["statut"] = "Fait"
            print(f"Le statut du todo '{todo['titre']}' est passé à 'Fait'.")
        elif todo["statut"] == "Fait":
            # Logique demandée : toujours repasser le statut à "À faire"
            todo["statut"] = "À faire"
            print(f"Le statut du todo '{todo['titre']}' est repassé à 'À faire'.")
        else:
            print("Statut inconnu, aucune modification effectuée.")
    except ValueError:
        print("Entrée invalide, veuillez entrer un numéro.")

# Fonction pour supprimer un todo
def supprimer_todo():
    if not todos:
        print("Aucun todo disponible pour suppression.")
        return

    lister_todos()
    try:
        choix = int(input("Choisissez le numéro du todo à supprimer : ")) - 1
        if choix < 0 or choix >= len(todos):
            print("Numéro invalide.")
            return

        todo_supprime = todos.pop(choix)
        print(f"Le todo '{todo_supprime['titre']}' a été supprimé avec succès.")
    except ValueError:
        print("Entrée invalide, veuillez entrer un numéro.")

# Menu principal
choix = ''
while choix != 'q':
    # Affichage des choix
    print("\n==== Menu principal ====")
    print("1: Créer un todo")
    print("2: Lister les todos")
    print("3: Modifier le statut d'un todo")
    print("4: Supprimer un todo")
    print("q: Quitter")
    print("========================")
    # Actions suivant le choix
    choix = input("=> Choix : ")
    match choix:
        case '1':
            creer_todo()
        case '2':
            lister_todos()
        case '3':
            modifier_statut_todo()
        case '4':
            supprimer_todo()
        case 'q':
            print("Au revoir !")
        case _:
            print("Choix invalide, veuillez réessayer.")

