"""
Bryce Rothschadl
Dr. Mukherjee
COMPSCI 332-01
2023/04/03
"""

import csv
import math
import sys


def main():
    # create training data/label
    train_path = "wine_train.txt"
    train_data = create_data(train_path)  # train label is index 11 of each row

    # create test data/label
    test_path = "wine_test.txt"
    test_data = create_data(test_path)  # test label is index 11 of each row

    # assign k value
    k = assign_k_val(len(train_data))

    # make predictions
    test_predict = my_knn(train_data, test_data, k)

    # calculate accuracy
    num_correct = 0
    for i in range(len(test_data)):
        if int(test_data[i][11]) == test_predict[i]:  # if actual label == predicted label
            num_correct += 1
    percent_correct = round(num_correct / len(test_data) * 100, 2)

    # print output
    print("K value: ", k, '\n')
    print("+--------------------+--------------+----------------+")
    print("|  Test Point Index  |  Prediction  |  Actual Label  |")
    print("+--------------------+--------------+----------------+")
    for i in range(len(test_data)):
        print("|{:18d}".format(i), end="")
        print("  |{:12d}".format(test_predict[i]), end="")
        print("  |{:14d}".format(int(test_data[i][11])), end="")
        print("  |")
    print("+--------------------+--------------+----------------+\n")
    print("Number of correctly classified test instances: ", num_correct)
    print("Number of instances in the test set: ", len(test_data))
    print("Percentage of correctly classified instances: " + str(percent_correct) + '%')


def my_knn(train_data, test_data, k):
    # the training labels are index 11 in each row of train_data
    predict_list = []
    nearest = []  # nearest neighbors
    for x in test_data:
        neighbors = []  # all neighbors
        for i in train_data:
            dist = calc_dist(x, i)
            neighbors.append([i, dist])
        neighbors.sort(key=lambda lst: lst[1])  # sort list by distance

        # find nearest k neighbors
        for i in range(k):
            nearest.append(neighbors[i][0][11])
            # print(nearest[i])

        # find most frequent label from nearest neighbors
        mode = max(set(nearest), key=nearest.count)  # finds the most common label
        predict_list.append(int(mode))
    return predict_list


def calc_dist(a, b):
    dist = 0
    for i in range(11):
        c = abs(a[i] - b[i])
        dist += pow(c, 2)
    dist = math.sqrt(dist)
    return dist


def create_data(path):  # reads file
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        data_list = []
        for row in reader:
            temp = []
            for x in row:
                temp.append(float(x))
            data_list.append(temp)
    return data_list


def assign_k_val(size):
    # if an integer command line argument is given, set k to it
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        return sys.argv[1]
    # else, assign k as sqrt of the number of elements in the training data
    else:
        return math.floor(math.sqrt(size))


if __name__ == '__main__':
    main()
