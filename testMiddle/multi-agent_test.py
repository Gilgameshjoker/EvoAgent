from autogen import ConversableAgent, GroupChat, GroupChatManager

llm_config_model = {
        "model": "deepseek-v4-flash",
        "api_key": "sk-cf7ade6fd155489b97dd133573ec1e7c",
        "base_url": "https://api.deepseek.com/v1"
    }

#定义多个Agent
product_manager = ConversableAgent(
    name="PM",
    system_message="你是产品经理，负责需求分析和产品规划。",
    llm_config=llm_config_model,
)

engineer = ConversableAgent(
    name="Engineer",
    system_message="你是工程师，负责技术实现。",
    llm_config=llm_config_model,
)

designer = ConversableAgent(
    name="Designer",
    system_message="你是设计师，负责UI/UX设计。",
    llm_config=llm_config_model,
)

#创建群聊
group_chat = GroupChat(
    agents=[product_manager, engineer, designer],
    messages=[],
    max_round=10,
)

#管理者
manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config_model,
)

#开始协作
# product_manager.initiate_chat(
#     manager,
#     message="我们需要开发一个AI聊天应用，大家讨论一下方案。",
# )

product_manager.initiate_chat(
    manager,
    message="刚才的讨论中大家已经有了相应的大致结果，请生成相应的文档并告知我文档所在位置",
)