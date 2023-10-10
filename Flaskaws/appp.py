from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a dictionary to store person information
person_info = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        address = request.form['address']
        person_info['name'] = name
        person_info['age'] = age
        person_info['address'] = address
    return render_template('index.html', person_info=person_info)

@app.route('/get_india_info')
def get_india_info():
    # You can fetch and display information about India here
    # For simplicity, we'll just display a message
    india_info = "India is a country in South Asia."
    return render_template('india_info.html', india_info=india_info)

if __name__ == '__main__':
    app.run(debug=True)
