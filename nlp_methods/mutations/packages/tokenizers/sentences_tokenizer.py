import graphene
import uuid
from nltk.tokenize import sent_tokenize


class SentencesTokenizer(graphene.Mutation):
    id = graphene.String()
    sentences = graphene.List(graphene.NonNull(graphene.String))

    class Arguments:
        text = graphene.String()

    def mutate(self, info, text):
        sentences = sent_tokenize(text)

        return SentencesTokenizer(
            id=uuid.uuid4(),
            sentences=sentences
        )
