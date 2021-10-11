from Soccer.classes.athlete import Athlete
import random


class LinkedList:

    def __init__(self):
        self._init = None
        self._size = 0

    @property
    def init(self):
        return self._init

    @property
    def size(self):
        return self._size

    # Scrolls through the entire linked list displaying element by element
    def show(self):
        current_athlete = self.init
        for i in range(0, self.size):
            print("Name:", current_athlete.name + ',', "Team:", current_athlete.team, "Role:", current_athlete.role)
            current_athlete = current_athlete.next

    # Create a new element at first position of list
    def insert_on_init(self, name, team, role):
        athlete = Athlete(name, team, role)
        athlete.next = self._init
        self._init = athlete
        self._size += 1

    # Helps insert elements in specific positions
    def insert(self, position, name, team, role):
        if position == 0:
            self.insert_on_init(name, team, role)
            return
        previous_athlete = self._athlete(position - 1)
        athlete = Athlete(name, team, role)
        athlete.next = previous_athlete.next
        previous_athlete.next = athlete
        self._size += 1

    def _athlete(self, position):
        self.validate_position(position)
        current_athlete = self.init
        for i in range(0, position):
            current_athlete = current_athlete.next
        return current_athlete

    # Help determines if a position is valid. This is
    # used to various functions
    def validate_position(self, position):
        if 0 <= position < self.size:
            return True
        raise IndexError(
            "Invalid position {}".format(position))

    # Remove the first element at athlete linked list
    def remove_from_init(self):
        removed = self._init
        self._init = self._init.next
        removed.next = None
        self._size -= 1
        return removed

    # Removes a element at parameterized position
    def remove(self, position):
        if position == 0:
            return self.remove_from_init()
        previous_athlete = self._athlete(position - 1)
        removed = previous_athlete.next
        previous_athlete.next = removed.next
        removed.next = None
        self._size -= 1
        return removed

    # This method return a athlete at parameter position
    def item_at(self, position):
        if position <= (self._size - 1):
            print(
                "Athlete name at position", position, "is:", self._athlete(position).name,
                "Role is: ", self._athlete(position).role,
                "Team is: ", self._athlete(position).team,
            )
        else:
            print("The position entered does not exist, you can't see this register")

    # This method remove a random athlete
    def remove_random_register(self):
        number = random.randint(0, (self._size - 1))
        removed_athlete = self.remove(number)
        print('Random athlete removed is: ', removed_athlete.name)
