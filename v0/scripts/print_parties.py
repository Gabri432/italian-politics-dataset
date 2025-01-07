import json

class Party:
    def __init__(
            self, name: str, group: str, website: str, leaders: list[str], deputies: list[str], senators: list[str], founders: list[str], 
            foundation_date: str
            ):
        self.name = name
        self.group = group
        self.website = website
        self.leaders = leaders
        self.deputies = deputies
        self.senators = senators
        self.founders = founders 
        self.foundation_date = foundation_date

    def __str__(self):
        return (
            f"Name: {self.name}\nGroup: {self.group}\nWebsite: {self.website}\n"
            f"Leaders: {self.leaders}\ndeputies: {self.deputies}\nSenators: {self.senators}\n\n"
            )
    
def get_data() -> list[Party]:
    with open('v0/italian_parties.json', 'r') as autog:
        data = json.load(autog)
        return [Party(**party) for party in data["parties"]]
    
for party in get_data():
    print(party)