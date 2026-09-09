import os
from langgraph.graph import StateGraph, START, END, MessagesState
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_community.llms import Tongyi

os.environ["DASHSCOPE_API_KEY"] = "sk-ws-H.PDIHHLP.HbnM.MEUCIAE4wZJHK47YQeacJHza73ddXCAhmwUJ3WsVaQgqIFSNAiEA1-OuYZbDwO42iIBkG1fz58VQHOlQr0l5900GHT75Y2Y"

llm = Tongyi(model="qwen-plus", temperature=0.7)


class ChatState(MessagesState):
    user_name: str
    conversation_count: int


def chatbot_node(state: ChatState):
    """聊天节点"""
    # 构建系统提示
    system_prompt = f"""你是一个友好的AI助手。
用户名: {state.get('user_name', '用户')}
当前是第 {state.get('conversation_count', 0)} 轮对话。"""

    messages = [SystemMessage(content=system_prompt)] + state["messages"]
    response = llm.invoke(messages)

    return {
        "messages": [AIMessage(content=response)],
        "conversation_count": state.get("conversation_count", 0) + 1
    }


# 构建图
workflow = StateGraph(ChatState)
workflow.add_node("chatbot", chatbot_node)
workflow.add_edge(START, "chatbot")
workflow.add_edge("chatbot", END)
app = workflow.compile()


# 多轮对话
state = {"messages": [], "user_name": "小红", "conversation_count": 0}

conversations = [
    "你好，我是小红",
    "我刚才说我叫什么？",
    "帮我推荐一本Python书"
]

for user_input in conversations:
    print(f"用户: {user_input}")
    state["messages"].append(HumanMessage(content=user_input))
    result = app.invoke(state)
    state = result
    print(f"助手: {result['messages'][-1].content}\n")
