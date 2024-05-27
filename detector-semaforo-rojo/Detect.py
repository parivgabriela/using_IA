import torch
import cv2
import numpy as np
model = torch.hub.load('ultralytics/yolov5', 'custom',
                       path='yolov5/runs/train/exp2/weights/best.pt')
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # realizamos la captura del video
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    #detectamos
    detect = model(frame)

    # mostramos FPS
    cv2.imshow("Detectar semaforos", np.squeeze(detect.render()))

    #leer el techlado
    t = cv2.waitKey(5) #ms
    if t == 27:
        break
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

