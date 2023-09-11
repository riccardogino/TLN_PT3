# Relazione LAB-2

## Consegna
I comuni dizionari a cui siamo abituati partono dalle parole, ovvero dalla forma, per arrivare al contenuto. Esistono alcuni tipi di dizionario chiamati dizionari analogici che funzionano ”al contrario”, ovvero non si ricerca per parola ma per definizione. Questo tipo di ricerca viene chiamata ricerca onomasiologica, ovvero si parte dal contenuto per arrivare alla forma. Proprio su questo si basa la seconda esercitazione. Sempre partendo dai dati sulle definizioni, si richiede di provare a costruire un sistema che utilizzi la molteplicità delle definizioni per risalire al termine "target" in maniera automatica. Non si richiede di "indovinare" ogni termine, ma di avvicinarsi (almeno semanticamente) alla risposta. Provare più soluzioni, includendo meccanismi di filtro delle definizioni (ad es. escludendo quelle meno informative o con caratteristiche particolari), di ricerca nell'albero tassonomico di WordNet (provando a partire da candidati "genus", secondo il principio Genus-Differentia), ecc.

## Struttura Dati
Per la risoluzione dll'esercizio abbiamo utilizzato ***`wordnet`***, ricavato dal corpus della libreria ***`nltk`***. Abbiamo utilizzato poi i ***`dict`*** e le ***`list`*** come strutture dati in cui venivano memorizzati i risultati della computazione.

## Estrazione del Genus
Per identificare il ***Genus***, ossia quel termine che specifica in maniera più generale quello oggetto della definizione, abbiamo utilizzatto dei pattern della forma:
$$it + 's+a+GENUS$$ 
oppure
$$a+GENUS$$
ricercati all'interno della frase. Il procedimento è stato implementato nella funzione ***`get_genus(sentence)`***.

### Esempio di estrazione del Genus
```
get_genus("A construction used to divide two rooms, temporarily closing the passage between them")

OUTPUT
['construction']
```

## Ricerca del termine target
Per ricercare il termine target, siamo partiti dal Synset del Genus, e per ogni elemento dell'insieme abbiamo trovato gli iponimi, selezionando poi i più frequenti come termini target.

La funzione che implementa queto passaggio è `get_target_term(sentence)`
```
get_target_term("A construction used to divide two rooms, temporarily closing the passage between them")

OUTPUT
{'structure': 58,
 'building': 11,
 'construction': 11,
 'wall': 5,
 'ship': 5,
 'room': 5,
 'part': 5,
 'people': 5}
```
## Risultati
Abbiamo eseguito la funzione `get_target_term(sentence)` per ogni definizione contenuta all'interno del file `TLN-definitions-23.tsv`, e poi controllato quante volte il termine target calcolato corrispondeva a quello desiderato, ottenendo i seguenti risultati
```
{'door': 0.23333333333333334,
 'ladybug': 0.0,
 'pain': 0.06666666666666667,
 'blurriness': 0.0}
```

Come si può notare dal risultato ottenuto, più il termine target è concreto e generico, più è probabile che la ricerca abbia match positivo.