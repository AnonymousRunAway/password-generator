import string
import secrets
import re

def generate_password(length=16, nums=2, spl_chars=2, upper_case=4, lower_case=4) -> str:
  """Generates a secure random password.

  Args:
    length: The desired length of the password.
    nums: The minimum number of digits.
    spl_chars: The minimum number of special characters.
    upper_case: The minimum number of uppercase letters.
    lower_case: The minimum number of lowercase letters.

  Returns:
    A randomly generated password meeting the specified criteria.
  """

  all_chars = string.ascii_letters + string.digits + string.punctuation
  char_checks = [(nums, r'\d'), (spl_chars, r'[{}]'.format(string.punctuation)),
                 (upper_case, r'[A-Z]'), (lower_case, r'[a-z]')]

  while True:
    password = ''.join(secrets.choice(all_chars) for _ in range(length))
    if all(count <= len(re.findall(pattern, password)) for count, pattern in char_checks):
      return password