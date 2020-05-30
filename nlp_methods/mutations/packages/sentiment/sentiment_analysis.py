import graphene
# UUID, Universal Unique Identifier, is a python library which helps in generating random objects of 128 bits as ids.
# It provides the uniqueness as it generates ids on the basis of time, Computer hardware (MAC etc.).
import uuid
from textblob import TextBlob


class SentimentAnalysis(graphene.Mutation):
    id = graphene.String()
    sentiments_result = graphene.String()  # graphene.List(graphene.NonNull(graphene.String))

    class Arguments:
        text = graphene.String()

    @staticmethod
    def sentiments(text):
        blob = TextBlob(text)
        if blob.sentiment.polarity < 0:
            result = 'Negative 😠'
        elif blob.sentiment.polarity > 0:
            result = 'Positive 😊'
        else:
            result = 'Neutral 😐'

        print(result)
        print(blob.sentiment)
        return result

    def mutate(self, info, text):
        sentiments_result = SentimentAnalysis.sentiments(text)
        return SentimentAnalysis(
            id=uuid.uuid4(),
            sentiments_result=sentiments_result
        )
