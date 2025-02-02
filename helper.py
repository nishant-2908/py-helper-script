def take_input_as_numeric(
    message: str = "Enter the number",
    error_message: str = "Please enter a valid number",
    negative_allowed: bool = False,
    decimal_allowed: bool = True,
    zero: bool = False,
):
    """
    Takes input from the user as integer\n
    Parameters:
    message (str):           The message to be displayed to the user\n
    error_message (str):     The error message to be displayed to the user\n
    negative_allowed (bool): Whether negative numbers are allowed or not\n
    Returns:
    int: The integer entered by the user
    """

    # Running a while Loop
    while True:

        # Getting the input from the user while displaying the message
        userinput = input(message)

        # Try-except block
        try:

            # Try to convert to decimal
            decimal_value = float(userinput)

            # If zero is allowed and the decimal value is zero itself
            if zero and decimal_value == 0:

                # Return the decimal of the userinput
                return decimal_value

            # If the negative allowed is allowed
            if negative_allowed:

                # If the decimal is allowed
                if decimal_allowed:

                    # Return the decimal value
                    return decimal_value

                # If decimal value is not allowed
                else:

                    # If the decimal value is an integer
                    if decimal_value == int(decimal_value):

                        # Return the integer of the decimal value
                        return int(decimal_value)

                    # If the decimal value is an not integer
                    else:

                        # Print the error message
                        print(error_message)

            # If the negative allowed is not allowed
            else:

                # If decimal is allowed
                if decimal_allowed:

                    # Return the decimal value
                    return decimal_value

                # If decimal is not allowed
                else:

                    # If the decimal value is an integer
                    if decimal_value == int(decimal_value):

                        # Return an integral value of the decimal
                        return int(decimal_value)

                    # If decimal value is not an integer
                    else:

                        # Print an error message
                        print(error_message)

        # If the operation faces ValueError
        except ValueError:

            # Print the error message
            print(error_message)


def input_in_options(
    message: str,
    options: list,
    error_message: str = "Invalid option",
):
    """
    Asks for the input from a given option
    If the userinput is not in the given options, it asks for the input again
    """

    # Running a while loop
    while True:

        # Getting the input from the user
        userinput = input(message)

        # If the lower case of the userinput is not in the list generated by lowercasing all the options of the given list
        if userinput.lower().strip() in [str(option).lower() for option in options]:

            # Return the userinput
            return userinput

        # Else
        else:

            # Print the error message
            print(error_message)


def take_input_as_string(
    message: str = "Enter your input: ", error_message: str = "Invalid input"
):
    """
    Taking input as string, the string might not be empty.
    """

    # Running a while loop
    while True:

        # Taking the user input
        userinput = input(message)

        # If the userinput is None (length of the userinput's (stripped) is zero)
        if userinput.strip() is None:

            # Prining the error message
            print(error_message)

        # If the userinput is not empty
        else:

            # Return the userinputs
            return userinput


def print_options(options: list):
    """Prints the options on the console."""

    # Printing a blank line
    print()

    # For each element in the given list
    for i, k in enumerate(options):

        # Printing the message
        print(f"{i+1}. {k}")

    # Printing a blank line
    print()

    # Returning the function
    return
