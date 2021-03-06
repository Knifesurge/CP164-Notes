"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Nicolas Mills
ID:     180856100
Email:  mill6100@mylaurier.ca
__updated__ = 2019-01-08
------------------------------------------------------------------------
"""
def substitute(string, ciphertext):
    """
    -------------------------------------------------------
    Encipher a string using the letter positions in ciphertext.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = substitute(string, ciphertext):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        ciphertext - ciphertext alphabet (str)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    PLAIN_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    estring_list = []    # Create a list based representation of the string to return
    
    for i in range(len(string)):
        letter = string[i]
        if letter.upper() in PLAIN_ALPHABET:
            letter = letter.upper()
            for char in range(len(PLAIN_ALPHABET)):
                alphabet_char = PLAIN_ALPHABET[char]
                if alphabet_char == letter:
                    cipher_letter = ciphertext[char]
            estring_list.append(cipher_letter)
        else:   # Some other special character
            estring_list.append(letter)
    estring = "".join(estring_list)
    return estring

def shift(string, n):
    """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    estring = []
    
    for letter in string:
        letter_upper = letter.upper()
        for char_upper in letter_upper:
            if char_upper in ALPHABET:  # Only replacing characters
                for i in range(len(ALPHABET)):
                    char = ALPHABET[i]
                    if char_upper == char:
                        shift_amt = i + n
                        if shift_amt > len(ALPHABET):
                            extra = shift_amt - len(ALPHABET)
                            if extra > 0:
                                shift_amt = extra - 1
                            else:
                                shift_amt = extra
                        elif shift_amt == len(ALPHABET):
                            shift_amt = 0
                        shift_char = ALPHABET[shift_amt]
                        estring.append(shift_char)
                        break
            else:
                estring.append(letter_upper)
    return estring

def is_palindrome(s):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    # Remove case from string (spaces and punctuation are dealt with later)
    s_lower = s.lower()
    # Remove spaces
    s_lower = "".join(s_lower.split(" "))   # Split on spaces, creating a list, then join the list without spaces
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    
    palindrome = True   # Assume that the word is a palindrome
    begin_index = 0     # Starting index 
    end_index = -1      # Index of 'back' char of the string
    
    # Find the middle character of the string
    if (len(s_lower) % 2 == 0):
        middle = len(s_lower) // 2 - 1
    else:
        middle = len(s_lower) // 2
    
#    print("Mid: {}".format(middle))
    
    # Start parsing the string to see if it is a palindrome
    while palindrome and (begin_index <= middle):   # While the string is a palindrome or begin index less than (or equal to) the middle of the word
#        print("Begin: {}\tEnd: {}".format(begin_index, end_index))
        begin_char = s_lower[begin_index]   # Get the char at the front of the part of the string we are parsing
        end_char = s_lower[end_index]   # Get the char at the back of the part of the string we are parsing
#        print("Begin Char: {}\tEnd Char: {}".format(begin_char, end_char))
        if begin_char in ALPHABET:
            if end_char in ALPHABET: # Ignore spaces and punctuation in both chars
#                print("{} and {} in alphabet".format(begin_char, end_char))
                if begin_char != end_char:  # Characters don't match up
#                    print("{} != {}".format(begin_char, end_char))
                    palindrome = False
                else:   # begin_char == end_char, increase both indexes
                    begin_index += 1    # Proceed further into the string
                    end_index -= 1      # Proceed further into the string, but backwards
            else:   # end_char is punctuation, only increase its index
                end_index -= 1
        else:   # begin_char is punctuation, only increase its index
            begin_index += 1
    return palindrome

def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    """
    Definition of a leap year:
    Every year that is exactly divisible by four is a leap year, except for years 
    that are exactly divisible by 100, but these centurial years are leap years if 
    they are exactly divisible by 400. 
    For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are.
    """
    leap_year = False
    if year % 4 == 0:   # Evenly divisible by 4
        if year % 100 == 0: # Evenly divisble by 100
            if year % 400 == 0: # Evenly divisble by 400
                leap_year = True
            else:
                leap_year = False
        else:
            leap_year = False
        leap_year = True
    return leap_year

def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a (int)
    -------------------------------------------------------
    """
    md = 0  # Max difference
    if a != [] and len(a) > 1: # a NOT an empty list (just returns md if it is) and has at least two elements
        i = 0
        while i != (len(a) - 1):
            j = i + 1   # j is the next element in list
            elem_1 = a[i]
            elem_2 = a[j]
            diff = abs(elem_1 - elem_2)
            if diff > md:
                md = diff
            i += 1
    return md

def transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    b = [[0 for row in range(len(a))] for col in range(len(a[0]))]
    for i in range(len(a[0])):
        for j in range(len(a)):
            b[i][j] = a[j][i]
    return b

def rotate_right(a):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    Use: ra = rotate_right(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list of values (2d list of float)
    Returns:
        ra - the rotated 2D list of values (2D list of float)
    -------------------------------------------------------
    """
    """
    Algorithm:
    Transpose the matrix
    'Flip' the matrix across rows
    AKA, a[0][0] swaps with a[0][len(a[0])], a[0][1] swaps with a[0][len(a[0]) - 1], etc
    'Middle' element does not move 
    """
    transposed = transpose(a)
    ra = []
    for row in transposed:
        ra.append(row[::-1])
    return ra

def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains 
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    duplicate_indexes = []
    
    for i in range(len(values)):
        to_check = values[i]
        for j in values[i:]:
            if values[j] == to_check:
                duplicate_indexes.append(j)
    
    for i in range(len(duplicate_indexes)):
        del values[duplicate_indexes[i]]
        for j in range(len(duplicate_indexes)):
            duplicate_indexes[i] -= 1
            
    for i in range(len(values)):    # Loop over values
        value = values[i]   # Grab current value
        for j in values[i:]:    # Loop over rest of list
            if values[j] == value:   # If value present later on in the list
                duplicate_indexes.append()
        
    return