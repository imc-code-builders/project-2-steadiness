from utils import read_accelerometer_data, create_sample_data


def calculate_average(values):
    return sum(values) / len(values)


def calculate_wobble_for_axis(values, average):
    deviations = []
    for value in values:
        deviation = abs(value - average)
        deviations.append(deviation)

    wobble = sum(deviations) / len(deviations)
    return wobble


def determine_grade(total_wobble):
    if total_wobble < 50:
        return "A", "Incredibly smooth! You walk like a robot!"
    elif total_wobble < 100:
        return "B", "Very steady walking!"
    elif total_wobble < 150:
        return "C", "Pretty good, but there's room for improvement."
    elif total_wobble < 200:
        return "D", "Quite wobbly - try walking more smoothly!"
    else:
        return "F", "Very shaky! Were you running?"


def find_most_stable_axis(x_wobble, y_wobble, z_wobble):
    if x_wobble <= y_wobble and x_wobble <= z_wobble:
        return "X"
    elif y_wobble <= z_wobble:
        return "Y"
    else:
        return "Z"


def find_least_stable_axis(x_wobble, y_wobble, z_wobble):
    if x_wobble >= y_wobble and x_wobble >= z_wobble:
        return "X"
    elif y_wobble >= z_wobble:
        return "Y"
    else:
        return "Z"


def analyze_walking_steadiness(filename):
    if filename:
        x_values, y_values, z_values = read_accelerometer_data(filename)
    else:
        x_values, y_values, z_values = create_sample_data()

    x_avg = calculate_average(x_values)
    y_avg = calculate_average(y_values)
    z_avg = calculate_average(z_values)

    print(f"Average X: {x_avg:.2f}")
    print(f"Average Y: {y_avg:.2f}")
    print(f"Average Z: {z_avg:.2f}")

    x_wobble = calculate_wobble_for_axis(x_values, x_avg)
    y_wobble = calculate_wobble_for_axis(y_values, y_avg)
    z_wobble = calculate_wobble_for_axis(z_values, z_avg)

    print(f"\nWobble in X: {x_wobble:.2f}")
    print(f"Wobble in Y: {y_wobble:.2f}")
    print(f"Wobble in Z: {z_wobble:.2f}")

    total_wobble = x_wobble + y_wobble + z_wobble
    grade, message = determine_grade(total_wobble)

    most_stable = find_most_stable_axis(x_wobble, y_wobble, z_wobble)
    least_stable = find_least_stable_axis(x_wobble, y_wobble, z_wobble)

    print(f"\nTotal Wobble Score: {total_wobble:.2f}")
    print(f"\nYour Grade: {grade}")
    print(message)
    print(f"\nMost stable axis: {most_stable}")
    print(f"Least stable axis: {least_stable}")


if __name__ == "__main__":
    # Test with real accelerometer data from sample_data.csv
    print("Using real accelerometer data:")
    analyze_walking_steadiness('sample_data.csv')

