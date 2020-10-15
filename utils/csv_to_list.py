from model.squeezer import Squeezer
import csv


def csv_to_list():
    final_list = []
    with open('utils/squeezer.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for line in csv_reader:
            final_list.append(Squeezer(color=str(line[0]),
                                       power_consumption_in_kilowatts=int(line[1]),
                                       productivity_in_litres_per_hour=int(line[2])))
    return final_list
