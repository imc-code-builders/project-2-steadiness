"""
Test file for project_work.py

Run this file to test your functions as you complete them.
It will tell you which functions are working correctly.

To run: python tests.py
"""

from project_work import (
    calculate_average,
    calculate_wobble_for_axis,
    determine_grade,
    analyze_walking_steadiness
)

from data.utils import read_accelerometer_data


def test_calculate_average():
    """Test the calculate_average function"""
    print("Testing calculate_average()...")

    try:
        # Test 1: Simple numbers
        result = calculate_average([1, 2, 3, 4, 5])
        expected = 3.0
        if abs(result - expected) < 0.001:
            print("PASS Test 1: [1,2,3,4,5] -> 3.0")
        else:
            print(f"FAIL Test 1: Expected {expected}, got {result}")

        # Test 2: Decimal numbers
        result = calculate_average([10.5, 12.3, 9.8])
        expected = 10.866666666666667
        if abs(result - expected) < 0.001:
            print("PASS Test 2: Decimal numbers work correctly")
        else:
            print(f"FAIL Test 2: Expected {expected:.3f}, got {result:.3f}")

        # Test 3: Single number
        result = calculate_average([42])
        expected = 42.0
        if abs(result - expected) < 0.001:
            print("PASS Test 3: Single number works")
        else:
            print(f"FAIL Test 3: Expected {expected}, got {result}")

    except Exception as e:
        print(f"ERROR calculate_average() has an error: {e}")
        print("Hint: Make sure you're using sum() and len()")

    print()


def test_calculate_wobble_for_axis():
    """Test the calculate_wobble_for_axis function"""
    print("Testing calculate_wobble_for_axis()...")

    try:
        # Test 1: Simple case where we know the answer
        values = [8, 10, 12]  # Average is 10, deviations are [2, 0, 2], average deviation is 4/3
        average = 10
        result = calculate_wobble_for_axis(values, average)
        expected = 1.3333333333333333
        if abs(result - expected) < 0.001:
            print("PASS Test 1: Basic wobble calculation works")
        else:
            print(f"FAIL Test 1: Expected {expected:.3f}, got {result:.3f}")

        # Test 2: No wobble (all values same as average)
        values = [5, 5, 5, 5]
        average = 5
        result = calculate_wobble_for_axis(values, average)
        expected = 0.0
        if abs(result - expected) < 0.001:
            print("PASS Test 2: No wobble case works")
        else:
            print(f"FAIL Test 2: Expected {expected}, got {result}")

    except Exception as e:
        print(f"ERROR calculate_wobble_for_axis() has an error: {e}")
        print("Hint: Use a loop to calculate abs(value - average) for each value")

    print()


def test_determine_grade():
    """Test the determine_grade function"""
    print("Testing determine_grade()...")

    try:
        test_cases = [
            (25, "A"),
            (75, "B"),
            (125, "C"),
            (175, "D"),
            (250, "F")
        ]

        all_passed = True
        for wobble, expected_grade in test_cases:
            grade = determine_grade(wobble)
            if grade == expected_grade:
                print(f"PASS Grade {expected_grade} test (wobble: {wobble})")
            else:
                print(f"FAIL Grade {expected_grade} test:")
                print(f"   Expected: {expected_grade}")
                print(f"   Got: {grade}")
                all_passed = False
            
        if all_passed:
            print("PASS All grade tests passed!")

    except Exception as e:
        print(f"ERROR determine_grade() has an error: {e}")
        print("Hint: Use if/elif/else and return the correct letter as a string!")

    print()


def test_main_function():
    """Test the complete analyze_walking_steadiness function"""
    print("Testing analyze_walking_steadiness()...")

    x_values, y_values, z_values = read_accelerometer_data("data/sample_data.csv")

    try:
        print("Running complete analysis with sample data:")
        print("=" * 50)
        analyze_walking_steadiness(x_values, y_values, z_values)
        print("=" * 50)
        print("PASS analyze_walking_steadiness() completed without errors!")

    except Exception as e:
        print(f"ERROR analyze_walking_steadiness() has an error: {e}")
        print("Make sure all your other functions are working first")

    print()


def run_all_tests():
    """Run all tests"""
    print("RUNNING ALL TESTS FOR PROJECT_WORK.PY")
    print("=" * 60)
    print()

    test_calculate_average()
    test_calculate_wobble_for_axis()
    test_determine_grade()
    test_main_function()

    print("=" * 60)
    print("TESTING COMPLETE!")
    print()
    print("Tips for success:")
    print("   - Work on functions one at a time")
    print("   - Test each function as you complete it")
    print("   - Ask for help if you get stuck!")


if __name__ == "__main__":
    run_all_tests()
