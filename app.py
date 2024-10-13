from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/theory')
def theory():
    return render_template('theory.html')

@app.route('/tests')
def tests():
    return render_template('tests.html')

@app.route('/calculators')
def calculators():
    return render_template('calculators.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/article1')
def article1():
    return render_template('article1.html')

@app.route('/article2')
def article2():
    return render_template('article2.html')

@app.route('/article3')
def article3():
    return render_template('article3.html')

@app.route('/article4')
def article4():
    return render_template('article4.html')

@app.route('/test1')
def test1():
    return render_template('test1.html')

@app.route('/test2')
def test2():
    return render_template('test2.html')

@app.route('/test3')
def test3():
    return render_template('test3.html')

@app.route('/test4')
def test4():
    return render_template('test4.html')

if __name__ == '__main__':
    app.run(debug=True)