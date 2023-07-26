from functools import reduce
from nltk import word_tokenize
from nltk.corpus import stopwords as sw

import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


def get_wordnet_pos(tag):
    # Mapping tra i POS tag di nltk.pos_tag e quelli di WordNet
    # Per convertire i POS tag ottenuti da nltk.pos_tag in quelli di WordNet
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Consideriamo il sostantivo come fallback


def lemmatize_word(word, pos_tag):
    lemmatizer = WordNetLemmatizer()
    pos = get_wordnet_pos(pos_tag)
    lemma = lemmatizer.lemmatize(word, pos)
    return lemma


def get_lemmatized_tokens_list(tokens):
    tokens_pos = nltk.pos_tag(tokens)
    lemmatized_words = []
    for word, pos_tag in tokens_pos:
        lemma = lemmatize_word(word, pos_tag)
        lemmatized_words.append(lemma)
    return lemmatized_words

def get_lemmatized_tokens_list_pos(tokens):
    tokens_pos = nltk.pos_tag(tokens)
    lemmatized_words = []
    for word, pos_tag in tokens_pos:
        lemma = lemmatize_word(word, pos_tag)
        lemmatized_words.append((lemma, pos_tag))
    return lemmatized_words



tokenizer = word_tokenize


def remove_punctuation(tokenized_sentence):
    context = []
    for w in tokenized_sentence:
        if w.isalpha():
            context.append(w)
    return context

def remove_punctuation_pos(tokenized_sentence):
    context = []
    for w in tokenized_sentence:
        if w[0].isalpha():
            context.append((w))
    return context


def remove_stop_words(token_list):
    stops = set(sw.words('english'))
    clear_tokens = []

    for t in token_list:
        if t not in stops:
            clear_tokens.append(t)
    return clear_tokens

def remove_stop_words_pos(token_list):
    stops = set(sw.words('english'))
    clear_tokens = []

    for t in token_list:
        if t[0] not in stops:
            clear_tokens.append(t)
    return clear_tokens


def remove_stop_words_it(token_list):
    stops = set(sw.words('italian'))
    clear_tokens = []

    for t in token_list:
        if t not in stops:
            clear_tokens.append(t)
    return clear_tokens


def remove_white_spaces(sentence: str) -> str:
    return sentence.strip()


def noise_reduction_it(sentence: str) -> list:

    def closure(*funcs) -> list:
        return reduce(lambda f, g: lambda x: f(g(x)), funcs, lambda x: x)

    return closure(remove_punctuation,
                   remove_stop_words_it,
                   tokenizer,
                   remove_white_spaces)(sentence)


def noise_reduction_en(sentence: str) -> list:

    def closure(*funcs) -> list:
        return reduce(lambda f, g: lambda x: f(g(x)), funcs, lambda x: x)

    return closure(remove_punctuation,
                   remove_stop_words,
                   get_lemmatized_tokens_list,
                   tokenizer,
                   remove_white_spaces)(sentence)

def noise_reduction_en_pos(sentence: str) -> list:

    def closure(*funcs) -> list:
        return reduce(lambda f, g: lambda x: f(g(x)), funcs, lambda x: x)

    return closure(remove_punctuation_pos,
                   remove_stop_words_pos,
                   get_lemmatized_tokens_list_pos,
                   tokenizer,
                   remove_white_spaces)(sentence)

