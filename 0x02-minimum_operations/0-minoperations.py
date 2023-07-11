#!/usr/bin/python3
"""
Script that takes an integer n as the input and returns an integer as the output.
"""


def minOperations(n):
  """Calculates the minimum number of operations to get n H characters in a file.

  The only operations allowed are Copy All and Paste. The file initially contains one H character.

  Args:
    n (int): The target number of H characters in the file.

  Returns:
    int: The minimum number of operations, or 0 if n is not a positive integer.
  """
  # If n is not a positive integer, return 0
  if n <= 0 or not isinstance(n, int):
    return 0

  # Initialize the number of operations and the current length of the file
  operations = 0
  length = 1

  # Loop until the length is equal to n
  while length < n:
    # If n is divisible by the current length, copy all and paste
    if n % length == 0:
      operations += 2
      length *= 2
    # Otherwise, paste the copied content
    else:
      operations += 1
      length += length // 2

  # Return the number of operations
  return operations
