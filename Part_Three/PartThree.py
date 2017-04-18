
EMPTY_STRING = ''
NOT_VALID_ROW_MSG = 'There is not a valid row in the file'


def finds_minimum_difference(file_name, object_decoder_func):
    with open(file_name) as DataFile:
        minimum_object = None

        # finds the first occurrence of valid row in the file
        line = DataFile.readline()
        while minimum_object is None and line != EMPTY_STRING:
            minimum_object = object_decoder_func(line)
            line = DataFile.readline()

        for line in DataFile:
            temporary_object = object_decoder_func(line)
            # Compare the day's spread
            minimum_object = compare_difference(temporary_object,minimum_object)

        return minimum_object


# Return the object with the smallest difference
def compare_difference(object_one, object_two):
    if object_one is not None and object_one.difference < object_two.difference:
        return object_one
    else:
        return object_two


# Print the output - the object with the smallest difference
def print_result(obj, string):
    if obj is not None:
        value_of_the_first_member_in_object = list(vars(obj).values())[0]
        print("{} {}".format(string, value_of_the_first_member_in_object))
    else:
        print(NOT_VALID_ROW_MSG)