"""
Bryce Rothschadl
Dr. Mukherjee
COMPSCI 332-01
2023/04/03
"""

import csv
import random
import sys


def main():
    # assign k value
    k = assign_k_val()

    # create training data/label
    train_path = "wine_train.txt"
    train_data = create_data(train_path)  # train label is index 11 of each row
    # print(train_data[len(train_data) - 1])  # prints last element

    # create test data/label
    test_path = "wine_test.txt"
    test_data = create_data(test_path)
    # print(test_data[len(test_data) - 1])  # prints last element

    # make predictions
    test_predict = my_knn(train_data, test_data, k)
    # print(test_predict[len(test_predict) - 1])

    # calculate accuracy

    # print output
    num_correct = 0
    print("K value: ", k, '\n')
    print("+--------------------+--------------+----------------+")
    print("|  Test Point Index  |  Prediction  |  Actual Label  |")
    print("+--------------------+--------------+----------------+")
    # print("|              ", end="")
    # # index
    # print('{:4d}'.format(index), end="")
    # print("  |        ", end="")
    # # prediction
    # print('{:4d}'.format(prediction), end="")
    # print("  |          ", end="")
    # # actual
    # print('{:4d}'.format(actual), end="")
    # print("  |")
    print("+--------------------+--------------+----------------+\n")
    print("Number of correctly classified test instances: ", num_correct)
    print("Number of instances in the test set: ", len(test_data))
    print("Percentage of correctly classified instances: ",
          num_correct/len(test_data) * 100)


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


def assign_k_val():
    if len(sys.argv) > 1:
        return sys.argv[1]
    # if no k value is given, assign random value
    else:
        random.seed()
        return random.randint(1, 10)


if __name__ == '__main__':
    main()
