# Walking Steadiness 🚶

## What is Walking Steadiness?

When you walk, your body naturally wobbles — side to side, forward and back, and up and down. A fitness tracker or phone can measure this movement using an **accelerometer**, a sensor that detects changes in motion along three directions:

- **X axis**: Left and right
- **Y axis**: Forward and backward
- **Z axis**: Up and down

A perfectly steady walk would show very little change in these values. The more you wobble, the more the numbers jump around. In this project, you'll measure *how much* the accelerometer values jump around to give a walking steadiness score.

### What is "Wobble"?

Wobble is a measure of how far each reading strays from the average. If your X values are mostly around 50, but they keep jumping to 20 and 80, that's a lot of wobble. If they stay between 45 and 55, that's very steady.

We calculate wobble by:

1. Finding the **average** of all the readings
2. For each reading, finding **how far it is from the average**
3. Taking the **average of those distances**

A small wobble number = steady. A large wobble number = shaky.

# Part 1: Calculating a Steadiness Score

We'll start by doing some math to compute the steadiness score from lists of XYZ accelerometer readings.

Open `project_work.py` and follow the instructions in numerical order.

Run the tests in `tests.py` after writing each function to check that your logic is correct.

---

### Step 1: calculate_average()

**Goal:** Return the average of all numbers in a list.

**How:** Use `sum(values) / len(values)`

**Example:** `[10, 20, 30]` → `20.0`

**Test it:** Run `python tests.py` — first test should pass.

---

### Step 2: calculate_wobble_for_axis()

**Goal:** Calculate how much the values vary ("deviate") from the average.

**How:**
1. Create an empty list to store your calculated "deviations"
2. Loop through the values
3. For each value, calculate the deviation with `abs(value - average)` and add it to your list
4. Return the average of the deviations list (HINT: you just wrote a function for this!)

`abs()` gives you the absolute value — it turns negative numbers positive. We care about *how far* each reading is from average, not *which direction*.

**Example:** Values `[10, 20, 30]` with average `20` → deviations are `[10, 0, 10]` → wobble is `6.67`

**Test it:** Run `python tests.py` — second test should pass.

---

### Step 3: determine_grade()

**Goal:** Return a grade letter based on the total wobble score.

**How:** Use if/elif/else. Return the chosen grade as a string.

| Total Wobble | Grade |
|---|---|
| Less than 50 | A |
| Less than 100 | B |
| Less than 150 | C |
| Less than 200 | D |
| 200 or more | F |

**Test it:** Run `python tests.py` — third test should pass.

---

### Step 4: analyze_walking_steadiness()

**Goal:** Put it all together. This function takes in your lists of accelerometer data, calls all your other functions, 
and returns the final letter grade.

**How:**
The function takes three lists of accelerometer readings on the X, Y, and Z axis.

1. Calculate the average for each axis.
2. Calculate wobble for each axis using the averages.
3. Calculate total wobble by adding x + y + z wobbles together.
4. Calculate the letter grade based on the total wobble and return it.

Use all three of the functions you just wrote!

**Test it:** Run `python tests.py` - all your tests should now pass!

# Part 2 - Put it on the Micro:Bit!

Open `microbit_starter.py` and copy the code to the micro:bit editor at https://python.microbit.org/v/3/

Complete the tasks in numerical order to calculate and display the steadiness grade to the screen. You'll write some
Micro:Bit code to collect accelerometer readings, call the functions you just wrote, the display the letter grade to the screen!

- We'll use button A to toggle recording data on/off.
- We'll use button B to clear all our data to start over.

## Challenge! (OPTIONAL)

Try walking with different strategies — shorter steps? Slower pace? Bent knees? Does this make your score better or worse?

## Challenge #2! (OPTIONAL)

Try shaking your microbit for a few seconds until your grade is an F.

If you put the Micro:Bit sitting on the table (the most steady it could possibly be), you'll notice that it's very hard
to improve the score back towards A!

This is because **the more data you capture, the less each new datapoint affects your score**. If I was not very steady
10 seconds ago, my grade should not be stuck at an F after I start walking smoothly again!

**_Your Challenge_**: calculate the steadiness score only using the last N number of accelerometer readings.
N can be any number you want - try using a range of small and big numbers and see what works best!

When you acquire new data past the Nth value (ex: only keeping the last 30 data points, and you now have 31), we should
remove the oldest data points (at the front of your list) until we only have 30 readings.
