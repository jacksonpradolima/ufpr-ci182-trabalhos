# USAGE
# python recognize_video.py --detector face_detection_model \
#	--embedding-model openface_nn4.small2.v1.t7 \
#	--recognizer output/recognizer.pickle \
#	--le output/le.pickle

# Importação das bibliotecas
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import pickle
import time
import cv2
import os

# Comandos para a execução do arquivo python
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--detector", required=True,
	help="path to OpenCV's deep learning face detector")
ap.add_argument("-m", "--embedding-model", required=True,
	help="path to OpenCV's deep learning face embedding model")
ap.add_argument("-r", "--recognizer", required=True,
	help="path to model trained to recognize faces")
ap.add_argument("-l", "--le", required=True,
	help="path to label encoder")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

# Carregamento dos objetos "serializados" // Carregando o modelo de aprendizado caffemodel
print("[INFO] Carregando o detector de faces...")
protoPath = os.path.sep.join([args["detector"], "deploy.prototxt"])
modelPath = os.path.sep.join([args["detector"],
	"res10_300x300_ssd_iter_140000.caffemodel"]) #Carregamento do modelo Caffe
detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

# Carregamento das imagens serializadas
print("[INFO] Carregando o reconhecimento das faces...")
embedder = cv2.dnn.readNetFromTorch(args["embedding_model"])

# Carregamento do modelo de reconhecimento e dos rótulos das imagens
recognizer = pickle.loads(open(args["recognizer"], "rb").read())
le = pickle.loads(open(args["le"], "rb").read())

# Inicializando a câmera
print("[INFO] Iniciando a stream de video...")
vs = VideoStream(src=0).start()
time.sleep(2.0)

# Inicializando o contador de fps
fps = FPS().start()

# Loop feito pra analisar os frames
while True:
	# Coletando os frames
	frame = vs.read()

	# Deixando o frame das imagens com 600px pra nao distorcer demais
	# e assim mantendo o aspecto da imagem mais natural
	frame = imutils.resize(frame, width=600)
	(h, w) = frame.shape[:2] #mantem a proporção do tamanho do frame

	# Contruindo os padrões a partir das imagens
	imageBlob = cv2.dnn.blobFromImage(
		cv2.resize(frame, (300, 300)), 1.0, (300, 300),
		(104.0, 177.0, 123.0), swapRB=False, crop=False)

	# Aplica os padrões de aprendizado da biblioteca OpenCV para localizar as faces
	# Localiza as faces baseadas na entrada da camera
	detector.setInput(imageBlob)
	detections = detector.forward()

	# Laço em que ocorrem as detecções
	for i in range(0, detections.shape[2]):
		# Estimativa dos graus de confiança e de previsões
		confidence = detections[0, 0, i, 2]

		# Filtrando as detecções
		if confidence > args["confidence"]:
			# Coordenadas para as caixas ao redor das faces
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			# Extraindo as faces
			face = frame[startY:endY, startX:endX]
			(fH, fW) = face.shape[:2]

			# Verifica se o tamanho das faces está no padrao
			if fW < 20 or fH < 20:
				continue

			# Controi um blob para a estimativa da face com base no modelo
			# Aplica a estimativa do blob ao modelo treinado
			# quantificação da face
			faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
				(96, 96), (0, 0, 0), swapRB=True, crop=False)
			embedder.setInput(faceBlob)
			vec = embedder.forward()

			#Classificação e reconhecimento das faces
			preds = recognizer.predict_proba(vec)[0]
			j = np.argmax(preds)
			proba = preds[j]
			name = le.classes_[j]

			# Contrução da caixa em volta das faces
			# Mostra a probabilidade associada a cada face
			text = "{}: {:.2f}%".format(name, proba * 100)
			y = startY - 10 if startY - 10 > 10 else startY + 10
			cv2.rectangle(frame, (startX, startY), (endX, endY),
				(0, 0, 255), 2)
			cv2.putText(frame, text, (startX, y),
				cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

	# Atualização do contador de frames
	fps.update()

	# Exibindo os frames
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# Condição de saída do loop
	if key == ord("q"):
		break

# Parada do timer e exibição das informações de FPS
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# Destruição das telas
cv2.destroyAllWindows()
vs.stop()
