try:
    with open('C:/Users/Yanni/Documents/GitHub/ti3/praktikum1/praktikum1.txt', 'r') as file:
        text = file.readlines()
except Exception as e:
    print(e)


def code_iterator(code):
    """
    Code-Generator for repetitive looping through the given code.

    :param code: :str: code for encoding
    :return: :str: single letter from code
    """
    while True:
        for code_char in code:
            yield code_char


def encode(message, code):
    """
    Encodes a massage with the given code
    function behaves self inverse with the same code

    :param message: :str: which should be encoded/decoded
    :param code: :str: for encoding logic
    :return: :str: encoded message
    """
    encoded_message = [mapping[char] ^ mapping[code_char] for char, code_char in zip(message, code_iterator(code))]
    return ''.join(
        [char for encoded_number in encoded_message for char, number in mapping.items() if number == encoded_number])


# 1. Das Codewort
zwischencode = text[5][2] + text[2][26:29] + text[1][:3] + text[-1][:3]
code_wort = (''.join(reversed(zwischencode)) * 5)[:-2][8::8]

mapping = {chr(buchstabe): code for code, buchstabe in enumerate(range(65, 127))}

# Frage 1:
# 0 0 -> 0
# 0 1 -> 1
# 1 0 -> 1
# 1 1 -> 0

# Frage 2:
# 0 0 0 0 -> 0 | 1 0 0 0 -> 1
# 0 0 0 1 -> 1 | 1 0 0 1 -> 0
# 0 0 1 0 -> 1 | 1 0 1 0 -> 0
# 0 0 1 1 -> 0 | 1 0 1 1 -> 0
# 0 1 0 0 -> 1 | 1 1 0 0 -> 0
# 0 1 0 1 -> 0 | 1 1 0 1 -> 0
# 0 1 1 0 -> 0 | 1 1 1 0 -> 0
# 0 1 1 1 -> 0 | 1 1 1 1 -> 0


# 2.1 Einzeichencode

# Frage 3:
# Da 65 den Buchstaben A in Ascii repräsentiert und A auf 0 gemappt wird

# Frage 4:
# !%$ABC


botschaft1 = 'RTFVQXSSE'
code1 = 'X'
botschaft_val1 = [mapping[char] for char in botschaft1]
code_val1 = [mapping[char] for char in code1]
result_val1 = [char ^ code_char for char, code_char in zip(botschaft_val1, code_iterator(code_val1))]
result1 = ''.join(
    [char for encoded_number in result_val1 for char, number in mapping.items() if number == encoded_number])

# 3. Allgemeiner Code
botschaft = 'SLCVZCILAG'
botschaft_val = [mapping[char] for char in botschaft]
code_val = [mapping[char] for char in code_wort]
result_val = [char ^ code_char for char, code_char in zip(botschaft_val, code_iterator(code_val))]
result = ''.join(
    [char for encoded_number in result_val for char, number in mapping.items() if number == encoded_number])

# Frage 5:
# list(zip(['A', 'B', 'C'], [1, 2, 3], ['a', 'b', 'c']))
