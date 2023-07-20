from flask import Flask, request
import json
from VirtualAsistant import AI

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    if request.method == 'GET':
        ai = AI()
        ai.jarvis("date")
        # Poskusimo naložiti v json obliki
        print(ai.response)
        return 'WELCOME'# ...
    
@app.route('/sendCommand', methods=['POST'])
def postjson():
    try:
        ai = AI()
        command = request.args.get("command")
        ai.jarvis(command)
        # Poskusimo naložiti v json obliki
        data = {"answer":ai.response}
        print(data)
        return data# ...
    except Exception as e:
        return e.message()
        # ...
    

app.run(host='127.0.0.1',debug=True, port=1234, use_reloader=False)