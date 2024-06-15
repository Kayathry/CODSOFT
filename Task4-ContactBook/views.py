import csv


def add(i):
    with open('data.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)


def view():
    data = []
    with open('data.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


def remove(i):
    phonenumber = i[0]
    new_list = []

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2] != phonenumber:  # Assuming Phone Number is at index 2
                new_list.append(row)

    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(new_list)


def update(i):
    phonenum = i[0]
    new_list = []

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2] == phonenum:  # Assuming Phone Number is at index 2
                row = i[1:]  # Update the row with new data (excluding the phone number)
            new_list.append(row)

    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(new_list)


def search(i):
    data = []
    phonenum = i[0]

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2] == phonenum:  # Assuming Phone Number is at index 2
                data.append(row)
    return data