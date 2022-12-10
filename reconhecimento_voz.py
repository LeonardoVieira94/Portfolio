from os import system
from pyttsx3 import init
from speech_recognition import Recognizer, Microphone

class Comandos:

    def assistente_ouvir(self):
        rec = Recognizer()

        with Microphone() as source:
            print("Fale..")
            rec.pause_threshold = 0.6
            audio = rec.listen(source)
            try:
                print("Reconhecendo Audio..")
                palavras = (rec.recognize_google(audio, language='pt-br')).lower()
                print(f'Frase dita: {palavras}')
            except:
                print('Voz não reconhecida.')
                return None
        return palavras

    def assistente_falar(self, falar):
        engine = init('sapi5')
        engine.say(falar)
        engine.runAndWait()

    def assistente_acoes(self):
        frase = self.assistente_ouvir()
        if frase != None:
            if 'bloco de notas' in frase:
                print('abrindo bloco de notas!')
                self.assistente_falar('abrindo bloco de notas')
                system("start notepad")
            elif 'arquivos' in frase:
                print('abrindo arquivos')
                self.assistente_falar('abrindo arquivos')
                system("start explorer")
            elif 'cmd' in frase:
                print('Abrindo cmd!')
                self.assistente_falar('abrindo cmd')
                system('start cmd')
            elif 'navegador' in frase:
                print('Abrindo navegador!')
                self.assistente_falar('abrindo navegador')
                system("start msedge")
        else:
            print('Nenhuma ação realizada.')
            
if __name__ == '__main__':
    assistente = Comandos()
    assistente.assistente_acoes()