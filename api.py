# 创建一个新的Python模块，例如api.py

import SparkApi

# 预设的参数
appid = "3c31bff1"  # 你的APPID
api_key = "9ebbdbc6a4e3d7b494327fd6d247aab7"  # 你的API Key
api_secret = "MjM0ZmQ3ZWJkY2Y4MTkyYmFiMGYyZGU0"  # 你的API Secret
domain = "general"  # 使用的模型版本
Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"  # 默认的服务地址

def get_answer(question):
    # 调用你的SparkApi模块，获取答案
    text = []
    question = SparkApi.checklen(SparkApi.getText("user", question))
    SparkApi.answer = ""
    SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
    SparkApi.getText("assistant", SparkApi.answer)
    return SparkApi.text
