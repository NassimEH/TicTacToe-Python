import tkinter

def check_win(clicked_row, clicked_col):
    # Victoire horizontale
    count = 0
    for i in range(3):
        current_button = buttons[i][clicked_row]
        if current_button['text'] == current_player:
            count += 1 
        if count == 3:
            print("Victoire horizontale !")
            winner()
            
    # Victoire verticale
    count = 0
    for i in range(3):
        current_button = buttons[clicked_col][i]
        if current_button['text'] == current_player:
            count += 1 
        if count == 3:
            print("Victoire verticale !")   
            winner()
            
    # Victoire diagonale
    count = 0
    for i in range(3):
        current_button = buttons[i][i]
        if current_button['text'] == current_player:
            count += 1 
        if count == 3:
            print("Victoire diagonale !")
            winner()
            
    # Victoire diagonale inverse
    count = 0
    for i in range(3):
        current_button = buttons[2-i][i]
        if current_button['text'] == current_player:
            count += 1 
        if count == 3:
            print("Victoire diagonale inverse !")
            winner()
            
# Fonction pour dessiner la grille de TicTacToe
def draw_grid():
    for column in range(3):
        boutons_dans_col = []
        for row in range(3):
            # Création d'un bouton avec une commande pour placer un symbole
            bouton = tkinter.Button(root, font=("Arial", 50), width=5, height=3, command=lambda r=row, c=column: place_symbol(r, c))
            bouton.grid(row=row, column=column)
            boutons_dans_col.append(bouton)
        buttons.append(boutons_dans_col)

def winner():
    print("Le joueur", current_player, "a gagné la partie !")

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else: 
        current_player = "X"

# Fonction pour placer un symbole sur le bouton cliqué
def place_symbol(row, column):
    print("Clic")
    # Récupération du bouton cliqué à partir de la liste des boutons
    bouton_clique = buttons[column][row]
    # Configuration du texte du bouton pour afficher "X"
    clicked_button = buttons[column][row]
    if clicked_button['text'] == "":
        clicked_button.config(text=current_player)
    
    check_win(row, column)
    switch_player()

# Variables
buttons = []
current_player = "X"
win = False

# Fenêtre principale
root = tkinter.Tk()
root.title("TicTacToe")
root.minsize(600, 600)

# Dessiner la grille de boutons
draw_grid()

# Lancement de la boucle principale de la fenêtre
root.mainloop()
