from flask import Flask, render_template, request

app = Flask(__name__)

# Datos simulados de paquetes (esto es lo que simula tus datos de Excel)
packages = [
    {
        "tracking_number": "ITD-3-12345678",
        "status": "En tránsito",
        "destination": "Lima, Perú",
        "shipping_date": "2024-12-07",
        "expected_delivery": "2024-12-21"
    },
    {
        "tracking_number": "ITD-1-12345678",
        "status": "En tránsito",
        "destination": "Arequipa, Perú",
        "shipping_date": "2024-12-07",
        "expected_delivery": "2024-12-23"
    },
    {
        "tracking_number": "ITD-0-12345678",
        "status": "En espera de recolección",
        "destination": "Cusco, Perú",
        "shipping_date": "2024-12-07",
        "expected_delivery": "2024-12-22"
    },
]

# Función para buscar información de un paquete
def get_package_status(tracking_number):
    for package in packages:
        if package["tracking_number"] == tracking_number:
            return package  # Aquí regresamos todos los datos del paquete
    return {"error": "No se encontró el número de rastreo."}

@app.route('/', methods=['GET', 'POST'])
def index():
    tracking_info = None
    if request.method == 'POST':
        tracking_number = request.form.get('tracking_number', '').strip()
        tracking_info = get_package_status(tracking_number)
    return render_template('index.html', tracking_info=tracking_info)

if __name__ == '__main__':
    app.run(debug=True)
