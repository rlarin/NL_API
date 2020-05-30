import graphene
from nlp_methods.mutations.packages.tokenizers.word_tokenizer import WordTokenizer
from nlp_methods.mutations.packages.tokenizers.sentences_tokenizer import SentencesTokenizer
from nlp_methods.mutations.packages.tokenizers.regexp_tokenizer import RegexpTokenizer
from nlp_methods.mutations.packages.topics.topics_modelling import TopicsModelling
from nlp_methods.mutations.packages.sentiment.sentiment_analysis import SentimentAnalysis
from nlp_methods.mutations.packages.translation.language_detection_translation import LanguageDetectionTranslation
from nlp_methods.mutations.packages.speech.speech_to_text import SpeechToText


class Mutation(graphene.ObjectType):
    word_tokenizer = WordTokenizer.Field()
    sentence_tokenizer = SentencesTokenizer.Field()
    regexp_tokenizer = RegexpTokenizer.Field()
    topics_modelling = TopicsModelling.Field()
    sentiment_analysis = SentimentAnalysis.Field()
    language_detection_translation = LanguageDetectionTranslation.Field()
    speech_to_text = SpeechToText.Field()


class Query(graphene.ObjectType):
    pass
