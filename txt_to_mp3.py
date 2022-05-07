# https://gtts.readthedocs.io/en/latest/

from os import close
from gtts import gTTS
# pip install gtts
from playsound import playsound
# pip install playsound

audio = 'teste.mp3' # nome do audio que será gerado
idioma = 'pt' # idioma utilizado (testado: pt, es, en, fr, ru, ja, ar)
arquivo = gTTS(text="Texto para mp3 com python", lang=idioma, slow=False) # transforma o texto em audio com a biblioteca gTTS
arquivo.save(audio) # salva o arquivo, gerando o mp3 com o nome escolhido
playsound(audio) # reproduz o mp3