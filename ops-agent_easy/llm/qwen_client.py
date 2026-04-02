# ================================
# LLM调用层（千问）
# ================================

import requests

API_KEY = "sk-340afc593bba49af83aefd73e9f73ac5"

url = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"

# 设置请求头并指定 UTF-8 编码
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json; charset=UTF-8"  # 确保使用 UTF-8 编码
}


def ask_llm(prompt):
    """
    调用LLM获取决策
    """
    data = {
        "model": "qwen-plus",
        "messages": [
            {"role": "system", "content": "你是运维分析助手"},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        # 打印请求头和数据以便调试
        print("Request Headers:", headers)
        print("Request Data:", data)

        # 发送 POST 请求
        res = requests.post(url, headers=headers, json=data)

        # 检查响应状态码
        res.raise_for_status()  # 如果响应状态码不是 200，会抛出异常

        # 解析 JSON 响应
        result = res.json()
        return result["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as e:
        # 请求失败时返回错误信息
        print(f"Request failed: {e}")
        return "check_metrics"  # fallback
    except Exception as e:
        # 捕获其他任何异常
        print(f"An error occurred: {e}")
        return "check_metrics"  # fallback