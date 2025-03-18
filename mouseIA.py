# Programa que controla o mouse usando sua mão
# Gabriel Novais
# 19/08/2024

#Importações:
import cv2 #Capturar vídeo da webcam e manipular imagens
import mediapipe as mp #Detecção de mãos e visões computacionais.
import pyautogui #Controlar o mouse e o teclado programaticamente.
import math #Calcular distância dos pontos

# Inicializando o MediaPipe para detecção de mãos
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils #Desenhando os pontos de referência

# Parâmetros para a detecção da mão
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# Captura de vídeo
cap = cv2.VideoCapture(0)

# Obtendo o tamanho da tela
screen_width, screen_height = pyautogui.size()

# Função para calcular a distância entre dois pontos
def calculate_distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2)

# Loop para processar os frames da câmera
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertendo a imagem para RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Processando a imagem para detectar as mãos
    result = hands.process(frame_rgb)
    
    # Obtendo as dimensões do frame
    frame_height, frame_width, _ = frame.shape
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Extraindo as coordenadas do ponto 8 (dedo indicador) e ponto 4 (polegar)
            index_finger_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]
            
            # Calculando a distância entre o polegar e o indicador
            distance = calculate_distance(index_finger_tip, thumb_tip)
            
            # Movendo o cursor do mouse
            x = int(index_finger_tip.x * frame_width)
            y = int(index_finger_tip.y * frame_height)
            
            # Invertendo o eixo x e ajustando o eixo y
            screen_x = screen_width - (screen_width / frame_width * x)
            screen_y = screen_height / frame_height * y
            
            pyautogui.moveTo(screen_x, screen_y)
            
            # Se a distância for menor que um certo limite, considera um clique
            if distance < 0.05:
                pyautogui.click()
            
            # Desenhando as landmarks na mão
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
    # Exibindo o frame com a detecção (sem espelhamento)
    cv2.imshow("Hand Tracking", frame)
    
    # Fechar ao pressionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberação dos recursos
cap.release()
cv2.destroyAllWindows()
