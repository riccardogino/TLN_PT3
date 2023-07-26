# Relazione LAB-1

<style>
    body{
        text-align: justify;
    }
</style>

## Consegna
Misurazione dell’overlap lessicale tra una serie di definizioni per concetti generici/specifici e concreti/astratti. Partendo dai dati sulle definizioni (presente nella cartella "dati" su Moodle), si richiede di calcolare la similarità 2-a-2 tra le definizioni (ad es. usando la cardinalità dell'intersezione dei lemmi normalizzata sulla lunghezza minima delle definizioni), aggregando (ed effettuando la media degli score di similarità) sulle due dimensioni (concretezza / specificità). 

## Struttura Dati
Per facilitare l'utilizzo della risorsa testuale, abbiamo deciso di utilizzare un `Dizionario` con la seguante struttura:
```json
{
  "name": {
    "id_1": ["t_1", "t_2", "...", "t_n"],
    "id_2": ["t_1", "t_2", "...", "t_n"],
    "id_m": ["t_1", "t_2", "...", "t_n"]
  }
}
```
dove `name` è la parola delle cui definizioni vogliamo calcolare l'overlap lessicale, mentre `id` è un indice numerico incrementale assegnato ad ogni definizione, che fa da chiave alla definizione pulita e tokenizzata in tokens `t`.

## Lavorazione della frase
Da ogni definizione abbiamo ***rimosso eventuali spazi bianchi*** all'inizio e alla fine della frase tramite la funzione `remove_white_spaces`, poi l'abbiamo ***tokenizzata*** per mezzo del `word_tokenizer` della libreria `nltk`. Successivamente abbiamo calcolato il ***`POS Tag`*** e il ***`lemma`*** per ogni token (tramite il `WordNetLemmatizer` e utilizzando i tag precedentemente trovati). Infine abbiamo rimosso eventuali ***stop_words*** e ***simboli di punteggiatura*** tramite le funzioni `remove_stop_words` e `remove_punctuation`.

## Calcolo della similarità
Abbiamo calcolato la similarità tra due definizioni utilizzando la cardinalità dell'intersezione tra le definizioni tokenizzate normalizzate per la minima tra le due:

$$
\frac{|def_1\cap def_2|}{|def_1|} \lor \frac{|def_1\cap def_2|}{|def_2|}
$$

Abbiamo poi applicato la formula ad ogni possibile coppia di definizioni e calcolato il ***valore medio***, utilizzato poi nella stampa dei risultati.

## Risultati
In funzione dell'input utilizzato, i risultati sono i seguenti:

<table>
    <tr>
        <th></th>
        <th>Astratto</th>
        <th>Concreto</th>
    </tr>
    <tr>
        <th>Generico</th>
        <td>pain: <br>0.17</td>
        <td>door:<br> 0.21</td>
    </tr>
    <tr>
        <th>Specifico</th>
        <td>blurriness:<br> 0.08</td>
        <td>ladybug:<br> 0.49</td>
    </tr>
</table>
