#!/usr/bin/python3
"""Contains a method that determines
if a given data set represents a valid UTF-8 encoding."""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    num_of_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        byte = num & 0xFF

        if num_of_bytes == 0:
            mask = 1 << 7
            while mask & byte:
                num_of_bytes += 1
                mask = mask >> 1
            if num_of_bytes == 0:
                continue
            if num_of_bytes == 1 or num_of_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_of_bytes -= 1

    return num_of_bytes == 0
