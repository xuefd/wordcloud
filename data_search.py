import re
import json
import requests

url = "https://m.weibo.cn/api/container/getIndex?type=wb&queryVal={}&containerid=100103type=2%26q%3D{}&page={}"


def clean_text(text):
    dr = re.compile(r'(<)[^>]+>', re.S)
    dd = dr.sub('', text)
    dr = re.compile(r'#[^#]+#', re.S)
    dd = dr.sub('', dd)
    dr = re.compile(r'@[^ ]+ ', re.S)
    dd = dr.sub('', dd)
    return dd.strip()


def fetch_data(query_val, page_id):
    resp = requests.get(url.format(query_val, query_val, page_id))
    card_group = json.loads(resp.text)['data']['cards'][0]['card_group']
    print('url：', resp.url, ' --- 条数:', len(card_group))

    mblogs = []
    for card in card_group:
        mblog = card['mblog']
        blog = {'mid': mblog['id'],
                'text': clean_text(mblog['text']),
                'userid': str(mblog['user']['id']),
                'username': mblog['user']['screen_name'],
                'reposts_count': mblog['reposts_count'],
                'comments_count': mblog['comments_count'],
                'attitudes_count': mblog['attitudes_count']
                }
        mblogs.append(blog)
    return mblogs


def remove_duplication(mblogs):
    mid_set = {mblogs[0]['mid']}
    new_blogs = []
    for blog in mblogs[1:]:
        if blog['mid'] not in mid_set:
            new_blogs.append(blog)
            mid_set.add(blog['mid'])
    return new_blogs


def fetch_pages(query_val, page_num):
    mblogs = []
    for page_id in range(1 + page_num + 1):
        try:
            mblogs.extend(fetch_data(query_val, page_id))
        except Exception as e:
            print(e)

    print("去重前：", len(mblogs))
    mblogs = remove_duplication(mblogs)
    print("去重后：", len(mblogs))

    fp = open('data_{}.json'.format(query_val), 'w', encoding='utf-8')
    json.dump(mblogs, fp, ensure_ascii=False, indent=4)
    print("已保存至 data_{}.json".format(query_val))


if __name__ == '__main__':
    fetch_pages('乔布斯', 66)
