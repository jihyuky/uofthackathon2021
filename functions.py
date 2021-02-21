"""
Functions used in the main.py
"""
import nltk


def create_freq_table(terms: str) -> dict[str, int]:
    """Returns a frequency table with the words as the keys and the
    values as the number of time it occurs in a given text string.

    It removes "stop words" such as "the", "with", "of", and "and"
    """

    # Make a set of "stop words"
    trivial_words = set(nltk.corpus.stopwords.words("english"))

    # Tokenize the string by words
    word_list = nltk.word_tokenize(terms)

    # Initialize a snowball stemmer
    stemmer = nltk.stem.snowball.SnowballStemmer("english")

    # Initialize a dictionary for the frequency table
    fr_table = {}

    punct = ['.', ',', '!', '?', ';', ':', '"', "'", '*', '(', ')', '[', ']', '{', '}', '/', '$'
             '%', ' ^', '``', """''"""]

    for word in word_list:

        # Stem the word
        word = stemmer.stem(word)

        # If the word is a punctuation or a "stop word", do not count it.
        if word in trivial_words or word in punct:
            continue

        # Add frequency if it is already in the dictionary
        elif word in fr_table:
            fr_table[word] += 1

        # Add the word as a new key if it does not exist in the dictionary
        else:
            fr_table[word] = 1

    # Weighing the words in the subheadings separately
    sentence_list = nltk.sent_tokenize(terms)

    titles = []
    for sentence in sentence_list:
        if "\n" in sentence:
            titles.append(sentence.split('\n')[0])

    for heading in titles:
        for word in heading:
            # Stem the word
            word = stemmer.stem(word)

            # If the word is a punctuation or a "stop word", do not count it.
            if word in trivial_words or word in punct:
                continue

            # Add frequency if it is already in the dictionary
            elif word in fr_table:
                fr_table[word] += 2

            # Add the word as a new key if it does not exist in the dictionary
            else:
                fr_table[word] = 2

    return fr_table


def create_sentence_list(terms: str) -> list[str]:
    """Returns the sentence list of a given term
    """
    sentence_list_bad = nltk.sent_tokenize(terms)

    sentence_list_good = []

    punct = ['.', ',', '!', '?', ';', ':', '"', "'", '*', '(', ')', '[', ']', '{', '}', '/', '$'
                                                                                             '%',
             ' ^', '``', """''"""]

    # Remove the headings from the sentence if it contains it
    for sentence in sentence_list_bad:
        if "\n" in sentence and sentence.split('\n')[1] != '':
            if len(sentence.split('\n')[1]) > 40 and sentence.split('\n')[1][-1] not in punct:
                sentence_list_good.append(sentence.split('\n')[1] + ".")
            elif len(sentence.split('\n')[1]) > 40 and sentence.split('\n')[1][-1] in punct:
                sentence_list_good.append(sentence.split('\n')[1])
        elif len(sentence) > 40 and sentence[-1] not in punct:
            sentence_list_good.append(sentence + ".")
        elif len(sentence) > 40 and sentence[-1] in punct:
            sentence_list_good.append(sentence)

    return sentence_list_good


def summary_generator(sentence_list: list[str], freq_table: dict[str, int]) -> str:
    """
    Returns the summary of the terms of conditions using the value of each
    sentence. If a sentence's value is above the threshold, it is included in
    the summary.
    """
    summary = ''
    value_table = create_value_table(sentence_list, freq_table)
    threshold = value_threshold(value_table)

    for sent in sentence_list:
        if (sent[:15] in value_table) and (value_table[sent[:15]]) > threshold:
            summary += sent + ' '

    return summary


def create_value_table(sentence_list: list[str], freq_table: dict[str, float]) -> dict[str, float]:
    """Return the value table for sentence list. It determines the "value" of each sentence
    This is a helper function summary_generator()
    """

    value_table = {}

    for sent in sentence_list:
        value = 0
        length = len(sent)
        # Increase the value of the sentence by the word's frequency
        for word in freq_table:
            if word in sent[:25].lower():
                value += freq_table[word]
        # Divide by the length of the sentence
        value = value / length
        value_table[sent[:15]] = value

    return value_table


def value_threshold(value_table: dict[str, float]):
    """Return the threshold value for the sentence to be considered worthy
    This is a helper function for summary_generator.
    """
    total_value = 0
    all_value = []

    for sent in value_table:
        all_value.append(value_table[sent])
        total_value += value_table[sent]

    all_value.sort()

    # Deciding what the threshold will be. Modify this for different results.
    avg = total_value / len(all_value)
    threshold = max(1.45 * avg, all_value[-13])

    return threshold


def find_scary_phrases(sentence_list: list[str], scary_words: list[str]) -> str:
    """Find and return the 'scary words' in a term of service
    """
    key_points = ''
    num = 1
    for sentence in sentence_list:
        for phrase in scary_words:
            # If a phrase in the scary word list is in the sentence, report the sentence.
            if phrase in sentence:
                key_points += str(num) + ". " + sentence + ' \n \n'
                num += 1
    # if there weren't any of the phrases found, print there was no red flags.
    if key_points == '':
        return "No Red Flags Found"
    return key_points
