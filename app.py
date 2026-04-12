from flask import Flask
app = Flask(__name__)
@app.route('/')
def главная():
    return '''<h1>Привет! Ты на курсах по детейлингу!</h1>
           <p>приступим</p>
           '''
@app.route('/courses')
def курсы():
    return 'это твои курсы'
if __name__=='__main__':
    app.run(debug=True)
