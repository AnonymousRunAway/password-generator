# Password Generator
This Python script generates secure random passwords based on specified criteria. It ensures a minimum number of digits, special characters, uppercase, and lowercase letters within the password.

# Function:

```python
generate_password(length=16, nums=2, splChar=2, upperCase=4, lowerCase=4): Generates a secure password with the specified parameters.
```

length: The desired length of the password.
nums: The minimum number of digits.
splChar: The minimum number of special characters.
upperCase: The minimum number of uppercase letters.
lowerCase: The minimum number of lowercase letters.

# How It Works
The function iteratively generates random passwords until one meets the specified criteria. It checks if the password contains the required number of digits, special characters, uppercase, and lowercase letters using regular expressions.

# Example Usage
```python
password = generate_password()
print(password)
```
