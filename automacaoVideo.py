# Programa que pega vídeos de vestibular e guarda em playlists de forma automática
# Gabriel Novais
# 22/08/2024

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Informações de login
email = "pythonautomacaoctrlplay@gmail.com"
senha = "ctrlplay"

# Lista de matérias:
materias = ["Matemática", "Física", "Química", "Bioloiga", "História", "Geografia"]

videos_qtd = 0# Quantidade de vídeos adicionados nas playlist

# Inicializando o navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    
# Função para criar uma nova playlist
def criar_playlist(materia):
    print("criou uma nova playlist")
    driver.find_element(By.XPATH, '//*[@id="endpoint"]/tp-yt-paper-item').click()
    time.sleep(1)

    # Digitar o nome da nova playlist
    name_input = driver.find_element(By.XPATH, '//*[@id="input-1"]/input')
    name_input.send_keys(f"{materia} Vestibular")
    time.sleep(1)

    # Salvar a nova playlist
    driver.find_element(By.XPATH, '//*[@id="actions"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]').click()
    time.sleep(3)

# Realizar o login
driver.get("https://accounts.google.com/signin/v2/identifier?service=youtube")
time.sleep(5)

# Inserir o e-mail
email_input = driver.find_element(By.ID, "identifierId")
email_input.send_keys(email)
email_input.send_keys(Keys.RETURN)
time.sleep(5)

# Inserir a senha
senha_input = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
senha_input.send_keys(senha)
senha_input.send_keys(Keys.RETURN)
time.sleep(8)

# Loop pelas matérias
for materia in materias:

    #Buscando vídeos:
    driver.get('https://www.youtube.com')
    time.sleep(2)

    # Encontrar a barra de pesquisa e buscar a matéria
    barra_de_pesquisa = driver.find_element(By.NAME, "search_query")
    barra_de_pesquisa.clear()
    barra_de_pesquisa.send_keys(f"vídeo aula {materia} vestibular")
    barra_de_pesquisa.send_keys(Keys.RETURN)
    time.sleep(7)
    
    # Capturar os títulos dos vídeos e seus links
    videos = driver.find_elements(By.XPATH, '//a[@id="video-title"]')
    contador = 0  # Inicializando o contador fora do loop

# Convertendo o elemento HTML em links
    for i in range(len(videos)):
        video = videos[i].get_attribute("href")

    # Filtrando apenas links de vídeos que não sejam "shorts"
        if "shorts" not in video:
            videos[contador] = video  # Armazenando o link no índice atual do contador
            contador += 1  # Incrementa o contador apenas se o vídeo não for um "shorts"

    # Remover quaisquer espaços vazios no array após a filtragem
    videos = videos[:contador]

    # Adicionando o vídeo na playlist enquanto houver vídeos no vetor
    contador_de_videos = 0# Variável que controla o índice do array videos[]
    for video in videos:
        driver.get(str(videos[contador_de_videos]))# Abrindo o vídeo na próxima página
        time.sleep(6)
        driver.find_element(By.XPATH, '//*[@id="button-shape"]/button/yt-touch-feedback-shape/div/div[2]').click()# Mais opções do vídeo (3 pontinhos)
        time.sleep(2)
        bt_salvar = driver.find_element(By.XPATH, '//*[@id="items"]/ytd-menu-service-item-renderer[2]/tp-yt-paper-item/yt-formatted-string')#.click()# Botão de salvar
        contador = 1# Contador para passar por todos os botões dos 3 pontinhos:
        while str(bt_salvar.text) != "Save" and str(bt_salvar.text) != "Salvar":
            elemento = f'//*[@id="items"]/ytd-menu-service-item-renderer[{contador}]/tp-yt-paper-item/yt-formatted-string'
            bt_salvar = driver.find_element(By.XPATH, elemento)#.click()# Botão de salvar
            contador+=1
        bt_salvar.click()
        time.sleep(2)

        # Verificar se a playlist já existe
        try:
            playlist_button = driver.find_element(By.XPATH, f"//*[contains(text(), '{materia} Vestibular')]")
            print(playlist_button.text)
            playlist_button.click()
        except:
            criar_playlist(materia)
        contador_de_videos+=1
        videos_qtd+=1

print("PROGRAMA ENCERRADO COM SUCESSO!")
print(f"\nFORAM ADICIONADOS {videos_qtd} AO TODO!")
# Fechar o navegador
driver.quit()
