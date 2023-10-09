from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    try:
        name = request.form.get('name')
        if not name:
            raise ValueError("Name is required.")
        greeting = f"Hello, {name}!"
        return render_template('index.html', greeting=greeting)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5086)
