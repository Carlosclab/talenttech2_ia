from flask import Flask, request, render_template
import joblib
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# regression_model_path = os.path.join(BASE_DIR, 'models', 'regression_model.pkl')
classification_model_path = os.path.join(BASE_DIR, 'models', 'classification_model.pkl')

# regression_model = joblib.load(regression_model_path)
classification_model = joblib.load(classification_model_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    classification_result = None
    bg_color = "#ffffff"  # color por defecto (blanco)

    if request.method == 'POST':
        input_value = request.form.get('input_value', None)
        try:
            input_value_num = float(input_value)
            X = [[input_value_num]]
            
            # Predicción de regresión
            # prediction = regression_model.predict(X)[0]

            # Predicción de clasificación
            class_pred = classification_model.predict(X)[0]
            classification_result = "Alto" if class_pred == 1 else "Bajo"
            
            # Cambiar el color de fondo según el resultado de clasificación
            if classification_result == "Alto":
                bg_color = "#f8d7da"  # Fondo rojizo
            else:
                bg_color = "#d4edda"  # Fondo verdoso

        except (ValueError, TypeError):
            prediction = "Entrada inválida"
            classification_result = "No se pudo clasificar"
            bg_color = "#ffffff"

    return render_template('index.html', 
                           prediction=prediction, 
                           classification_result=classification_result,
                           bg_color=bg_color)

if __name__ == "__main__":
    app.run(debug=True)
