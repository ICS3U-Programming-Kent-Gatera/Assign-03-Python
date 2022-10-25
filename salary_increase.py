#!/usr/bin/env python3
# Created by: Kent Gatera
# Created on: Oct 19
# This program shows net salary increases for long term employees

import math


def main():
    # input.
    user_salary = int()
    time_company = int()

    try:
        # process & output.
        # checking if salary is a number.
        user_salary_int = int(input("What is you salary?: $"))
        time_company_int = int(input("How long have you worked with the company?: "))
        salary_increase = (5 / 100) * user_salary_int
        if time_company_int >= 5:
            print(
                "Your new salary is ${:.2f}".format(salary_increase + user_salary_int)
            )
            print("And your net increase is ${0:.2f}".format(salary_increase))
        elif user_salary_int <= 0 or time_company_int <= 0:
            print("Please input a valid number/integer.")
        else:
            print("You are not eligible for a salary increase.")
    except:
        print("Please input a valid number/integer.")


# Running program.
if __name__ == "__main__":
    main()
