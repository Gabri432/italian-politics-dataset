# Italian Politics Dataset
List of some of the most important Italian parties and political figures.

## Project layout
```
root
-- license
-- README.md

-- v0 (unstable data structure)
---- v0/italian_parties.json
---- v0/italian_politicians.json

-- v1 (future stable data structure)
---- v1/italian_parties.json
---- v1/italian_politicians.json
```

## Json Structure
For a party:
```json
{
    "parties":[
        {
            "name":"Partito Democratico",
            "website":"https://...",
            "leaders":["Elly Schlein"],
            "deputees":[""],
            "senators":[""],
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
            "roles":["Co-founder of Fratelli d'Italia", "Italian Prime Minister"],
            "category":"minister"
        }
    ]
}
```

## How to use it

To clone the repository:
```
git clone https://github.com/Gabri432/italian-politics-dataset.git
```


## NOTES
1. This project is under the CC BY-SA 4.0 [license](https://github.com/Gabri432/italian-politics-dataset?tab=CC-BY-SA-4.0-1-ov-file).

2. This project was not intended for commercial use.

3. Data are publicly available there (in Italian language): 
    - [Italian government website](https://www.governo.it/it/);
    - [Italian Senate website](https://www.senato.it/home);
    - [Italian Chamber website](https://www.camera.it/);
    - [Italian Parliament Website](https://www.parlamento.it/)

4. You can contribute by reporting bugs, issues or potential improvements [here](https://github.com/Gabri432/italian-politics-dataset/issues/new).