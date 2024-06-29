

sk = "sk-APRXbBzI9LIcHH51PiMeXPm95QoKb5XxWXuA20OcoKZGtZEe"

# from openai import OpenAI
#
# client = OpenAI(
#     api_key=sk,
#     base_url="https://api.moonshot.cn/v1",
# )
#
# completion = client.chat.completions.create(
#     model="moonshot-v1-8k",
#     messages=[
#         {"role": "system",
#          "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
#         {"role": "user", "content": "你好，我叫李雷，1+1等于多少？"}
#     ],
#     temperature=0.3,
# )
#
# print(completion.choices[0].message.content)


from openai import OpenAI
import json
client = OpenAI(
    api_key=sk,
    base_url="https://api.moonshot.cn/v1",
)

text = [
                "文档处理",
                "项目管理",
                "会议工具",
                "时间管理",
                "数据管理",
                "办公协作",
                "运营与产品",
                "销售与市场",
                "编程与技术",
                "自动化工具"
            ]

res = json.dumps(text, ensure_ascii=False)
print(res)
completion = client.chat.completions.create(
    model="moonshot-v1-8k",
    messages=[
        {"role": "user", "content": "帮我总结下面的文本属于哪一个分类,分类的列表如下：'''" + str(res) + "'''文本内容如下：'''question 是什么？answer Gitee提供一系列DevOps服务，包括代码托管、项目协同、代码管理、代码扫描、持续集成、测试管理制品管理和效能度量，致力于提供企业研发管理解决方案。question 适用人群与使用场景？answer 适用于企业，提供研发管理平台，助规划和管理研发过程，提高效率和质量。可用于多种开发项目，包括软件开发、应用程序开发等。question 主要功能？answer 包括多种项目管理模板、代码仓库安全保障、多语言代码扫描、自动化流水线调度引擎和多样化的度量指标。question 如何使用？answer 用户可在Gitee官网注册账号，创建项目并上传代码，利用各项功能管理项目，提高开发效率。question 相关费用？answer 提供企业版和专业版，支持私有化部署，采用订阅制，具体价格根据版本和订阅方式而定。'''"}
    ],
    temperature=0.3,
)

print(completion.choices[0].message.content)