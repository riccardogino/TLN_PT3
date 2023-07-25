Lab-1

Misurazione dell’overlap lessicale tra una serie di definizioni per concetti generici/specifici e concreti/astratti. Partendo dai dati sulle definizioni (presente nella cartella "dati" su Moodle), si richiede di calcolare la similarità 2-a-2 tra le definizioni (ad es. usando la cardinalità dell'intersezione dei lemmi normalizzata sulla lunghezza minima delle definizioni), aggregando (ed effettuando la media degli score di similarità) sulle due dimensioni (concretezza / specificità). 



Lab-2

I comuni dizionari a cui siamo abituati partono dalle parole, ovvero dalla forma, per arrivare al contenuto. Esistono alcuni tipi di dizionario chiamati dizionari analogici che funzionano ”al contrario”, ovvero non si ricerca per parola ma per definizione. Questo tipo di ricerca viene chiamata ricerca onomasiologica, ovvero si parte dal contenuto per arrivare alla forma. Proprio su questo si basa la seconda esercitazione. Sempre partendo dai dati sulle definizioni, si richiede di provare a costruire un sistema che utilizzi la molteplicità delle definizioni per risalire al termine "target" in maniera automatica. Non si richiede di "indovinare" ogni termine, ma di avvicinarsi (almeno semanticamente) alla risposta. Provare più soluzioni, includendo meccanismi di filtro delle definizioni (ad es. escludendo quelle meno informative o con caratteristiche particolari), di ricerca nell'albero tassonomico di WordNet (provando a partire da candidati "genus", secondo il principio Genus-Differentia), ecc.



Lab-3

Si richiede un’implementazione della teoria sulle valenze di Patrick Hanks. In particolare, partendo da un corpus a scelta e uno specifico verbo (tendenzialmente non troppo frequente e/o generico ma nemmeno raro), l’idea è di costruire dei possibili cluster semantici, con relativa frequenza. Ad es. dato il verbo "to see" con valenza = 2, e usando un parser sintattico (ad es. Spacy), si possono collezionare eventuali fillers per i ruoli di subj e obj del verbo, per poi convertirli in semantic types. Un cluster frequente su "to see" potrebbe unire subj = noun.person con obj = noun.artifact. Si richiede di partire da un corpus di almeno alcune centinaia di istanze del verbo.


Lab-4a (in alternativa a Lab-4b)


Si richiede un'implementazione di un sistema di text segmentation, prendendo ispirazione da TextTiling. In particolare, partendo da un corpus composto da almeno 3 sezioni su tematiche molto diverse (ad es. potete usare paragrafi da tre pagine di Wikipedia diverse), dovrete testare il vostro sistema in modo che riesca ad individuare le giuste linee di taglio (o quasi).



Lab-4b (in alternativa a Lab-4a)

Si richiede un'implementazione di un metodo per la generazione di una nuova lingua (che chiameremo NL). In particolare, partendo da una lingua di partenza L1 (ad es. la lingua Inglese), si prendano i termini di L1 usando un dizionario elettronico (ad es. WordNet o BabelNet). Per ogni termine t ed i suoi sensi S_t, dovrete cercare un nuovo termine tt (in una seconda lingua L2 a vostra scelta) da accoppiare a t, per la costruzione del termine t-tt, da inserire in NL. Il termine tt in L2 va selezionato tra quelli meno ambigui per il concetto S_t di riferimento. Si richiede di calcolare un valore di riduzione dell'ambiguità della nuova lingua rispetto a quella di partenza (ad es. calcolando il numero di sensi associabili ai termini t-tt in NL rispetto a quelli associabili ai termini t in L1. Una volta implementato il sistema, potrete cambiare la lingua L2 per valutare il potere "disambiguante" di diverse lingue rispetto a quella di partenza L1.



Lab-5
Si richiede un'implementazione di un esercizio di Topic Modeling, utilizzando librerie open (come ad es. GenSim (https://radimrehurek.com/gensim/). Si richiede l'utilizzo di un corpus di almeno 1k documenti. Testare un algoritmo (ad esempio LDA) con più valori di k (num. di topics) e valutare la coerenza dei risultati, attraverso fine-tuning su parametri e pre-processing. Update: essendo che spesso i topic, per essere interpretabili, devono contenere content words, potete pensare di filtrare solamente i sostantivi in fase di preprocessing (cioè POS=noun).



Lab-6

Si richiede di sviluppare uno tra i seguenti tre moduli: 

Lab-6a: ranking su basicness dei synset di WordNet. Si richiede di creare un mapping tra i synset di WordNet ed un basicness score (ad es. [0, 1]), utilizzando dati, risorse, features e approcci che credete opportuni alla risoluzione del task. 

Lab-6b: basicness in downstream tasks. Si richiedere l'uso dei concetti e del dataset fornito su basicness (e/o altri dati e risorse) all'interno di in un task esistente (ad es. WSD, MT, text simplification, text segmentation, summarization, ecc.) motivandone e dimostrandone l'utilità (anche solamente in casi/domini specifici).

Lab-6c: classificazione basic/advanced. Si richiedere l'uso (o meno) del dataset su basicness per fare classificazione automatica (binaria, basic/advanced) su nuovi termini e/o synset presi in esame.



Valutazione

La valutazione degli esercizi osserverà i seguenti criteri: conoscenza personale del codice presentato; correttezza del codice, semplicità e leggibilità; livello di approfondimento sui risultati ottenuti (ad es. contezza sui limiti degli approcci implementati, eventuali tentativi alternativi, ecc.).