import graphene
# UUID, Universal Unique Identifier, is a python library which helps in generating random objects of 128 bits as ids.
# It provides the uniqueness as it generates ids on the basis of time, Computer hardware (MAC etc.).
import uuid
from textblob import TextBlob


class LanguageDetectionTranslation(graphene.Mutation):
    id = graphene.String()
    language_detection = graphene.String()
    language_translation = graphene.String()

    class Arguments:
        text = graphene.String()
        target_language = graphene.String()

    def mutate(self, info, text, target_language):
        blob = TextBlob(text)
        language_detection = blob.detect_language()
        language_translation = blob.translate(to=target_language)

        return LanguageDetectionTranslation(
            id=uuid.uuid4(),
            language_detection=language_detection,
            language_translation=language_translation
        )
