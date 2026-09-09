import warnings
from datetime import datetime

# 精准屏蔽这条弃用警告，其他警告正常输出
warnings.filterwarnings(
    "ignore",
    message="create_react_agent has been moved to langchain.agents"
)

import os
from langchain_openai import ChatOpenAI
from langchain_core.tools import StructuredTool
from langgraph.prebuilt import create_react_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import sqlite3


# ========== 工具函数 ==========
def query_order(order_id: str) -> str:
    """查询订单状态"""
    conn = sqlite3.connect(r'C:\Users\Admin1\PycharmProjects\PythonLangchainTest1\testMiddle\ecommerce.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT status, items, total FROM orders WHERE order_id = ?",
        (order_id,)
    )
    result = cursor.fetchone()
    conn.close()
    if result:
        status, items, total = result
        return f"订单状态: {status}, 商品: {items}, 总金额: {total}元"
    else:
        return "未找到该订单"


def search_faq(question: str) -> str:
    """搜索FAQ知识库"""
    faq_db = {
        "退货": "退货政策：7天无理由退货，商品需保持完好...",
        "发货": "发货时间：工作日下单当天发货，节假日顺延...",
        "支付": "支付方式：支持微信、支付宝、信用卡...",
    }
    for key, answer in faq_db.items():
        if key in question:
            return answer
    return "未找到相关FAQ，建议转人工客服"


def detect_emotion(text: str) -> str:
    """检测用户情绪"""
    negative_words = ["生气", "不满意", "糟糕", "差", "垃圾"]
    for word in negative_words:
        if word in text:
            return "negative"
    return "neutral"


tools = [
    StructuredTool.from_function(
        func=query_order,
        name="QueryOrder",
        description="查询订单状态。输入订单号，返回订单详情。"
    ),
    StructuredTool.from_function(
        func=search_faq,
        name="SearchFAQ",
        description="搜索常见问题答案。输入问题关键词。"
    ),
    StructuredTool.from_function(
        func=detect_emotion,
        name="DetectEmotion",
        description="检测用户情绪。输入用户消息文本。"
    ),
]


llm = ChatOpenAI(
    model="deepseek-v4-flash",
    api_key="sk-cf7ade6fd155489b97dd133573ec1e7c",
    base_url="https://api.deepseek.com/v1",
    temperature=0.7
)

system_text = """
你是一个友好、专业的电商客服AI助手。

你的职责:
1. 热情回答用户问题
2. 查询订单信息
3. 处理退换货问题
4. 如遇复杂问题，建议转人工客服

重要原则:
- 始终保持礼貌和耐心
- 如果用户情绪不好，先安抚情绪
- 准确查询信息，不要编造数据
- 不确定时建议转人工
"""

# ✅ 构建 ChatPromptTemplate，满足你要求的模板形式
prompt = ChatPromptTemplate.from_messages([
    ("system", system_text),
    MessagesPlaceholder(variable_name="messages"),
])

# ✅ create_react_agent 可以直接接收 ChatPromptTemplate 对象
agent = create_react_agent(llm, tools, prompt=prompt)


def chat_with_customer(user_input, messages: list):
    resp = agent.invoke({"messages": [*messages, ("user", user_input)]})
    new_messages = resp["messages"]
    output_msg = new_messages[-1].content
    return new_messages, output_msg

class EnhancedCustomerServiceAgent:
    def __init__(self, graph_agent):
        self.agent = graph_agent
        self.human_agent_queue = []
        self.msg_history = []  # 维护对话历史，适配langgraph

    def handle_message(self, user_input):
        # 1. 前置检测情绪（外层Python先执行，不等LLM调用工具）
        emotion = detect_emotion(user_input)
        if emotion == "negative":
            comfort_msg = "非常抱歉给您带来不好的体验，我会尽快帮您解决问题...."
            print(f"客服: {comfort_msg}")

        # 2. Agent调用，langgraph格式 {messages: [...]}
        try:
            resp = self.agent.invoke({
                "messages": [*self.msg_history, ("user", user_input)]
            })
            new_messages = resp["messages"]
            result = new_messages[-1].content
            # 更新内部对话历史
            self.msg_history = new_messages

            # 3. 判断是否需要转人工
            if self._need_human_agent(result):
                return self._transfer_to_human(user_input)
            return result

        except Exception as e:
            # 出错时转人工
            return self._transfer_to_human(user_input)

    def _need_human_agent(self, agent_response):
        # 检测关键词
        keywords = ["转人工", "不能解决", "复杂问题"]
        return any(kw in agent_response for kw in keywords)

    def _transfer_to_human(self, user_input):
        self.human_agent_queue.append({
            "user_input": user_input,
            "timestamp": datetime.now(),
        })
        return "我为您转接人工客服，请稍等...."


if __name__ == "__main__":
    print("客服: 您好! 我是AI客服小助手, 很高兴为您服务~")
    msg_history = []

    res1_msg, res1 = chat_with_customer("我想查一下订单号12345的状态", msg_history)
    msg_history = res1_msg
    print(f"客服: {res1}")

    res2_msg, res2 = chat_with_customer("什么时候能到?", msg_history)
    msg_history = res2_msg
    print(f"客服: {res2}")

    enhanced_agent = EnhancedCustomerServiceAgent(agent)
    response3 = enhanced_agent.handle_message("我的订单有问题，很生气！")
    # res2_msg, res2 = chat_with_customer("什么时候能到?", msg_history)
    # msg_history = res2_msg
    # print(f"客服: {res2}")