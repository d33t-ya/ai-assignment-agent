from flask import Flask, render_template, request, jsonify
from agent import explain_assignment, extract_features

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/explain', methods=['POST'])
def api_explain():
    data = request.get_json()
    question = data.get('question', '')
    result, features = explain_assignment(question)
    return jsonify({'result': result, 'features': features})

if __name__ == '__main__':
    app.run(debug=True)
