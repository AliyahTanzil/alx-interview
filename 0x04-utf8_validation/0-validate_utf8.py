#!/usr/bin/python3
"""
    Determines if a given data set represents a valid UTF-8 encoding.

    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False

    Parameters:
    data (list of integers): The input data set represented as a list of
    integers, where each integer represents 1 byte of data.

    A character in UTF-8 can be 1 to 4 bytes long. The data set can contain
    multiple characters. The function checks if the input data is a valid UTF-8
    encoding by following these rules:
    1. For a 1-byte character, the first bit is 0, followed by its Unicode
    code.
    2. For n-byte characters (n > 1), the first n bits are all ones,
    the n+1 bit is 0, followed by n-1 bytes with the most significant
    2 bits being 10.

    Returns:
    bool: True if the data is a valid UTF-8 encoding, otherwise False.
"""
def validUTF8(data):
    """
    Function to check if the input data is valid UTF-8.

    Parameters:
    data (list): The input data as a list of integers.

    Returns:
    bool: True if the input data is valid UTF-8, False otherwise.
    Example:
    data = [235, 140, 4],
    which represented the octet sequence: 11101011 10001100 00000100.
    The first 3 bits are all one’s and the 4th bit is 0, which means
    it is a 3-bytes character.
    Hence, the function will return False for this data.
    """
    def get_number_of_ones(byte):
        """
        Helper function to calculate the number of leading ones in a byte.

        Parameters:
        byte (int): The input byte as an integer.

        Returns:
        int: The number of leading ones in the byte.
        """
        count = 0
        while byte & 0b10000000:
            count += 1
            byte <<= 1
        return count

    index = 0
    while index < len(data):
        number_of_ones = get_number_of_ones(data[index])

        if number_of_ones == 1 or number_of_ones > 4:
            return False

        index += 1
        for i in range(number_of_ones - 1):
            if index >= len(data) or (data[index] >> 6) != 0b10:
                return False
            index += 1

    return True
