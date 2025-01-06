# Italian Politics Dataset
List of some of the most important Italian parties and political figures.

## Project layout
root
-- license
-- README.md
-- v0
---- v0/italian_parties.json
---- v0/italian_politicians.json
-- v1
---- v1/italian_parties.json
---- v1/italian_politicians.json

## Json Structure
For a party:
```json
{
    "parties":[
        {
            "name":"Partito Democratico",
            "website":"https://...",
            "leader":"Elly Schlein",
            "famous_members":[""],
            "founders":[""],
            "foundation_date":""
        },
        {...}
    ]
}
```

For a political figure:
```json
{
    "politicians":[
        {
            "name":"Giorgia Meloni",
            "party":"Fratelli d'Italia",
            "roles":["Co-founder of Fratelli d'Italia", "Italian Prime Minister"]
        }
    ]
}
```

## NOTE
1. This project is under the CC BY-SA 4.0 license.