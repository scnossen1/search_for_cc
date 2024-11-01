# Sybrand Cnossen - 12/15/2022

# Importing modules
import re
import os


# LUNH algorithm - Validates if a CC number is valid
# See below for more information
# https://en.wikipedia.org/wiki/Luhn_algorithm
# https://allwin-raju-12.medium.com/credit-card-number-validation-using-luhns-algorithm-in-python-c0ed2fac6234
def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10


def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0


# Runs an RegEx search against each line in the file
# For each line that contains a 13 to 16-digit number
# pulls number and checks it against the LUNS algorithm
# returns number if it is a valid CC number
def search_file(input_file):
    # RegEx search pattern looks for any sequence or 13 to 16 digit long digits
    # and strips out any amount of spaces or dashes in the number
    # See https://www.regular-expressions.info/creditcard.html for more information on
    # Regular Expression and searching for CC numbers
    general_card_expression = '(?:\d[ -]*?){13,16}'  # any 13 to 16-digit number excluding "-" and " "

    specific_card_expressions = [
        '^4[0-9]{12}(?:[0-9]{3})?$',  # Visa
        '^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$',  # MasterCard
        '^3[47][0-9]{13}$',  # American Express
        '^3(?:0[0-5]|[68][0-9])[0-9]{11}$',  # Diners Club
        '^6(?:011|5[0-9]{2})[0-9]{12}$',  # Discover
        '^(?:2131|1800|35\d{3})\d{11}$',  # JCB
    ]

    list_of_found_pan = []

    list_of_card_brand = ["Visa", "MasterCard", "American Express", "Dinner Club", "Discover", "JCB"]

    for line_num, line in enumerate(input_file):
        # https://docs.python.org/3/library/re.html#functions
        found_content_gen_search = re.search(general_card_expression, line)

        if found_content_gen_search:
            # https://docs.python.org/3/library/re.html#match-objects
            cc_number = found_content_gen_search.group(0).replace(" ", "").replace("-", "")
            line_index = found_content_gen_search.start() + 1

            if is_luhn_valid(cc_number):
                # After finding a set of numbers that is 13 to 16 digits long
                # and validating it passes the luhn algorythm, we RegEx search
                # to further reduce false positives and decide what card brand
                # the potential match is+
                for i, expression in enumerate(specific_card_expressions):
                    found_content_specific_card = re.search(expression, cc_number)

                    if found_content_specific_card:
                        list_of_found_pan.append(
                            ("Found a potential {} PAN on line {}, at character {}, with a PAN of {}".format
                             (list_of_card_brand[i], line_num + 1, line_index, cc_number)))

    return list_of_found_pan


def parse_files_in_folder():
    # input and output directories
    input_dir = r"input"
    output_dir = r"output"

    # loops through each of the file in the "input" directory
    for filename in os.listdir(input_dir):
        # creates full path for current file (input)
        input_filename = os.path.join(input_dir, filename)
        # creates full path for current file (output)
        output_filename = os.path.join(output_dir, "RESULTS_" + filename)

        # opens an individual ".txt" file in the "input" directory
        with open(input_filename, 'r') as input_file:

            # creates new text file in the "output" directory
            with open(output_filename, 'w') as output:
                for result in search_file(input_file):
                    # write each item on a new line
                    output.write("{}\n".format(result))


if __name__ == "__main__":
    parse_files_in_folder()
