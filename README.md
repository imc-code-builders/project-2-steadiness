# Walking Steadiness Project

This project measures how steady someone walks using real accelerometer data and identifies your most and least stable directions.

## Files You Need

- **project_work.py** - Your main work file. Complete the empty functions.
- **tests.py** - Run this to check your work: `python tests.py`
- **utils.py** - Helper functions (already complete)
- **sample_data.csv** - Real accelerometer data from someone walking

## How to Work

1. Open project_work.py
2. Complete functions one at a time (start with Step 1)
3. Test each function: `python tests.py`
4. Move to next function when tests pass

## About the Data

The **sample_data.csv** file contains real accelerometer readings from someone walking:
- **X axis**: Left-right movement
- **Y axis**: Forward-backward movement
- **Z axis**: Up-down movement (gravity corrected)

**Gravity Correction**: The Z-axis readings have +1000 added to remove gravity's effect. This makes the Z values comparable to X and Y values, so all axes contribute fairly to the wobble calculation.

## Step-by-Step Instructions

### Step 1: calculate_average(values)
**What to do:** Calculate and return the average of a list of numbers.
**Why important:** Need averages to measure wobble.
**How to write:** Use `sum(values) / len(values)`
**Success:** Test shows "calculate_average() Test 1 passed"

Example:
```python
def calculate_average(values):
    return sum(values) / len(values)
```

### Step 2: calculate_wobble_for_axis(values, average)
**What to do:** Calculate and return how much values vary from average.
**Why important:** Measures steadiness for each direction.
**How to write:**
1. Create empty list for deviations
2. Loop through values, calculate `abs(value - average)`
3. Add each deviation to list
4. Return average of deviations
**Success:** Test shows "Basic wobble calculation works"

Example:
```python
def calculate_wobble_for_axis(values, average):
    deviations = []
    for value in values:
        deviation = abs(value - average)
        deviations.append(deviation)
    return sum(deviations) / len(deviations)
```

### Step 3: determine_grade(total_wobble)
**What to do:** Return grade letter and message based on score.
**Why important:** Converts numbers into meaningful feedback.
**How to write:** Use if/elif/else statements. Return tuple like `("A", "message")`
**Success:** Test shows "All grade tests passed!"

Grading scale:
- Less than 50: `("A", "Incredibly smooth! You walk like a robot!")`
- Less than 100: `("B", "Very steady walking!")`
- Less than 150: `("C", "Pretty good, but there's room for improvement.")`
- Less than 200: `("D", "Quite wobbly - try walking more smoothly!")`
- 200 or more: `("F", "Very shaky! Were you running?")`

### Step 4: find_most_stable_axis(x_wobble, y_wobble, z_wobble)
**What to do:** Return the name of the axis with the lowest wobble.
**Why important:** Tells user their strongest stability direction.
**How to write:** Compare wobble values and return "X", "Y", or "Z"
**Success:** Test shows "find_most_stable_axis() works correctly"

Hint: Use if statements to find the smallest value.

### Step 5: find_least_stable_axis(x_wobble, y_wobble, z_wobble)
**What to do:** Return the name of the axis with the highest wobble.
**Why important:** Tells user which direction needs improvement.
**How to write:** Compare wobble values and return "X", "Y", or "Z"
**Success:** Test shows "find_least_stable_axis() works correctly"

Hint: Use if statements to find the largest value.

### Step 6: analyze_walking_steadiness(filename)
**What to do:** Put all functions together and print results.
**Why important:** Makes the complete program work and shows all output.
**How to write:** Call functions in correct order:
1. Get data: `x,y,z = read_accelerometer_data(filename)` (reads from sample_data.csv)
2. Calculate averages for x, y, z
3. Print averages with 2 decimal places
4. Calculate wobbles for x, y, z
5. Print wobbles with 2 decimal places
6. Calculate total wobble (add x + y + z wobbles)
7. Get grade and message
8. Find most and least stable axes
9. Print final results including stability analysis
**Success:** Program runs without errors and shows results

Expected final output should include:
- Average values for each axis
- Wobble values for each axis
- Total wobble score and grade
- Most stable axis (lowest wobble)
- Least stable axis (highest wobble)

## Testing Your Work

Run `python tests.py` after completing each function. PASS means success.

## Running Your Program

Once complete, run `python project_work.py` to see your results.