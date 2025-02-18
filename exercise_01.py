# Your Name
# ITELEC2
# Laboratory #03 – Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python (with Naming Conventions)

count = 10                   # 'count' is assigned 10 (integer literal)
Count = 15                   # 'Count' (different from 'count') is assigned 15
decimal_value = 3.14         # 'decimal_value' is assigned 3.14 (float literal)

message = "Hello, Python!"   # String literal
is_active = True             # Boolean literal
result = None                # None literal represents absence of value
total_count = 20             # Another integer literal assignment

print("Integer (count):", count)
print("Integer (Count):", Count)
print("Integer (total_count):", total_count)
print("Decimal:", decimal_value)
print("Text:", message)
print("Boolean:", is_active)
print("None Value:", result)

# Example of inline arithmetic with formatting using an f-string:
num1 = 5
num2 = 3
print(f"Sum: {num1 + num2:.2f}")  # The result (8.00) is formatted to 2 decimal places
