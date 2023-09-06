# Relazione LAB-3

## Consegna
Si richiede un’implementazione della teoria sulle valenze di Patrick Hanks. In particolare, partendo da un corpus a scelta e uno specifico verbo (tendenzialmente non troppo frequente e/o generico ma nemmeno raro), l’idea è di costruire dei possibili cluster semantici, con relativa frequenza. Ad es. dato il verbo "to see" con valenza = 2, e usando un parser sintattico (ad es. Spacy), si possono collezionare eventuali fillers per i ruoli di subj e obj del verbo, per poi convertirli in semantic types. Un cluster frequente su "to see" potrebbe unire subj = noun.person con obj = noun.artifact. Si richiede di partire da un corpus di almeno alcune centinaia di istanze del verbo.

## Struttura Dati
Abbiamo creato un dizionario contenente i supersensi di Wordnet associati ciascuno al proprio elenco di synset di WordNet.


## Estrazione frasi dal corpus SemCor
Abbiamo importato il corpus SemCor e abbiamo ottenuto una lista di frasi sotto forma di token per la ricerca del verbo scelto, selezionando solo le frasi contenenti tale verbo e andandole a trasformare in una stringa unica.

## Ricerca del soggetto e oggetto
Per ogni frase, utilizziamo la libreria SpaCy (nlp) per analizzare la struttura sintattica e ottenere informazioni sui token della frase. In particolare andiamo ad analizzare se il token è un soggetto "nsubj" o un oggetto  "dobj", andando a estrarre il lemma  e i synset associati andandoli a salvare in una matrice.
