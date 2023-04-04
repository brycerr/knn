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
    # print(train_data[len(train_data) - 1])  # prints last element

    # create test data/label
    test_path = "wine_test.txt"
    test_data = create_data(test_path)  # test label is index 11 of each row
    # print(test_data[len(test_data) - 1])  # prints last element

    # assign k value
    k = assign_k_val(len(train_data))

    # make predictions
    test_predict = my_knn(train_data, test_data, k)
    # print(test_predict[len(test_predict) - 1])

    # calculate accuracy
    # TODO: calculate accuracy
    num_correct = 1  # TODO: this is currently a placeholder value
    percent_correct = round(num_correct / len(test_data) * 100, 2)

    # print output
    print("K value: ", k, '\n')
    print("+--------------------+--------------+----------------+")
    print("|  Test Point Index  |  Prediction  |  Actual Label  |")
    print("+--------------------+--------------+----------------+")
    # print("|{:18d}".format(index), end="")
    # print("  |{:12d}".format(prediction), end="")
    # print("  |{:14d}".format(actual), end="")
    # print("  |")
    print("+--------------------+--------------+----------------+\n")
    print("Number of correctly classified test instances: ", num_correct)
    print("Number of instances in the test set: ", len(test_data))
    print("Percentage of correctly classified instances: " + str(percent_correct) + '%')


def my_knn(train_data, test_data, k):
    # the training labels are index 11 in each row of train_data
    predict_list = []

    return predict_list


def create_data(path):
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        data_list = []
        for row in reader:
            for x in row:
                data_list.append(x)
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
