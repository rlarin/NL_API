import graphene
# UUID, Universal Unique Identifier, is a python library which helps in generating random objects of 128 bits as ids.
# It provides the uniqueness as it generates ids on the basis of time, Computer hardware (MAC etc.).
import uuid
from nltk.tokenize import regexp_tokenize


class RegexpTokenizer(graphene.Mutation):
    id = graphene.String()
    tokens = graphene.List(graphene.NonNull(graphene.String))

    class Arguments:
        regexp = graphene.String()
        text = graphene.String()

    def mutate(self, info, text, regexp):
        tokens = regexp_tokenize(text, regexp)

        return RegexpTokenizer(
            id=uuid.uuid4(),
            tokens=tokens
        )
