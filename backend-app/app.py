import speech_recognition as sr


def functionSwitcher(argument):
    switcher = {
        1: "Bom dia",
        2: "Boa tarde",
        3: "Boa noite"
    }

    for key, value in switcher.items():
        if argument == value:
            return key, value

    return "Function not yet implemented"


def listenSpeech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.7
        r.adjust_for_ambient_noise(source, duration=1)
        print('Say something...')
        audio = r.listen(source)
        print('Translating...\n')
    try:
        command = r.recognize_google(audio, language='pt-BR')
        print('You said: {0}\n'.format(command))
    # loop back to continue to listen for commands if unrecognizable speech
    # is received
    except sr.UnknownValueError:
        print('Sarah did not recognize what you said\n')
        command = listenSpeech()
    return command


while True:
    answer = listenSpeech()

    print(functionSwitcher(answer))
pass
