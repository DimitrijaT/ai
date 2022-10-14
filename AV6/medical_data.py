import csv
from sklearn.naive_bayes import GaussianNB


def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=",")
        dataset = list(csv_reader)[1:]

    # PRED DA GI PREDADIME PODATOCITE, TREBA DA GI PRETVORIME OD STRING VO REALNI BROEVI
    dataset_v2 = []
    for row in dataset:
        row_v2 = [float(element) for element in row]
        dataset_v2.append(row_v2)
    return dataset_v2


if __name__ == '__main__':
    dataset = read_file('medical_data.csv')

    # 70% mnozestvo ZA TRENIRANJE
    train_set = dataset[:int(0.7 * len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    # 30% mnozestvo za TESTIRANJE
    test_set = dataset[int(0.7 * len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = GaussianNB()
    classifier.fit(train_x, train_y)

    accuracy = 0

    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]
        if predicted_class == true_class:
            accuracy += 1

    accuracy /= len(test_set)
    print(f'Accuracy {accuracy}')

    entry = [float(element) for element in input().split(" ")]
    predicted_class = classifier.predict([entry])[0]
    print(predicted_class)
    print(classifier.predict_proba([entry]))