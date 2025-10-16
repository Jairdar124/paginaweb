# generate_espacios.py
import cv2
import pickle

img = cv2.imread('estacionamiento.png')  # o video frame
espacios = []

print("Selecciona rectángulos. Presiona ENTER/SPACE para confirmar, ESC para salir.")
while True:
    roi = cv2.selectROI('Selecciona espacio (ESC para terminar)', img, False)
    if roi == (0,0,0,0):
        break
    espacios.append(tuple(map(int, roi)))
    # mostrar rectángulos en la imagen
    for x,y,w,h in espacios:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.imshow('Preview', img)
    key = cv2.waitKey(1)
    # si presionas ESC (27) puedes terminar la seleccion
    if key == 27:
        break

cv2.destroyAllWindows()

with open('espacios.pkl', 'wb') as f:
    pickle.dump(espacios, f)

print(f"Guardado {len(espacios)} espacios en espacios.pkl")
