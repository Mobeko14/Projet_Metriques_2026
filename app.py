from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('hello.html')

@app.route('/histogramme')
def histogramme():
    return render_template('histogramme.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)