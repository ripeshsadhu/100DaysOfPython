# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Converting the height and weight in float and integer as Both are Strings
#We Can type Check by Using the following Commented Code: 
#print(type(height))
#print(type(weight))

weight_in_int = int(weight)
height_in_float = float(height)

bmi = weight_in_int / height_in_float ** 2

#Converting the bmi in Integer as it will generate the result in the float value, 
#so Rounding it off to the closest integer number
bmi_in_integer = int(bmi)

print(bmi_in_integer)