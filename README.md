# WordCloud  极简词云

## 基于Anaconda + Pycharm 环境

### 安装
#### 由于Anaconda 默认并未安装 jieba中文分词包和词云生成包wordcloud。
#### 安装jieba/wordcloud：conda install -c conda-forge jieba/wordcloud
#### mac/linux在终端输入指令，Windows在Anaconda Prompt 输入指令。

---

### 数据收寻与整理

#### 免登录的移动端微博API：
```
url = "https://m.weibo.cn/api/container/getIndex?type=wb&queryVal={}&containerid=100103type=2%26q%3D{}&page={}" 
```
#### 获取一定量的json数据，并且要根据微博ID进行去重处理，处理结果如下：
```json
{
    "mid": "4397177504005617",
    "text": "在苹果新品发布会上，所有 iPhone 设备的时间都是定格在9:41。为什么苹果对其情有独钟？因为2007年1月7日9:41，是乔布斯发布第一代 iPhone 的时间。「9：41」",
    "userid": "1978107555",
    "username": "手机界大佬",
    "reposts_count": 0,
    "comments_count": 1,
    "attitudes_count": 4
}
```

---

### 生成词云
#### 基于所整理json格式的数据，使用 jieba 分词器的 TF-IDF 关键词提取，需要对其中的文本去除大量的停用词，例如（你，我，他，这，是）。
#### 将上一步得到的关键词用空格串联起来形成一个字符串，以及一幅底层图像一并传入 wordcloud。

---

### 案例：
![Jobs]("jobs_wc.png")
