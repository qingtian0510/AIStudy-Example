import logging
import numpy as np
from collections import Counter
# import torch.nn as nn
# import torch
import code
import os
from collections import Counter
import nltk
nltk.download('punkt')



def load_data(in_file):
    cn = []
    en = []
    num_examples = 0
    with open(in_file, 'r') as f:
        for line in f:
            line = line.strip().split("\t")

            en.append(["BOS"] + nltk.word_tokenize(line[0]) + ["EOS"])
            # split chinese sentence into characters
            cn.append(["BOS"] + [c for c in line[1]] + ["EOS"])
    return en, cn

def build_dict(senctences,max_word=50000):
    word_count = Counter()
    #记录每个词出现的次数
    for senctence in senctences:
        for s in senctence:
            word_count[s] += 1

    #把出现最频繁的50000个单词保存下来
    ls = word_count.most_common(max_word)
    total_words = len(ls)+1
    word_dict = {w[0]: index+1 for (index,w) in enumerate(ls)}
    word_dict["UNK"] = 0
    return word_dict,total_words

def encode(en_sentences,cn_sentences,en_dict,cn_dict):
    length = len(en_sentences)
    out_en_sentences = []
    out_cn_sentences = []
    for i in range(length):
        en_seq = [en_dict[w] if w in en_dict else 0 for w in en_sentences[i]]
        cn_seq = [cn_dict[w] if w in cn_dict else 0 for w in cn_sentences[i]]
        out_en_sentences.append(en_seq)
        out_cn_sentences.append(cn_seq)

    def len_argsort(seq):
        return sorted(range(len(seq)),key=lambda x:len(seq[x]))

    sorted_index = len_argsort(out_en_sentences)
    out_en_sentences = [out_en_sentences[i] for i in sorted_index]
    out_cn_sentences = [out_cn_sentences[i] for i in sorted_index]

    return out_en_sentences,out_cn_sentences

def get_minibatches(n, minibatches_size, shuffle = False):
    idx_list = np.arange(0, n, minibatches_size)
    minibatches = []
    if shuffle:
        np.random.shuffle(idx_list)
    for idx in idx_list:
        minibatches.append(np.arange(idx, min(n, idx+minibatches_size)))
    return minibatches


def prepare_data(seqs):
    B = len(seqs)
    lengths = [len(seq) for seq in seqs]
    max_len = np.max(lengths)

    x = np.zeros((B, max_len)).astype('int32')
    x_mask = np.zeros((B, max_len)).astype('float32')
    for idx, seq in enumerate(seqs):
        x[idx, :lengths[idx]] = seq
        x_mask[idx, :lengths[idx]] = 1.
    return x, x_mask   # x:数据矩阵  x_mask:标志矩阵每一个元素是否填充值（0：是填充值）

def gen_examples(en_sentences, cn_sentences, batch_size):
    minibatches = get_minibatches(len(en_sentences),batch_size)

    all_ex = []
    for minibatch in minibatches:
        mb_en_sentences = [en_sentences[t] for t in minibatch]
        mb_x, mb_x_mask = prepare_data(mb_en_sentences)

        mb_cn_sentences = [cn_sentences[t] for t in minibatch]
        mb_y, mb_y_mask = prepare_data(mb_cn_sentences)

        all_ex.append((mb_x, mb_x_mask, mb_y, mb_y_mask))
    return all_ex






