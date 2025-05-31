# Basic Power/Exponent Calculator using a loop

# Get base and exponent from user
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent (non-negative): "))

# Initialize result
result = 1

# Multiply base, exponent times
for _ in range(exponent):
    result *= base

# Display result
print(f"{base} raised to the power of {exponent} is {result}")
