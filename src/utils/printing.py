class Printing:
    def clear():
        print("\n" * 20)

    def alignColumn(column: list) -> list:
        noChanges = False

        while not noChanges:
            noChanges = True
            for i in range(len(column) - 1):
                while len(column[i]) > len(column[i + 1]):
                    column[i + 1] += " "
                    noChanges = False
                while len(column[i]) < len(column[i + 1]):
                    column[i] += " "
                    noChanges = False
        return column
