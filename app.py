# 创建一个名为app.py的Flask应用
from flask import Flask, request, jsonify
from api import get_answer

app = Flask(__name__)

@app.route('/get_answer', methods=['GET'])
def answer_route():
    question = request.args.get('question')  # 获取传递的问题参数
    if question:
        # 获取答案并以JSON格式返回
        answer = get_answer(question)
        return jsonify(answer)
    else:
        return jsonify({'error': 'Missing question parameter'}), 400

# 在Vercel上需要的启动代码
if __name__ == '__main__':
    app.run(debug=True, port=8080)

