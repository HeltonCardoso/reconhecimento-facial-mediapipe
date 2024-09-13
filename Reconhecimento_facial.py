import cv2
import mediapipe as mp

#inicalizando a webCam
webcam = cv2.VideoCapture(0)
#iniciando o reconhecimento facil do MediaPipe
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils


while True:
   #Ler Informações da webcam  
   verificador, frame =  webcam.read()
   if not verificador:
    break
   #Reconhecer os rostos que tem ali dentro 
   lista_rostos = reconhecedor_rostos.process(frame)
   if lista_rostos.detections:
      for rosto in lista_rostos.detections:
         #desenha os rostos na imagem 
         desenho.draw_detection(frame, rosto)
         cv2.imshow("RECONHECIMENTO DE ROSTOS V1.0", frame)

   if cv2.waitKey(5) == 27:
    break
    #quando apertar ESQ, para o loop
webcam.release()
cv2.destroyAllWindows()