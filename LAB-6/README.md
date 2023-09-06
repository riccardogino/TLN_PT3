# Relazione LAB-6


## Consegna
Lab-6a: ranking su basicness dei synset di WordNet. Si richiede di creare un mapping tra i synset di WordNet ed un basicness score (ad es. [0, 1]), utilizzando dati, risorse, features e approcci che credete opportuni alla risoluzione del task.

## Struttura Dati
Abbiamo salvato all'interno di una lista tutti i synset di Wordnet riferiti ai nomi.
Dopo aver calcolato per ogni synset il baasicness score abbiamo salvato all'intenro di un dizionario il synset più il suo valore di score associato.

## Logica
Per effettuare il mapping abbiamo sfruttato la gerarchia di wordnet usufruendo del fatto che gli elementi in cima sono macro categorie degli elementi più in basso nel grafo.
Per prima cosa abbiamo calcolato la profondità massima del grafo di wordnet salvando il valore in una variabile `max_depth`.
Dopo di che per ogni synset di wordnet abbiamo calcolato la sua profondità nell'albero e quindi il rapporto tra la `max_depth` dell'albero e la profondità del synset in questione.
Il risultato di questo rapporto consiste nel basicness score,

## Risultati 
I risultato sono visualizzabili all'interno di un grafico a barre.

