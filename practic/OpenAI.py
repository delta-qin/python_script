
from openai import OpenAI
import os
import json
os.environ["OPENAI_API_KEY"] = "sk-weGUGZ6zZtI2lFNBE0579bF2F1F94b3f93Ad8aA09c51B178"

def request_ai(prompt):
    client = OpenAI(
        # This is the default and can be omitted
        base_url="https://one.close-api.com/v1/",
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-4",
    )
    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content

def simplify_text(content):
    text = '''
    你是一个数据润色高级写手，专注于提高效率的应用分享，帮我将下面的内容洗稿，主要分为固定的几大类：应用的标签tags（2-5个之间），应用的分类（影音视听、实用工具、聊天社交、图书阅读、时尚购物、摄影摄像、学习教育、旅行交通、金融理财、娱乐消遣、新闻资讯、居家生活、体育运动，医疗健康，效率办公）。
    数据返回的使用JSON格式输出，下面是一个JSON定义，严格按照这个格式返回，value值使用中文。直接输出json，不要有任何多余的字符。例如````json`等等
    {"tags": ["xxx"],"category": "xxx"}
    下面是你需要洗稿的内容：```'''+ content + '''```'''
    #     text = '''
    # 你是一个数据润色高级写手，专注于提高效率的应用分享，帮我将下面的内容洗稿，主要分为固定的几大类：应用名字，一句话描述（最好20字以内），主要功能亮点（每一点单独列出来），FAQS（整体内容保持在300字左右，不要太少。包含是什么？适用人群与使用场景？主要功能（尽可能详细些）？如何使用？相关费用？），应用的标签tags（2-5个之间），应用的分类（影音视听、实用工具、聊天社交、图书阅读、时尚购物、摄影摄像、学习教育、旅行交通、金融理财、娱乐消遣、新闻资讯、居家生活、体育运动，医疗健康，效率办公）。
    # 数据返回的使用JSON格式输出，下面是一个JSON定义，严格按照这个格式返回，value值使用中文。直接输出json，不要有任何多余的字符。例如````json`等等
    # {"name": "xxx","description": "xxx","link": "xxx","highlights": ["xxxx"],"faqs": [{"question": "xxx","answer": "xxxx"}],"tags": ["xxx"],"category": "xxx"}
    # 下面是你需要洗稿的内容：```'''+ content + '''```'''
    res = request_ai(text)
    # 如果 res 是以 ```json 开头的，删除 ```json 和 ``` 结尾的
    if res.startswith("```json"):
        res = res[7:-3]
    # 如果结尾依旧是 ` 有几个删除几个
    while res.endswith("`"):
        res = res[:-1]
    print('res' + res)
    return res


def second_category(category_list, content):
    res = json.dumps(category_list, ensure_ascii=False)
    print(res)
    return request_ai("帮我总结下面的文本属于哪一个分类,直接输出分类的文本，必须严格不要有多余的字符，，例如引号等不要修改分类的文字，输出的格式为单一字符串,例如\"摄影工具\"，不要输出列表没有的内容"
                      "分类的列表如下：'''" + str(
                res) + "'''文本内容如下：'''"+ content +"'''")

# second_category()
#
#
# if __name__ == '__main__':
#     simplify_text("""
#     在学术世界中，论文写作是一项既重要又具挑战性的任务，大家在面对繁杂的研究主题和严格的格式要求时，常常感到不知所措。
#
# 此时，一个能够简化论文写作流程、提供专业辅助的工具显得尤为重要。笔灵AI论文写作是面向700＋学科专业的论文写作服务平台，致力于一键解决所有论文写作难题。该平台支持免费生成千字大纲，创作多种类型论文，且生成速度快、效率高。
#
# 官网入口：https://ibiling.cn/paper
#
#
# 一、笔灵AI论文四大写作优势
# 1.免费千字大纲生成：精准把握论文结构
# 笔灵AI论文写作提供千字大纲的免费生成服务。你只需输入相关关键词，就能获得一个详尽且结构清晰的论文大纲，以此有效规划文章结构。此外，你还可在线编辑大纲，随时删减章节。
#
#
# 2.700+学科专业全覆盖：满足不同专业论文要求
# 笔灵AI论文写作服务于从专科生到研究生的各个学术层次，还提供超过700个不同专业的论文写作支持，从文学、历史到工程、科学，无一不包。无论你学术背景或研究领域如何，都能在这个平台上找到适合自己需求的专业帮助。
#
#
# 3.多类型论文支持：课题论文、开题报告、毕业论文一网打尽
# 笔灵AI论文写作提供对多种类型论文的全面支持。无论是处于学习早期的课题论文、学术研究的开题报告，还是学业的重要里程碑——毕业论文，该平台都能提供专业的写作指导和辅助，使你轻松应对各种类型的论文挑战。
#
#
# 4.论文生成速度：大纲1分钟，全文5分钟
# 笔灵AI论文写作能在短短一分钟内提供完备的论文大纲，仅需五分钟就能完成整篇论文的撰写，充分体现了它在人工智能写作领域的专业优势。你因此可以节约大量准备和撰写论文时间，将更多精力投入到研究和创新中。
#
#
# 二、使用笔灵AI论文写作搞定论文，只需四步：
# 第1步：进入笔灵AI论文写作官方网站。
#
# 第2步，选择专业，并输入题目，生成千字大纲目录。
#
#
# 第3步，编辑大纲，生成全文模板，可增加、删减章节，修改章节内容。
#
#
#
# 无论是毕业论文还是课题论文，笔灵AI论文都能成为你学术写作路上的强大助力，让你的研究工作更加轻松，成果更加显著。
#
# 笔灵AI论文写作官网入口：https://ibiling.cn/paper
#     """)
#     request_ai('''
#     帮我生成一段Python代码，生成如下格式的sql语句：
#
# ```
#     INSERT INTO `xbfox_forum`.`xb_application` (
# 	`name`,`icon`,`description`,`link`,`user_id`,`application_id`,`highlights`,`collect_num`,`like_num`,`visit_number`,`status`,`faq`,
# )
# VALUES
# 	('SunoAI',	'app.png','AI音乐生成，快速创作你的音乐作品。','https://app.suno.ai','01hcw2kbaxw86nx21parwatbna','','全球首个能产生广播级质量音乐的AI模型,自定义和纯音乐两种模式,每天免费玩50次，每月付费10美元可获2500积分,提供Prompt辅助创作',
# 		0,0,0,1,
# 		'[{\"question\":\"SunoAI是什么？\",\"answer\":\"SunoAI是一款AI音乐生成应用，能够快速创作广播级质量的音乐作品。\"},{\"question\":\"适用人群？\",\"answer\":\"适用于希望快速生成音乐作品的音乐爱好者和创作者。\"},{\"question\":\"主要功能是什么？\",\"answer\":\"SunoAI提供自定义模式和纯音乐模式，每天免费玩50次，付费用户每月10美元可获2500积分。提供Prompt辅助创作。\"},{\"question\":\"如何使用SunoAI？\",\"answer\":\"打开https://app.suno.ai，输入歌词或使用提供的Prompt，点击创建，等待生成后下载即可。\"}]',
# 	);
# ```
#
# 	要求读取读取下面格式的json数据，替换json中的数据，保留剩余的数据，生成对应的sql语句，下面是对应的json数据：
# ```
# {
#     "name": "xxx",
#     "description": "xxx",
#     "link": "xxx",
#     "highlights": [
#         "xxxx",
#     ],
#     "faqs": [
#         {
#             "question": "xxx",
#             "answer": "xxxx"
#         },
#     ]
# }
# ```
#     ''')