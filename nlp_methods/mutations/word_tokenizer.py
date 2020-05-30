import graphene
from nltk.tokenize import word_tokenize


class WordTokenizer(graphene.Mutation):
    id = graphene.Int()
    tokens = graphene.List(graphene.NonNull(graphene.String))

    class Arguments:
        regex = graphene.String()
        text = graphene.String()

    def mutate(self, info, text, regex):
        tokens = word_tokenize(text)

        return WordTokenizer(
            id=1,
            tokens=tokens
        )
