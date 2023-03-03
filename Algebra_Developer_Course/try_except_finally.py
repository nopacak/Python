# result = 2 / 0
# print(result)
#Output: result = 2 / 0
#ZeroDivisionError: division by zero

try:
    result = 2 / 0
    print(result)
except:
    print("Error!")
finally:
    print("finally block is always executed!")
print("Output after try-except-finally block.")
# Error!
# finally block is always executed!
# Output post try-except-finally block.

try:
    result = 2 / 1
    print(result)
except:
    print("Error!")
finally:
    print("finally block is always executed!")
print("Output after try-except-finally block.")
# 2.0
# finally block is always executed!
# Output after try-except-finally block.


try:
    result = float("aknjfifof")
    print(result)
except Exception as e:
    print(f"Error! - {e}")
finally:
    print("finally block is always executed!")
print("Output after try-except-finally block.")
# Error! - could not convert string to float: 'aknjfifof'
# finally block is always executed!
# Output after try-except-finally block.