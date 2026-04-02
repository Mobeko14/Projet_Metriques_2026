from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('hello.html')

@app.route('/histogramme')
def histogramme():
    return render_template('histogramme.html')

@app.route('/graphique')
def graphique():
    return render_template('graphique.html')

@app.route('/paris')
def paris():
    data = [
        {"datetime": "2026-04-01T00:00", "temperature_c": 15},
        {"datetime": "2026-04-02T00:00", "temperature_c": 17},
        {"datetime": "2026-04-03T00:00", "temperature_c": 16},
        {"datetime": "2026-04-04T00:00", "temperature_c": 18},
        {"datetime": "2026-04-05T00:00", "temperature_c": 20},
        {"datetime": "2026-04-06T00:00", "temperature_c": 19},
        {"datetime": "2026-04-07T00:00", "temperature_c": 21}
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)