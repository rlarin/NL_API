import graphene
# UUID, Universal Unique Identifier, is a python library which helps in generating random objects of 128 bits as ids.
# It provides the uniqueness as it generates ids on the basis of time, Computer hardware (MAC etc.).
import uuid
import speech_recognition as sr


class SpeechToText(graphene.Mutation):
    id = graphene.String()
    text = graphene.String()

    class Arguments:
        pass

    def mutate(self, info):

        r = sr.Recognizer()

        with sr.Microphone() as source:
            print('Speak something...')
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                print('You said: {}'.format(text))
                return SpeechToText(
                    id=uuid.uuid4(),
                    text=text
                )
            except:
                text = 'Sorry I could not hear you'
                print(text)
                return SpeechToText(
                    id=uuid.uuid4(),
                    text=text
                )
