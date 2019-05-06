from math import log
import operator

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    #返回数据集的行数
    labelCounts = {}
    #保存每个标签(Label)出现次数的字典
    for featVec in dataSet:
    #对每组特征向量进行统计
        currentLabel = featVec[-1]
        #提取标签(Label)信息
        if currentLabel not in labelCounts.keys():
        #如果标签(Label)没有放入统计次数的字典,添加进去
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
        #Label计数
    shannonEnt = 0.0
    #经验熵(香农熵)
    for key in labelCounts:
    #计算香农熵
        prob = float(labelCounts[key])/numEntries
        #选择该标签(Label)的概率
        shannonEnt -= prob * log(prob,2)
        #利用公式计算
    return shannonEnt
    #返回经验熵(香农熵)

def createDataSet():
    dataSet = [[1,1,'yes'],
              [1,1,'yes'],
              [1,0,'no'],
              [0,1,'no'],
              [0,1,'no']]
    #数据集
    labels = ['no surfacing','flippers']
    #分类属性
    return dataSet,labels
    #返回数据集和分类属性

"""
    Function:
        按给定特征划分数据集
    Parameters:
        dataSet——待划分的数据集
        axis——划分数据集的特征
        value——特征的返回值
    Return：
        retDataSet——划分好后的数据集列表
    Modify：
        2017-11-29    
"""
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    #创建返回数据列表对象
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            #去掉axis特征
            reducedFeatVec.extend(featVec[axis+1:])
            #将符合条件的添加到返回的数据里表中
            retDataSet.append(reducedFeatVec)
    return retDataSet
    #返回划分后的数据集

"""
    Function:
        选择最优特征
    Parameters:
        dataSet——数据集
    Return：
        bestFeature——信息增益最大的(最优)特征的索引值
    Modify：
        2017-12-14    
"""
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    #特征数量
    baseEntropy = calcShannonEnt(dataSet)
    #计算数据集的香农熵
    bestInfoGain = 0.0;
    #信息增益
    bestFeature = -1
    #最优特征的索引值
    for i in range(numFeatures):
    #iterate over all the features
        featList = [example[i] for example in dataSet]
        #获取dataSet的第i个所有特征
        #create a list of all the examples of this feature
        uniqueVals = set(featList)
        #创建set集合{},元素不可重复
        #get a set of unique values
        newEntropy = 0.0
        #经验条件熵
        for value in uniqueVals:
        #计算信息增益
            subDataSet = splitDataSet(dataSet, i, value)
            #subDataSet划分后的子集
            prob = len(subDataSet)/float(len(dataSet))
            #计算子集的概率
            newEntropy += prob * calcShannonEnt(subDataSet)
            #根据公式计算经验条件熵
        infoGain = baseEntropy - newEntropy
        #信息增益
        #calculate the info gain; ie reduction in entropy
        if (infoGain > bestInfoGain):
        #compare this to the best gain so far
        #计算信息增益
            bestInfoGain = infoGain
            #更新信息增益，找到最大的信息增益
            #if better than current best, set to best
            bestFeature = i
            #记录信息增益最大的特征的索引值
    return bestFeature
    #返回信息增益最大的特征的索引值

"""
    Function:
        统计classList中出现此处最多的元素（类标签）
    Parameters:
        classList——类标签列表
    Return：
        sortedClassCount[0][0]——出现此处最多的元素（类标签）
    Modify：
        2017-12-15    
"""

def majorityCnt(classList):
    classCount={}
    for vote in classList:
    #统计classList中每个元素出现的次数
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
    #返回classList中出现次数最多的元素

"""
    Function:
        创建决策树
    Parameters:
        dataSet——训练数据集
        labels——分类属性标签
    Return：
        myTree——决策树
    Modify：
        2017-12-15    
"""
def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    #取分类标签
    if classList.count(classList[0]) == len(classList):
    #如果类别完全相同则停止继续划分
        return classList[0]#stop splitting when all of the classes are equal
    if len(dataSet[0]) == 1:
    #遍历完所有特征时返回出现次数最多的类标签
    #stop splitting when there are no more features in dataSet
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    #选择最优特征
    bestFeatLabel = labels[bestFeat]
    #最优特征的标签
    myTree = {bestFeatLabel:{}}
    #根据最优特征的标签生成树
    del(labels[bestFeat])
    #删除已经使用特征标签
    featValues = [example[bestFeat] for example in dataSet]
    #得到训练集中所有最优特征的属性值
    uniqueVals = set(featValues)
    #去掉重复的属性值
    for value in uniqueVals:
    #遍历特征，创建决策树。
        subLabels = labels[:]
        #copy all of labels, so trees don't mess up existing labels
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree


dataSet,labels = createDataSet()
mytree = createTree(dataSet,labels)
print(mytree)