import json

class Politician():
    def __init__(self, name: str, party: str, roles: list[str], category: str):
        self.name = name
        self.party = party
        self.roles = roles
        self.category = category

    def __str__(self):
        return f"Name: {self.name}\nParty: {self.party}\nRoles: {self.roles}\nCategory: {self.category}\n\n"
    
def get_data() -> list[Politician]:
    with open('v0/italian_politicians.json', 'r') as autog:
        data = json.load(autog)
        return [Politician(**politician) for politician in data["politicians"]]
    
for politician in get_data():
    print(politician)