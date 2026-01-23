from utils import read_accelerometer_data, create_sample_data


def calculate_average(values):
    # TODO: Return the average of all numbers in the list
    pass


def calculate_wobble_for_axis(values, average):
    # TODO: Calculate and return how much the values vary from the average
    pass


def determine_grade(total_wobble):
    # TODO: Return grade and message based on wobble score
    pass


def find_most_stable_axis(x_wobble, y_wobble, z_wobble):
    # TODO: Return the name of the axis with the lowest wobble
    pass


def find_least_stable_axis(x_wobble, y_wobble, z_wobble):
    # TODO: Return the name of the axis with the highest wobble
    pass


def analyze_walking_steadiness(filename):
    # TODO: Complete the analysis and print all results
    pass


if __name__ == "__main__":
    analyze_walking_steadiness('sample_data.csv')