# Zadanie
Vytvořte kalkulačku se základními matematickými operacemi (+,-,*,/), faktoriálem, umocňováním s přirozenými exponenty (exponenty jsou přirozená čísla), obecnou odmocninou (obecná odmocnina) a jednou další funkcí.

Program lze vytvořit v libovolném programovacím jazyce a bude se skládat z knihovny s matematickými funkcemi (vč. základních operací jako +,-,* apod.), nad kterou bude postaveno grafické uživatelské rozhraní.

Součástí uživatelského rozhraní bude i nápověda.
Program bude možné ovládat klávesnicí (min. základní operace.
K programu bude dodána uživatelská i programová dokumentace.
V uživatelské dokumentaci bude mimo jiné i postup instalace a odinstalace programu pomocí instalátoru (odinstalátoru).
Dále bude uveden návod pro manuální (od)instalaci, tzn. postup překladu ze zdrojových kódů, vytvoření zástupců (ikonek) a dalších akcí, které provádí instalátor.
Program bude distribuován s otevřenými zdrojovými texty pod licencí GNU GPL v. 1, 2 nebo 3).

## Spustenie testov

```
$ sudo apt install python3
$ sudo apt install python3-pip
$ sudo pip install pytest
$ cd src/
$ pytest tests.py
```

## Spustenie GUI

```
$ sudo apt install python3
$ sudo apt install python3-tk
$ cd src/
$ python3 gui.py
```