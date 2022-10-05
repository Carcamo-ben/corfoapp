from flask import Flask, render_template, url_for,request,json
import requests
app = Flask(__name__,template_folder='templates')

@app.route('/', methods=['post', 'get'])
def index():
    message = ''
    res = ''
    message=json.dumps({"idProyecto":request.form.get('idProyecto'),"comuna":request.form.get('comuna'),"zonatermica":request.form.get('zonatermica')})
    print (message)
    res = requests.post('https://prod-85.eastus.logic.azure.com:443/workflows/d240ea3b2d4c421eb793d86ed8a0663d/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=xHhaMjj22xzP71gyE4x3V5q8sMkZBXWuoquOwoVG6RE', data = message, headers = {"Content-Type": "application/json"})
    print (res)
    return render_template('index.html', message=message)
