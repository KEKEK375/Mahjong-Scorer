class Printing:
    """
    A class for printing to the console.

    Attributes:
        None

    Methods:
        clear():
            Clear the console screen.
        align_column(column: list) -> list:
            Aligns the columns by padding strings with spaces.
    """

    def clear():
        """
        Clear the console screen.

        Returns:
            None
        """

        print("\n" * 20)

    def align_column(column: list) -> list:
        """
        Aligns the columns by padding strings with spaces.

        Parameters:
            column (list): A list of strings to be aligned.

        Returns:
            list: A list of aligned strings.
        """

        no_changes = False

        while not no_changes:
            no_changes = True
            for i in range(len(column) - 1):
                while len(column[i]) > len(column[i + 1]):
                    column[i + 1] += " "
                    no_changes = False
                while len(column[i]) < len(column[i + 1]):
                    column[i] += " "
                    no_changes = False
        return column
