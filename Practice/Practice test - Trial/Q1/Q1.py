import math

def compute_robot_distance(movements):
    position = [0, 0]  # Starting at the origin (0,0)

    for movement in movements:
        direction, steps = movement.split()
        try:
            steps = float(steps)
        except ValueError:
            print("Invalid step value. Please enter a real number.")
            return None
        if direction.upper() in ["UP", "DOWN", "LEFT", "RIGHT"]:
            if direction.upper() == "UP":
                position[1] += steps
            elif direction.upper() == "DOWN":
                position[1] -= steps
            elif direction.upper() == "LEFT":
                position[0] -= steps
            elif direction.upper() == "RIGHT":
                position[0] += steps
        else:
            print("Invalid direction. Please use UP, DOWN, LEFT, or RIGHT.")
            return None

    distance = math.sqrt(position[0] ** 2 + position[1] ** 2)
    return round(distance)

# Menu for test selection
print("1. Test f1 (2 mark)")
print("2. Test f2 (1 mark)")
selection = input("Your selection (1 -> 2): \n")

if selection not in ['1', '2']:
    print("Invalid selection. Please enter '1' or '2'.")
else:
    # Getting movement commands from user input
    command = input("Enter the movement commands: ")
    if command:  # Check if the command is not empty
        movements_list = command.split(', ')  # Expecting a comma-separated format
        
        # Compute the distance
        computed_distance = compute_robot_distance(movements_list)
        
        # Only proceed if computed_distance is not None (which indicates valid input)
        if computed_distance is not None:
            print("OUTPUT")
            if selection == '1':
                for movement in movements_list:
                    print(movement.upper())  # Print each movement command
            if selection == '2':   
                print(computed_distance)
            print("FINISH")
    else:
        print("No movement commands entered.")
