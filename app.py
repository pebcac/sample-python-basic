from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

AI_CONTAINER_1 = 'http://gowebapp1.test.svc.cluster.local'
AI_CONTAINER_2 = 'http://gowebapp2.test.svc.cluster.local'

@app.route('/<container_id>')
def proxy(container_id):
    if container_id == '1':
        response = requests.get(AI_CONTAINER_1)
    elif container_id == '2':
        response = requests.get(AI_CONTAINER_2)
    else:
        return jsonify({"error": "Invalid container ID"}), 404

    llm_info = response.headers.get('LLM-Header', 'Not provided')
    return jsonify({
        "service_called": container_id,
        "llm_info": llm_info,
        "original_response": response.json()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
