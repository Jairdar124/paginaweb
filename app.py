# app.py
import os
from flask import Flask, render_template, jsonify, Response
import pickle
import cv2
import numpy as np

app = Flask(__name__)

# Cargar espacios desde archivo (generado previamente)
ESPACIOS_PATH = os.path.join(os.path.dirname(__file__), 'espacios.pkl')
if not os.path.exists(ESPACIOS_PATH):
    raise FileNotFoundError(f"espacios.pkl no encontrado en {ESPACIOS_PATH}. Genera el archivo con generate_espacios.py y súbelo al repo.")

with open(ESPACIOS_PATH, 'rb') as f:
    espacios = pickle.load(f)

@app.route('/')
def index():
    return "Parking app running"

@app.route('/api/espacios')
def api_espacios():
    return jsonify({"count": len(espacios), "espacios": espacios})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
