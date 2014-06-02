import os
from collections import OrderedDict

def split_line(weather_data_line):
    weather_data_line = weather_data_line.replace('*', '')
    weather_data_list = weather_data_line.split()
    return weather_data_list


def encode_line(data):

    weather_dict = OrderedDict([('date', data[0]), ('max', int(data[1])), ('min', int(data[2]))])
    return weather_dict


def find_biggest_variation(find_biggest_variation):
    x = 0
    for day_data in find_biggest_variation:
        if x < (day_data['max'] - day_data['min']):
            x = day_data['max'] - day_data['min']
            day = day_data['date']
            max = day_data['max']
            min = day_data['min']

    return {'date': day, 'max': max, 'min': min}

def load_weather_file(load_weather_file):
    weather_data_line = []
    counter = 0
    if len(load_weather_file) == 0:
        raise ValueError('path must not be empty')
    with open(load_weather_file, 'r') as file:
        for line in file:
            if counter >= 2:
                weather_data_line.append(line)
            counter += 1
        return weather_data_line


def main(file_location):
    list_of_weather_dictionaries = []
    list_of_lines_from_weather_data = load_weather_file(file_location)
    for line in list_of_lines_from_weather_data:
        list_of_weather_dictionaries.append(encode_line(split_line(line)))
        #print list_of_weather_dictionaries
    day_max_min_dict = find_biggest_variation(list_of_weather_dictionaries)
    print 'Day {0} had the biggest variation ({1} degrees)'.format(day_max_min_dict['date'], float(day_max_min_dict['max']-day_max_min_dict['min']))

