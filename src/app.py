from flask import Flask, request, render_template
from model import Model

from input_processing import format_model_inputs

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_input = dict(request.form)

        print(form_input)

        model_inputs = format_model_inputs(form_input)
        prediction = Model().predict(model_inputs)

        return render_template('index.html', prediction=prediction)
    
    return render_template('index.html')


@app.route('/api/predict_one', methods=['POST'])
def predict():
    request_data = request.get_json()

    print(request_data)

    model_inputs = format_model_inputs(request_data)
    prediction = Model().predict(model_inputs).tolist()

    return {'prediction': prediction}


if __name__ == '__main__':
    app.run(debug=True)