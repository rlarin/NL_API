import graphene
from nlp_methods.mutations.classes.word_tokenizer import WordTokenizer
from nlp_methods.mutations.classes.sentences_tokenizer import SentencesTokenizer


class Mutation(graphene.ObjectType):
    word_tokenizer = WordTokenizer.Field()
    sentence_tokenizer = SentencesTokenizer.Field()


class Query(graphene.ObjectType):
    pass
