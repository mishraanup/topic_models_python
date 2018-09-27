#!/usr/bin/env python

# By: Anup Mishra (anupmishratech@gmail.com)

"""This code generates topic models from a text document

Example usage:
    python topic_model.py DOCUMENT_NAME.txt 5
    python topic_model.py resources/document_embc_2015.txt 3
"""


# imports
import re
import spacy
import argparse
import gensim
from gensim import corpora
from sets import Set


# [START topic_model]
def topic_model(text, n_topics):
    """ A simple TOPIC MODEL generator using gensim and spaCy

    Parameters:
        text (str) : a text document name; eg. DOCUMENT.txt
        n_topics (int) : number of topics to be generated; eg. 5

    Return:
        list : a list of words representing topics
    """

    # Load english tokenizer from spacy
    nlp = spacy.load('en_core_web_sm')

    # empty list to start with!
    token_list = []

    # read data from file
    # then tokenize excluding stop words
    # finally create the list - > token_list that would have all the single words
    with open(text) as f:
        for line in f:
            doc = nlp(unicode(line, 'utf-8'))
            # get tokens
            tokens = [token.lemma_.strip() for token in doc if len(token.lemma_) > 4 and not token.is_stop]

            if len(tokens) > 1:
                token_list.append(tokens)

    # use corpora from gensim to create a dictionary of words
    dictionary = corpora.Dictionary(token_list)

    # create the corpus using bag of words
    corpus = [dictionary.doc2bow(token) for token in token_list]

    # create LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=n_topics, id2word=dictionary, passes=100)

    # get topics
    topics = ldamodel.print_topics(num_words=5)

    # get the individual words in a set
    regex = r'"(.*?)"'
    set_of_words = Set()
    for topic in topics:
        set_of_words = set_of_words.union(re.findall(regex, topic[1]))

    # return the set or words as a list
    return list(set_of_words)
# [END topic_model]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('text',
                        help='The text input file.')
    parser.add_argument('n',
                        help='Number of topics')
    args = parser.parse_args()
    topic_list = topic_model(args.text, args.n)
    print topic_list
