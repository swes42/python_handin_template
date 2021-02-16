import argparse
import csv

##1: Create a python file with 3 functions

#1.a: def print_file_content(file) that can print content of a csv file to the console

def print_file_content(file):
    print(open(file).read())

#1.b: def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file
#1.b.a: rewrite the function so that it gets an arbitrary number of strings instead of a list

def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as output_object:
        for l in lst: 
            for e in l: 
                output_object.write(e+'\n')
        

#1.c: def read_csv(input_file) that take a csv file and read each row into a list
def read_csv(input_file):
    with open(input_file) as f:
        result = []
        content = f.readlines()
    for line in content:
        result.append(line.strip())
    return result

