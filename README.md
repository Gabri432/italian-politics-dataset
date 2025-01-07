# Italian Politics Dataset
List of some of the most important Italian (currenlty active) parties and political figures.

The list primarly includes:

- ministers;
- deputies;
- senators;
- regional presidents.

The parties included are:

- Fratelli d'Italia;
- Lega;
- Forza Italia;
- Noi Moderati (alliance);
- Azione;
- Italia Viva;
- +Europa;
- Partito Democratico;
- Alleanza Verdi e Sinistra;
- others, deputies or senators classified in group Misto (Mixed), including Minoranze Linguistiche (Linguistic Minorities), and Gruppo Per le Autonomie (SVP-PATT, Campobase) (Group for the Autonomies).

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
            "group":"Partito Democratico - Italia Democratica e Progressista",
            "website":"https://...",
            "leaders":["Elly Schlein"],
            "deputies":["..."],
            "senators":["..."],
            "founders":["..."],
            "foundation_date":"14th of October, 2007"
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