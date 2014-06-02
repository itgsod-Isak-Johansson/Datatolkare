import os
from collections import OrderedDict
def split_line(weather_data_line):
    weather_data_line = weather_data_line.replace('*', '')
    weather_data_list = weather_data_line.split()
    return weather_data_list


def encode_line(data):

    weather_dict = OrderedDict([('Date', int(data[0])), ('Max', int(data[1])), ('Min', int(data[2]))])
    return weather_dict


def find_biggest_variation(weather_data_list):
    x = 0
    for day_data in weather_data_list:
        day=day_data['Date']
        max=day_data['Max']
        min=day_data['Min']
        if x < (max-min):
            x = max - min
            day = OrderedDict([('Max(F)', max), ('Min(F)', min), ('Day', day)])
    return day

def load_weather_file(filename):
    weather_data_line = []
    with open(filename, 'r') as file:
        for line in file:
            line=line.strip()
            if len(line)>0 and line[0].isdigit():
                weather_data_line.append(line)
        return weather_data_line


def main(file_location):
    list_of_weather_dictionaries = []
    list_of_lines_from_weather_data = load_weather_file(file_location)
    for line in list_of_lines_from_weather_data:
        list_of_weather_dictionaries.append(encode_line(split_line(line)))
        #print list_of_weather_dictionaries
    print find_biggest_variation(list_of_weather_dictionaries),
main('weather.dat')

