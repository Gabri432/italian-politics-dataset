# Dataset sulla politca italiana
Lista di alcuni dei più importanti partiti politici e figure politiche (attualmente attive).

Questa lista include principalmente:

- ministri;
- deputati;
- senatori;
- presidenti di regione;
- europarlamentari.

I partiti inclusi sono:

- Fratelli d'Italia;
- Lega;
- Forza Italia;
- Noi Moderati;
- Azione;
- Italia Viva;
- +Europa;
- Partito Democratico;
- Alleanza Verdi e Sinistra;
- others (altri), deputati o senatori appartenenti al gruppo Misto, incluse le Minoranze Linguistiche e il Gruppo Per le Autonomie (SVP-PATT, Campobase).

## Layout del progetto
```
root
-- license
-- README.md

-- v0 (struttura dati non stabile)
---- v0/italian_parties.json
---- v0/italian_politicians.json
---- v0/scripts/ (cartella contenente degli script per la versione 0)
------ scripts/print_parties.py (stampa i partiti)
------ scripts/print_politicians.py (stampa i politici)


-- v1 (futura struttura dati stabile)
---- v1/italian_parties.json
---- v1/italian_politicians.json
---- v1/scripts/ (cartella contenente degli script per la versione 1, ciascuna cartella avrà i propri script)
------ scripts/print_parties.py
------ scripts/print_politicians.py
```

## Struttura dei Json
Per un partito:
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
            "eu_parliamentarians":[""],
            "founders":["..."],
            "foundation_date":"14th of October, 2007"
        },
        {...}
    ]
}
```

Per una figura politica:
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

## Come usarlo

1. Per clonare il repository:
```
git clone https://github.com/Gabri432/italian-politics-dataset.git
```

2. Per stampare i partiti:
```
python v0/scripts/print_parties.py
```

3. Per stampare i politiici:
```
python v0/scripts/print_politicians.py
``` 


## NOTE
1. Questo progetto è sotto la [licenza](https://github.com/Gabri432/italian-politics-dataset?tab=CC-BY-SA-4.0-1-ov-file) CC BY-SA 4.0.

2. Questo progetto non è stato inteso/pensato per l'uso commerciale durante il suo sviluppo. Sii accorto se intendi fare tale utilizzo.

3. I dati sono pubblicamente disponibili qui (in lingua italiana): 
    - [Sito web del governo italiano](https://www.governo.it/it/);
    - [Sito web del Senato](https://www.senato.it/home);
    - [Sito web della Camera](https://www.camera.it/);
    - [Sito web del Parlamento](https://www.parlamento.it/)
    - [Sito web dell'Europarlamento](https://www.europarl.europa.eu/meps/it/search/advanced?countryCode=IT)

4. Puoi contribuire riportando evenutali bug, problemi o suggerendo miglioramenti [qui](https://github.com/Gabri432/italian-politics-dataset/issues/new).