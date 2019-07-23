import json
import imageio
import jieba.analyse
from wordcloud import WordCloud


def keywords(mblogs):
    text = []
    for blog in mblogs:
        keyword = jieba.analyse.extract_tags(blog['text'])
        text.extend(keyword)
    return text


def gen_img(texts, img_file):
    data = ' '.join(text for text in texts)
    image_coloring = imageio.imread(img_file)
    wc = WordCloud(
        background_color='white',
        mask=image_coloring,
        font_path='msyh.ttc'
    )
    wc.generate(data)

    wc.to_file(img_file.split('.')[0] + '_wc.png')


if __name__ == '__main__':
    keyword = '乔布斯'
    mblogs = json.loads(open('data_{}.json'.format(keyword), 'r', encoding='utf-8').read())
    print('微博总数：', len(mblogs))

    words = []
    for blog in mblogs:
        words.extend(jieba.analyse.extract_tags(blog['text']))

    print("总词数：", len(words))

    gen_img(words, 'jobs.png')
