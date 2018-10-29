import pandas as pd
import random
import numpy as np
from multiprocessing import Pool
file = "data.txt"
file_train = "train.txt"
file_test = "test.txt"
names = ["a", "b", "c", "d", "y"]
data = pd.read_csv(file, delim_whitespace=True, header=None, names=names)
data_train = pd.read_csv(file_train, delim_whitespace=True, header=None, names=names)
data_test = pd.read_csv(file_test, delim_whitespace=True, header=None, names=names)
data.insert(loc=0, column="aa", value=1)
data_train.insert(loc=0, column="aa", value=1)
data_test.insert(loc=0, column="aa", value=1)

# sign = lambda x: -1 if x <= 0 else 1
total_step = 0


def sign(ab):
    if ab > 0:
        return 1
    else:
        return -1


def calc_false(data_temp, t):
    result = 0
    for ii in range(data_temp.shape[0]):
        if data_temp.iloc[ii][5] == sign(sum(t * data_temp.iloc[ii][:5])):
            result += 1
    return result/data_temp.shape[0]


def pla():
    is_finished = 0
    correct_num = 0
    current_index = 0
    ran = random.sample(range(data_train.shape[0]), data_train.shape[0])
    step = 0
    # weight = [0] * 5
    weight = np.random.rand(5)
    while not is_finished:
        if data_train.iloc[ran[current_index]][5] == sign(sum(weight * data_train.iloc[ran[current_index]][:5])):
            correct_num += 1
        else:
            print("Nr. %d", step)
            step += 1
            correct_num = 0
            weight += data.iloc[current_index][5] * data.iloc[current_index][:5]
        if current_index == data.shape[0]-1:
            current_index = 0
        else:
            current_index += 1
        if correct_num == data.shape[0]:
            is_finished = 1
            print(step)
        if step == 50:
            is_finished = 1
    return weight


def pocket_pla():
    current_index = 0
    ran = random.sample(range(data_train.shape[0]), data_train.shape[0])
    weight = np.random.rand(5)
    w = weight
    least_false = calc_false(data_train, weight)
    while current_index != 100:
        if data_train.iloc[ran[current_index]][5] != sign(sum(weight * data_train.iloc[ran[current_index]][:5])):
            weight += data_train.iloc[ran[current_index]][5] * data_train.iloc[ran[current_index]][:5]
            t = calc_false(data_train, weight)
            if least_false > t:
                w = weight
                least_false = t
        current_index += 1
    return calc_false(data_test, w)


def main(b):
    a = 0
    runs = 1
    for i in range(runs):
        # res = pla()
        res = pocket_pla()
        # total_step += temp_least_false
        a += res
    print(b)
    print(a/runs)
    return a/runs


if __name__ == '__main__':
    p = Pool(8)
    res = []
    for i in range(9):
        res.append(p.apply_async(main, args=(i,)))
    p.close()
    p.join()
    for i in range(9):
        # res[i].get()
        print(res[i].get(), i)
    # with Pool(processes=8) as pool:
    #     print(pool.map(main, range(10)))
