class Printing:
    def clear():
        print("\n" * 20)

    def align_column(column: list) -> list:
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
