import json
import uuid

def generate_sql_from_json(json_data_str):
    insert_sql = "INSERT INTO `xbfox_forum`.`xb_application` (`name`,`icon`,`description`,`link`,`user_id`,`application_id`,`highlights`,`collect_num`,`like_num`,`visit_number`,`status`, `pay_type`, `faq`) VALUES\n"
    # str 转 json
    json_data = json.loads(json_data_str)

    # 从json数据中提取必要的信息
    name = json_data.get("name", "")
    icon = "app.png"  # 这里的icon字段暂时使用了固定值，你可以根据实际情况修改
    description = json_data.get("description", "")
    link = json_data.get("link", "")
    highlights = ", ".join(json_data.get("highlights", []))
    faqs = json_data.get("faqs", [])
    faq_json = json.dumps(faqs, ensure_ascii=False)
    # 生成一个随机的UUID
    random_id = uuid.uuid4()
    # 将UUID转换为字符串
    id_str = str(random_id).replace('-', '')

    # 构造SQL语句
    insert_sql += f"('{name}', '{icon}', '{description}', '{link}', '01hcw2kbaxw86nx21parwatbna', '{id_str}', '{highlights}', 0, 0, 0, 1, 10, '{faq_json}');"

    return (insert_sql, id_str, name, json_data.get("tags", []), json_data.get("category", "") )


# 示例json数据
json_data = {
    "name": "HuluAI",
    "description": "AI绘图、写作、对话，简洁高效，支持多种场景",
    "link": "https://h5.cxyhub.com/",
    "highlights": [
        "集成ChatGPT4.0、Midjourney、Dall·E3等多大模型",
        "无限使用，不限次数",
        "支持角色设定、多语言模型、聊天对话场景",
        "AI绘图功能：支持线稿、图片解析、多图融合等场景",
        "网站兼容PC端、手机端，简洁易用"
    ],
    "faqs": [
        {
            "question": "HuluAI是什么？",
            "answer": "HuluAI是一款集成了AI绘图、写作、对话功能的网站。"
        },
        {
            "question": "适用人群是什么？",
            "answer": "适合需要AI绘图、写作、对话功能的个人和团体用户。"
        },
        {
            "question": "主要功能有哪些？",
            "answer": "主要功能包括AI对话，AI写作和AI绘画。用户可以选择不同的大语言模型，设定角色，选择不同的聊天对话场景。在绘画方面，支持线稿模型、图片解析、多图融合等几大场景。"
        },
        {
            "question": "如何使用？",
            "answer": "用户可以通过网站https://h5.cxyhub.com/进行在线使用。新用户注册后可免费体验15次。"
        },
        {
            "question": "相关费用是多少？",
            "answer": "新用户注册后可免费体验15次，之后费用可能根据使用情况而定，请查阅官方网站获取最新信息。"
        }
    ]
}

if __name__ == '__main__':
    # 生成SQL语句
    sql_statement = generate_sql_from_json(json_data)
    print(sql_statement)