import pandas as pd
import numpy as np
import random
from tqdm import tqdm
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
#%matplotlib inline
import warnings;
warnings.filterwarnings('ignore')
df = pd.read_excel('Online Retail.xlsx')
print(df.head())

# 检查缺失值数据
print(df.isnull().sum())

# 删除缺失值所在行
df.dropna(inplace=True)

df['StockCode']= df['StockCode'].astype(str)

customers = df["CustomerID"].unique().tolist()
print(len(customers))

# 打乱消费者id
random.shuffle(customers)
# 提取90%的消费者
customers_train = [customers[i] for i in range(round(0.9*len(customers)))]
# 分为训练集和验证集
train_df = df[df['CustomerID'].isin(customers_train)]
validation_df = df[~df['CustomerID'].isin(customers_train)]

# 存储消费者的购买历史
purchases_train = []
# 用商品代码填充列表
for i in tqdm(customers_train):
    temp = train_df[train_df["CustomerID"] == i]["StockCode"].tolist()
    purchases_train.append(temp)
# 存储消费者的购买历史
purchases_val = []
# 用商品代码填充列表
for i in tqdm(validation_df['CustomerID'].unique()):
    temp = validation_df[validation_df["CustomerID"] == i]["StockCode"].tolist()
    purchases_val.append(temp)

# 训练word2vec模型
# window 句子中当前和预测单词之间的最大距离，取词窗口大小
# sg 训练时算法选择 0:skip-gram, 1: CBOW
# hs 0: 当这个为0 并且negative 参数不为零，用负采样，1：层次 softmax
# negative 负采样，大于0是使用负采样，当为负数值就会进行增加噪音词
# alpha 初始学习率
# min_alpha 随着学习进行，学习率线性下降到这个最小数
# seed 向量初始化的随机数种子

model = Word2Vec(window = 10, sg = 1, hs = 0,negative = 10, alpha=0.03, min_alpha=0.0007,seed = 14)
model.build_vocab(purchases_train, progress_per=200)
model.train(purchases_train, total_examples = model.corpus_count,
epochs=10, report_delay=1)

model.init_sims(replace=True)

print(model)

# 提取向量
X = model[model.wv.vocab]
print(X.shape)


products = train_df[["StockCode", "Description"]]
# 去重
products.drop_duplicates(inplace=True, subset='StockCode', keep="last")
# 创建一个商品id和商品描述的字典
products_dict = products.groupby('StockCode')['Description'].apply(list).to_dict()
# 字典测试
print(products_dict['84029E'])

def similar_products(v, n = 6):
    # 为输入向量提取最相似的商品
    ms = model.similar_by_vector(v, topn= n+1)[1:]
    # 提取相似产品的名称和相似度评分
    new_ms = []
    for j in ms:
            pair = (products_dict[j[0]][0], j[1])
            new_ms.append(pair)
    return new_ms

print(similar_products(model['90019A']))