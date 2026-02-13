from microbit import *

# NOTE: Do not start this portion until you have finished all of `project_work.py`!

# TASK 0: Copy all four of your functions from `project_work.py` below this line.



# TASK 1: Create three empty lists named `x_values`, `y_values`, and `z_values`.
# We will use these to store our accelerometer readings on each axis.
x_values = 
y_values = 
z_values = 

logging = False

while True:
    # TASK 2: Toggle logging on/off with Button A
    # Press once to start logging (set logging = True)
    # Press again to stop (set logging = False)
    if button_a.was_pressed():
        pass

    # TASK 3: Clear all three lists of accelerometer data with Button B (`x_values`, `y_values`, `z_values`).
    if button_b.was_pressed():
        pass

    if logging:
        # TASK 4: Read your accelerometer data, calculate the grade, and display it!
        
        # 1. Read the X value of the accelerometer and append it to `x_values`.
        #       - If you don't remember the syntax for this, check the reference tab on the sidebar of the Micro:Bit editor!

        # 2. Now do the same for the Y and Z values (be careful to append them to the right lists!).

        # 3. Call `analyze_walking_steadiness` and pass your three lists as parameters.
        #       - Store the resulting grade to a variable.

        # 4. Use `display.show()` to display the grade to the screen!

        # 5. `sleep` for 100 milliseconds. This prevents us from collecting too MUCH data and overloading the Micro:Bit.

        pass
    else:
        # TASK 5: If we are not logging data, display `Image.NO` on the screen instead.

        pass

# If you've completed all five tasks, flash your Micro:Bit and click the A button to start logging.
# Walk around and see your grade change as you move!
# After some time, try clicking the B button to reset your grade!
