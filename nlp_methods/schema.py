import graphene
from graphene_django import DjangoObjectType

from .models import InputText


class InputTextType(DjangoObjectType):
    class Meta:
        model = InputText


class WordTokenize(graphene.Mutation):
    id = graphene.Int()
    text = graphene.String()
    method = graphene.String()

    class Arguments:
        text = graphene.String()
        method = graphene.String()

    def mutate(self, info, text, method):
        input_text = InputText(text=text, method=method)

        return input_text


class Mutation(graphene.ObjectType):
    word_tokenize = WordTokenize.Field()


class Query(graphene.ObjectType):
    input_text = graphene.List(InputTextType)

    def resolve_input_text(self, info, **kwargs):
        return InputText.objects.all()
