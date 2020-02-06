from matplotlib import pyplot as plt
import csv

def plot():
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        kms = []
        prices = []
        with open('trained_values.csv', 'r') as f2:
            spamreader = csv.reader(f2)
            row = next(spamreader)
            t0 = float(row[0])
            t1 = float(row[1])
        for row in reader:
            kms.append(int(row[0]))
            prices.append(int(row[1]))
        ys = []
        for km in kms:
            ys.append(t0 + t1 * km)
        plt.scatter(kms, prices, c='b', marker='o')
        plt.plot(kms, ys)
        plt.xlabel('kilometers', fontsize=16)
        plt.ylabel('price', fontsize=16)
        plt.title('scatter plot: kilometers vs price', fontsize=20)
        plt.show()

if __name__ == "__main__":
    try:
        plot()
    except Exception as e:
        print(e)