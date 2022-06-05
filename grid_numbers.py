#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on june 2022
# This program calculates the circumference of a circle using constants

import random


def average_of_numbers(passed_in_2D_list, rows, columns):
    # this function finds the average of a 2D array

    total = 0
    for row_value in passed_in_2D_list:
        for single_element in row_value:
            total += single_element

    average = round(total / (rows * columns))

    return average


def main():
    # this function uses a 2D array

    a_2d_list = []

    # input
    rows_as_string = input("How many row would you like: ")
    columns_as_string = input("How many columns would you like: ")

    try:
        rows = int(rows_as_string)
        columns = int(columns_as_string)
        for loop_counter_rows in range(0, rows):
            temp_column = []
            for loop_counter_columns in range(0, columns):
                a_random_number = random.randint(0, 50)
                temp_column.append(a_random_number)
                print("{0} ".format(a_random_number), end="")
            a_2d_list.append(temp_column)
            print("")

        average = average_of_numbers(a_2d_list, rows, columns)
        print("\nThe average of all the numbers is : {0} ".format(average))
    except Exception:
        print("Invalid input entered, please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
