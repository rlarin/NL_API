import graphene
# UUID, Universal Unique Identifier, is a python library which helps in generating random objects of 128 bits as ids.
# It provides the uniqueness as it generates ids on the basis of time, Computer hardware (MAC etc.).
import uuid
from nltk.tokenize import word_tokenize


class WordTokenizer(graphene.Mutation):
    id = graphene.String()
    tokens = graphene.List(graphene.NonNull(graphene.String))

    class Arguments:
        text = graphene.String()

    def mutate(self, info, text):
        tokens = word_tokenize(text)

        return WordTokenizer(
            id=uuid.uuid4(),
            tokens=tokens
        )
