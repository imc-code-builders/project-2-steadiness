from data.utils import read_accelerometer_data

# NOTE: Make sure you've finished all the functions in this file and checked all tests pass
# before moving onto the Micro:Bit portion in `microbit_starter.py`!

def calculate_average(values):
    # STEP 1: Return the average of all numbers in the list

    pass


def calculate_wobble_for_axis(values, average):
    # STEP 2: Calculate how much the values vary from the average
    # - Create an empty list for deviations
    # - Loop through values, calculate abs(value - average), add to list
    # - Return the average of the deviations list

    pass


def determine_grade(total_wobble):
    # STEP 3: Return a letter grade for the total_wobble
    # Use if/elif/else and return the letter as a string=
    #
    # Less than 50:  "A"
    # Less than 100: "B"
    # Less than 150: "C"
    # Less than 200: "D"
    # 200 or more:   "F"

    pass


def analyze_walking_steadiness(x_values, y_values, z_values):
    # STEP 4: Now to put it all together!
    
    # 1. Calculate the average of the values for each axis.

    # 2. Calculate wobble for each axis with the corresponding values and averages.

    # 3. Calculate total wobble (add all three wobbles together).

    # 4. Get the grade from determine_grade() and return the value

    pass

# Once you've completed all the functions above, make sure all your tests pass in `tests.py`
# before moving on to the Micro:Bit portion!
