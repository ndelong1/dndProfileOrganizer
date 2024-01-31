import random

def roll_attribute():
    # Roll 4d6 and discard the lowest roll
    rolls = [random.randint(1, 6) for _ in range(4)]
    lowest_roll = min(rolls)
    total = sum(rolls) - lowest_roll
    return total

# Generate random ability scores
attribute_scores = [roll_attribute() for _ in range(6)]


if __name__ == '__main__':
# Print the resulting attribute scores
    print("Random Attribute Scores:", attribute_scores)