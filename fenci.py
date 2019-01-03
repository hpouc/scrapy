#!/usr/bin/python
# coding:utf-8

import jieba_fast as jieba

import pandas as pd
import re
from nltk import FreqDist
import random
from sklearn.model_selection import train_test_split


# 数据预处理

def load_data(path):
    data = pd.read_csv(path, encoding='utf-8')
    data = data.dropna()
    # train_data, test_data = train_test_split(data, test_size=0.3, random_state=0)

    # return train_data, test_data
    return data


def getStopWords(path):
    """获取停用词表"""
    stopwords = pd.read_csv(path, sep="\t", encoding='utf-8')
    stopwords = stopwords['stopword'].values
    return stopwords


def de_stop_words(content_line, stopwords):
    """去停用词
    parm:

    content_line: list
    """
    process_text = []
    for i in range(len(content_line)):
        try:
            line = content_line[i]
            line = line.strip()
            line = line.replace('\n', '')
            line = line.replace('\r', '')
            line = line.replace('\xa0', '')
            line = line.replace('\u3000', '')

            segs = jieba.lcut(line)
            #                 print('去1', segs)
            segs = [item for item in segs if len(item) > 1]
            #                 print('去停', segs)
            segs = [item for item in segs if item not in stopwords]
            process_text.append(segs)

        except Exception as e:
            print(e)
            continue
    # print(process_text)
    return process_text


def de_low_frequency_words(text):
    """去低频词"""
    processed_text = []
    for items in text:
        fdist = FreqDist(items)  # 生成词频的字典
        # 直接获取低频词
        low_fre = fdist.hapaxes()  # 只出现一次的项
        # print(low_fre)
        process_text = [item for item in items if item not in low_fre]
        processed_text.append(process_text)

    return processed_text


def saveData(sentences, filename):
    """保存处理好的文档"""

    print('start saving..')
    with open(filename, 'w', encoding='utf8') as f:
        for line in sentences:
            f.write(line + '\n')
    print('done!')


def preprocessData(data, label, stopwords, filename):
    """数据预处理"""

    sentences = []

    # 处理停用词
    process_stop_words = de_stop_words(data, stopwords)

    # 处理低频词
    # process_low_words = de_low_frequency_words(process_stop_words)

    # 合成fasttext训练数据
    for i in range(len(process_stop_words)):
        # sentences.append("_label_" + str(label[i]) + ' ' + ' '.join(process_low_words[i]))
        sentences.append(' '.join(process_stop_words[i]))

    # 乱序
    random.shuffle(sentences)

    # 最后一步，保存
    saveData(sentences, filename)


if __name__ == '__main__':
    # 预处理 & 特征

    # 第一步：获取数据
    data_path = './data/t_news_valid.csv'
    stopwords_path = './data/stopwords.csv'

    # train_data, test_data = load_data(data_path)
    valid_data = load_data(data_path)
    stopwords = getStopWords(stopwords_path)


    # 第二步：转化为list
    # train_data['title_contents'] = train_data['info_title'] + '\n' + train_data['content']
    # test_data['title_contents'] = test_data['info_title'] + '\n' + test_data['content']
    valid_data['title_contents'] = valid_data['info_title'] + '\n' + valid_data['content']

    # train_list = train_data.title_contents.values.tolist()
    # test_list = test_data.title_contents.values.tolist()
    valid_data_list = valid_data.title_contents.values.tolist()

    # train_label_list = train_data.large_class_label.values.tolist()
    # test_label_list = test_data.large_class_label.values.tolist()

    # 第三步：数据预处理
    # trainData_file = r'./data/train_dblocal_all_0102.txt'
    testData_file = r'./data/valid_data_0103.txt'

    # preprocessData(train_list, train_label_list, stopwords, trainData_file)
    # preprocessData(test_list, test_label_list, stopwords, testData_file)
    preprocessData(valid_data_list, '', stopwords, testData_file)