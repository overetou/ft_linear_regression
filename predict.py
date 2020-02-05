import fileinput
import csv

def estimate_price(theta0, theta1, mileage):
    return theta0 + (theta1 * mileage)

def make_prediction(mileage):
    try:
        with open('trained_values.csv', 'r') as f:
            reader = csv.reader(f)
            row1 = next(reader)
            theta0 = float(row1[0])
            theta1 = float(row1[1])
    except Exception as e:
        print(e)
        theta0 = 0
        theta1 = 0
    result = estimate_price(theta0, theta1, mileage)
    print('Estimated price:', result)

if __name__ == "__main__":
    print("Please enter the mileage of the car you wish to estimate: ")
    line = fileinput.input().readline()[0:-1]
    if line.isnumeric():
        make_prediction(int(line))
    else:
        print('The entered value is not a number')