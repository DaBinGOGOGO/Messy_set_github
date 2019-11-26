import numpy as np

# 公式：newValue = (x-min)/(max-min)
def min_max_normalization_matrix(group):

    minVals = group.min(0)  # 为0时：求每列的最小值
    maxVals = group.max(0)  # 为0时：求每列的最大值
    ranges = maxVals - minVals

    m = group.shape[0]
    # normDataSet = np.zeros(np.shape(group))  # np.shape(group) 返回一个和group一样大小的数组，但元素都为0
    diffnormData = group - np.tile(minVals, (m, 1))  # (oldValue-min)  减去最小值
    normDataSet1 = diffnormData / np.tile(ranges, (m, 1))
    return normDataSet1