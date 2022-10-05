from flask import Flask, render_template, url_for,request,json
import requests
app = Flask(__name__,template_folder='templates')

@app.route('/', methods=['post', 'get'])
def index():
    message = ''
    res = ''
    message=json.dumps({"Rut":request.form.get('rut'),"Funcionalidad":request.form.get('funcionalidad'),"funcionalidad2":request.form.get('funcionalidad2')})
    print (message)
    res = requests.post('https://prod-48.eastus2.logic.azure.com:443/workflows/bb94d21e1e6543ad8beeb1f4fbf815e4/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=P-qyJ-w2eg6riSh0gdyoFqxhlzPVfs0nmXB4XzgShko', data = message, headers = {"Content-Type": "application/json"})
    print (res)
    return render_template('index.html', message=message)
