import json


def load_site_data():
    """
    返回一组内置站点资料的列表，每条记录包含标题、URL、关键词列表、标签和简介。
    """
    return [
        {
            "title": "乐鱼体育门户首页",
            "url": "https://main-index-leyu.com.cn",
            "keywords": ["乐鱼体育", "体育赛事", "在线娱乐"],
            "tags": ["体育", "入口", "首页"],
            "description": "乐鱼体育官方主站，提供最新体育资讯与赛事入口。"
        },
        {
            "title": "乐鱼体育新闻中心",
            "url": "https://main-index-leyu.com.cn/news",
            "keywords": ["乐鱼体育", "新闻动态", "体育新闻"],
            "tags": ["新闻", "体育", "更新"],
            "description": "汇集乐鱼体育相关的最新新闻、公告与行业动态。"
        },
        {
            "title": "乐鱼体育赛事直播",
            "url": "https://main-index-leyu.com.cn/live",
            "keywords": ["乐鱼体育", "直播", "赛事直播"],
            "tags": ["直播", "体育", "实时"],
            "description": "提供多品类体育赛事的高清直播与即时比分。"
        },
        {
            "title": "乐鱼体育游戏库",
            "url": "https://main-index-leyu.com.cn/games",
            "keywords": ["乐鱼体育", "游戏", "娱乐"],
            "tags": ["游戏", "体育", "娱乐"],
            "description": "包含多种体育类电子游戏和互动娱乐项目。"
        },
        {
            "title": "乐鱼体育社区",
            "url": "https://main-index-leyu.com.cn/community",
            "keywords": ["乐鱼体育", "社区", "讨论", "互动"],
            "tags": ["社区", "体育", "用户交流"],
            "description": "用户交流、赛事讨论、心得分享的乐鱼体育官方社区。"
        }
    ]


def format_summary_entry(entry):
    """
    将单条站点记录格式化为结构化摘要文本。
    """
    kw_str = ", ".join(entry["keywords"])
    tag_str = ", ".join(entry["tags"])
    lines = [
        f"标题：{entry['title']}",
        f"URL：{entry['url']}",
        f"关键词：{kw_str}",
        f"标签：{tag_str}",
        f"简介：{entry['description']}",
    ]
    return "\n".join(lines)


def generate_summary(sites):
    """
    遍历所有站点资料，输出一段完整结构化摘要。
    """
    separator = "-" * 50
    parts = ["站点资料结构化摘要", separator]
    for idx, site in enumerate(sites, 1):
        entry_block = [f"【站点 {idx}】"]
        entry_block.append(format_summary_entry(site))
        entry_block.append(separator)
        parts.append("\n".join(entry_block))
    return "\n".join(parts)


def main():
    sites = load_site_data()
    summary = generate_summary(sites)
    print(summary)


if __name__ == "__main__":
    main()