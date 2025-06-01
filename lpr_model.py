import easyocr
import cv2
import numpy as np

reader = easyocr.Reader(['en'])


def detectar_placa(image_bytes):
    np_img = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    results = reader.readtext(img)

    posibles_placas = []
    for (bbox, texto, conf) in results:
        if len(texto) >= 6 and any(char.isdigit() for char in texto):
            posibles_placas.append((texto, conf))

    posibles_placas.sort(key=lambda x: x[1], reverse=True)
    return posibles_placas[0][0] if posibles_placas else "NO DETECTADA"
