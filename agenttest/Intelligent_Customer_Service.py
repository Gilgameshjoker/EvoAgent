from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory
import sqlite3

# 1. 定义工具
def query_order(order_id: str) -> str:
    """查询订单状态"""
    conn = sqlite3.connect('ecommerce.db')
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
        "退货": "退货政策: 7天无理由退货, 商品需保持完好...",
        "发货": "发货时间: 工作日下单当天发货, 节假日顺延...",
        "支付": "支付方式: 支持微信、支付宝、信用卡...",
    }
    # 简单的关键词匹配
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


# 2. 创建工具列表
tools = [
    Tool(
        name="QueryOrder",
        func=query_order,
        description="查询订单状态。输入订单号，返回订单详情。"
    ),
    Tool(
        name="SearchFAQ",
        func=search_faq,
        description="搜索常见问题答案。输入问题关键词。"
    ),
    Tool(
        name="DetectEmotion",
        func=detect_emotion,
        description="检测用户情绪。输入用户消息文本。"
    ),
]

# 3. 创建客服Agent
llm = ChatOpenAI(model="gpt-4", temperature=0.7)

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

customer_service_prompt = """
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

可用工具:
{tools}

对话历史:
{chat_history}

用户问题: {input}
{agent_scratchpad}
"""


agent = create_react_agent(llm, tools, customer_service_prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True,
    max_iterations=5,
)

# 4. 使用示例
def chat_with_customer(user_input):
    result = agent_executor.invoke({"input": user_input})
    return result["output"]

# 对话流程
print("客服: 您好! 我是AI客服小助手, 很高兴为您服务~")

# 第一轮
user1 = "我想查一下订单号12345的状态"
response1 = chat_with_customer(user1)
print(f"客服: {response1}")

# Agent思考过程 (verbose=True会显示):
# Thought: 用户想查询订单, 我需要使用QueryOrder工具
# Action: QueryOrder
# Action Input:"12345"
# Observation:订单状态：已发货，商品：iPhone 15，总金额：5999元
# Thought：我现在知道订单信息了
# Final Answer：您的订单12345已经发货啦！。。。

# 第二轮（记忆上下文）
user2 = "什么时候能到？"
response2 = chat_with_customer(user2)
print(f"客服: {response2}")

# Agent会记得在讨论订单12345