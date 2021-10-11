from Soccer.classes.linkedList import LinkedList
import json


# Instantiating a blank linked list
athleteList = LinkedList()

# Reading data file and defining that encoding characters
file_opened = open('data/soccer_list.json', encoding='utf-8')
data = json.load(file_opened)

# Scrolling through JSON records to include players in the list
for register in data:
    athlete_name = register['Atleta']['nome']
    athlete_club = register['clube_nome']
    role = register['posicao']
    athleteList.insert_on_init(athlete_name, athlete_club, role)

# Showing others functions that was implemented in Soccer class
athleteList.remove_from_init()
athleteList.remove_from_init()

# Removing some athletes
athleteList.remove(3)

# Inserting athlete at position 6
athleteList.insert(6, 'João Kirshnov', 'CSKA', 'Goleiro')

# Inserting athlete at position 15
athleteList.insert(15, 'Marta Vieira da Silva', 'Orlando Pride', 'Atacante')
athleteList.remove(7)

# Removing a random athlete
athleteList.remove_random_register()
athleteList.remove_random_register()
athleteList.remove_random_register()
athleteList.remove_random_register()

# Showing all elements of linked list
athleteList.show()

# This function show name of element at position.
# If entered position is not valid, that show a message
# explain this error.
athleteList.item_at(10)
athleteList.item_at(7)
athleteList.item_at(3)
athleteList.item_at(150)
athleteList.item_at(350)
athleteList.item_at(2005)

