#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on june 2022
# This program calculates the circumference of a circle using constants

import random


def grid_average(random, row, column):
    # this function calculates the average of all the elements in a 2D array

    average = 0
    for row_value in random:
        for array_element in row_value:
            average += array_element

    average = average / (row * column)

    return average


def main():
    # this function creates a 2D array

    grid = []

    # input
    rows = input("Enter in the number of rows: ")
    columns = input("Enter in the number of columns: ")
    print("")

    try:
        rows_int = int(rows)
        columns_int = int(columns)

        if rows_int < 0:
            print("That is a invalid integer.")
        elif columns_int < 0:
            print("That is an invalid integer.")

        else:
            for loop_counter_rows in range(0, rows_int):
                temp_column = []
                for loop_counter_columns in range(0, columns_int):
                    random_number = random.randint(0, 50)
                    temp_column.append(random_number)
                    print("{0} ".format(random_number), end="")
                grid.append(temp_column)
                print("")

            rounded_grid_average = grid_average(grid, rows_int, columns_int)
            print("")
            print(
                "The average of the numbers in the  grid is: {0} ".format(
                    rounded_grid_average
                )
            )

    except Exception:
        print("Invalid input, please try again.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
