from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    string = request.form['string']
    converted_string = string.upper()
    return render_template('result.html', converted_string=converted_string)

if __name__ == '__main__':
    app.run(debug=True)
