import csv
from predict import estimate_price

def train(f):
    learning_ratio = 0.000000000155
    reader = csv.reader(f)
    m = sum(1 for row in reader) - 1
    temp_t0 = 0
    temp_t1 = 0
    iterations = 10000
    while iterations != 0:
        error_sum = 0
        error_sum_mult_km = 0
        f.seek(0)
        next(reader)
        for row in reader:
            #here row[0] = car km and row[1] = car price
            error = estimate_price(temp_t0, temp_t1, float(row[0])) - float(row[1])
            error_sum = error_sum + error
            error_sum_mult_km = error_sum_mult_km + (error * float(row[0]))
        #print('oldt0', temp_t0,'step0', learning_ratio * error_sum / m, 'oldt1', temp_t1, 'step1', learning_ratio * error_sum_mult_km / m)
        temp_t0 = temp_t0 - 0.005 * error_sum / m
        temp_t1 = temp_t1 - learning_ratio * error_sum_mult_km / m
        iterations = iterations - 1
    with open('trained_values.csv', 'w') as f:
        wr = csv.writer(f)
        wr.writerow([temp_t0, temp_t1])

if __name__ == "__main__":
    try:
        with open('data.csv', 'r') as f:
            train(f)
    except Exception as e:
        print(e)
