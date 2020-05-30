import graphene
import uuid
import nltk
import pickle
import gensim
import re
from gensim import corpora
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import regexp_tokenize


class TopicsModelling(graphene.Mutation):
    id = graphene.String()
    topics_result = graphene.List(graphene.NonNull(graphene.String))

    class Arguments:
        text = graphene.String()

    @staticmethod
    def get_lemma(word):
        lemma = wn.morphy(word)
        if lemma is None:
            return word
        else:
            return lemma

    @staticmethod
    def get_lemma2(word):
        return WordNetLemmatizer().lemmatize(word)

    @staticmethod
    def prepare_text_for_lda(text):
        en_stop = set(nltk.corpus.stopwords.words('english'))
        tokens = regexp_tokenize(text.lower(), '(\\d+|\\w+)')
        tokens = [token for token in tokens if token not in en_stop]
        tokens = [TopicsModelling.get_lemma(token) for token in tokens]

        return tokens

    @staticmethod
    def mutate(self, info, text):
        tokens = TopicsModelling.prepare_text_for_lda(text)
        dictionary = corpora.Dictionary([tokens])
        corpus = [dictionary.doc2bow(text) for text in [tokens]]
        pickle.dump(corpus, open('corpus.pkl', 'wb'))
        dictionary.save('dictionary.gensim')

        num_topics = 1
        lda_model = gensim.models.ldamodel.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)
        lda_model.save('model5.gensim')
        topics = lda_model.print_topics(num_words=2)

        topics_result = []

        for topic in topics:
            print(topic)
            tokenized_topic = re.findall('[a-z]+', topic[1])
            topics_result.extend(tokenized_topic)

        return TopicsModelling(
            id=uuid.uuid4(),
            topics_result=topics_result
        )
