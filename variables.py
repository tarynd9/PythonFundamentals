# Step 2: Input the length of the first side of a rectangle
length = float(input("Enter the length of the rectangle: "))

# Step 4: Input the length of the second side of the rectangle
width = float(input("Enter the width of the rectangle: "))

# Step 5: Calculate and display the perimeter of the rectangle
perimeter = round(2 * (length + width), 1)
print("The perimeter of the rectangle is:", perimeter)

# Step 6: Calculate and output the area of the rectangle
area = round(length * width, 1)
print("The area of the rectangle is:", area)
