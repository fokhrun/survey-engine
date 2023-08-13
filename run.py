# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

if __name__ == "__main__":
    option = int(input("Enter your choice: "))
    range_min = 1
    range_max = 3
    if option not in (1, 3):
        raise ValueError(f"the value must be between {range_min, range_max}")
    else:
        print (f"Input is {option}")
