# Slot Machine - Python

Tämä on yksinkertainen kolmen rullan ja kolmen rivin (3x3) peliautomaatti, jossa pelaaja voi panostaa eri rivimäärille ja voittaa symboleista riippuen.

## Ominaisuudet

- Pelaaja voi tallettaa rahaa ennen pelin aloittamista.
- Pelaaja voi valita pelattavien rivien määrän (1-3).
- Pelaaja asettaa panoksen per rivi.
- Satunnaisesti arvottavat symbolit eri arvoilla.
- Voittosumman laskenta rivien ja symbolien perusteella.

## Asennus ja suoritus

Tämä skripti ei vaadi ulkoisia kirjastoja, vaan toimii suoraan Pythonilla. Varmista, että sinulla on Python asennettuna.

### Suorita skripti:

```sh
python main.py
```

## Pelin kulku

1. Pelaaja tallettaa haluamansa summan.
2. Pelaaja valitsee, kuinka monelle riville haluaa panostaa (1-3).
3. Pelaaja asettaa panoksen per rivi (1-100 €).
4. Peli arpoo satunnaiset symbolit rullille.
5. Jos rivillä on voittoyhdistelmä, pelaaja voittaa panoksensa mukaisesti.
6. Pelin tulos näytetään ja mahdollinen voitto lisätään saldoon.

## Symbolit ja voitot

Pelin symbolit ovat:

| Symboli | Voitto per panostettu euro |
| ------- | -------------------------- |
| **A**   | 40 €                       |
| **B**   | 20 €                       |
| **C**   | 10 €                       |
| **D**   | 5 €                        |

Voitto tulee, jos kaikki rivin kolme symbolia ovat samoja.

![image](https://github.com/user-attachments/assets/d2aa7746-1b97-406e-b8fb-eabbc8dbb16d)

