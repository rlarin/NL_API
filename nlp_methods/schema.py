import graphene
from .mutations.word_tokenizer import WordTokenizer


class Mutation(graphene.ObjectType):
    word_tokenizer = WordTokenizer.Field()


class Query(graphene.ObjectType):
    pass
