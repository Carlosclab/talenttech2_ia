from flask import Flask, request, render_template
import joblib
import os

app = Flask(__name__)

# Ruta base del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Rutas de los modelos
#regression_model_path = os.path.join(BASE_DIR, 'models', 'regression_model.pkl')
classification_model_path = os.path.join(BASE_DIR, 'models', 'classification_model.pkl')

# Carga de los modelos
#regression_model = joblib.load(regression_model_path)
classification_model = joblib.load(classification_model_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    classification_result = None

    if request.method == 'POST':
        input_value = request.form.get('input_value')
        try:
            # Convertir el input a número (depende de tu modelo, aquí suponemos numérico)
            input_value_num = float(input_value)
            X = [[input_value_num]]

            # Predicción con el modelo de regresión
            #prediction = regression_model.predict(X)[0]

            # Predicción con el modelo de clasificación
            class_pred = classification_model.predict(X)[0]
            classification_result = "Alto" if class_pred == 1 else "Bajo"
        except ValueError:
            # Si el valor no se puede convertir a número
            prediction = "Entrada inválida"
            classification_result = "No se pudo clasificar"
    
    return render_template('index.html', prediction=prediction, classification_result=classification_result)

if __name__ == "__main__":
    app.run(debug=True)
