import graphene
from nlp_methods.mutations.classes.tokenizers.word_tokenizer import WordTokenizer
from nlp_methods.mutations.classes.tokenizers.sentences_tokenizer import SentencesTokenizer
from nlp_methods.mutations.classes.tokenizers.regexp_tokenizer import RegexpTokenizer
from nlp_methods.mutations.classes.topics.topics_modelling import TopicsModelling
from nlp_methods.mutations.classes.sentiment.sentiment_analysis import SentimentAnalysis


class Mutation(graphene.ObjectType):
    word_tokenizer = WordTokenizer.Field()
    sentence_tokenizer = SentencesTokenizer.Field()
    regexp_tokenizer = RegexpTokenizer.Field()
    topics_modelling = TopicsModelling.Field()
    sentiment_analysis = SentimentAnalysis.Field()


class Query(graphene.ObjectType):
    pass
