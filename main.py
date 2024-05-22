from flask import Flask, render_template, request
import os
import codecs

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        file = request.files['myfile']
        file.save(os.path.join(file.filename))
        with codecs.open(file.filename,'r' ,'utf-8') as f:
            file_content = f.read()
        os.remove(file.filename)
        answer = analiz(file_content)
    return render_template('index.html', ans= answer[0], povtor= answer[1])

def analiz(file_content):
    razdeliteli = ",?.;:!\'\"()[]{}<>/|\\&*^%$#@`~_+=№\n\r1234567890—"
    for razdelitel in razdeliteli:
        file_content = file_content.replace(razdelitel, ' ')
    file_content = file_content.lower()
    words = file_content.split(' ')
    list_of_words = set(words)
    list_of_words.remove('')
    if "-" in list_of_words:
        list_of_words.remove('-')
    schetchick = {}
    for word in list_of_words:
        schetchick[word] = 0
    max_povtor = 0
    max_key = ''
    for word in words:
        for sr_word in list_of_words:
            if sr_word == word:
                schetchick[sr_word] += 1
    for key, value in schetchick.items():
        if value > max_povtor:
            max_key = key
            max_povtor = value
    return max_key, max_povtor

if __name__ == '__main__':
    app.run(debug=False)