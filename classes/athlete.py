class Athlete:
    # This class define a model to Athlete.
    # That just temporarily stores data
    def __init__(self, name, team, role):
        self.name = name
        self.team = team
        self.role = role
        self.next = None

