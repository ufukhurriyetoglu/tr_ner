import flask
from flask import request, jsonify, request
from ner import recognize

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# post için url
@app.route('/api/v1/ner', methods=['POST'])
def ner_api():
    try:
        text = request.json['text'] #request içinden text alınıyor
        if type(text)==str: # eğer input str ise devam et
            output = recognize(text) # adlı varlıklar belirleniyor
            return jsonify({"output": output}) 
        else:
            return jsonify({"error": "only string input, please"})
    except:
        return jsonify(
            {"error": "Did you mean to send: {'text': 'some text'}"}
        )
# api çalıştırılıyor
app.run()
