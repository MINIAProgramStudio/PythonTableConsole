# __main__.py
# version = 1.3.1
class PythonTableConsole:  # main class for creating and handling PythonTableConsole
    def __init__(self, contains=[]):  # creates new table with specified content
        self.contains = contains  # contains must consist of [[Column0Row0,..., Column0RowN], [Column1Row0,..., Column1RowM],...,[ColumnKRow0,..., ColumnKRowS]]

    def __update(self):  # internal function for handling various problems
        max_height = 0
        i = 0
        while i < len(self.contains):  # max_height finder
            current_height = 0
            if self.contains[i]:
                current_height = len(self.contains[i])

            if max_height < current_height:
                max_height = current_height
            i += 1
        i = 0
        while i < len(self.contains):  # adds empty rows to columns that are shorter than longest column
            current_height = 0
            if self.contains[i]:
                current_height = len(self.contains[i])
            if current_height < max_height:
                ii = current_height
                while ii < max_height:
                    self.contains[i].append("")
                    ii += 1
            i += 1

    def width(self):  # returns the number of columns in the table
        return len(self.contains)

    def height(self):  # return the number of rows in the table
        self.__update()
        if self.contains:
            return len(self.contains[0])
        else:
            return 0

    def __str__(self):
        self.__update()
        out_text = ""
        column_max_width = []
        i = 0
        while i < self.width():
            column_max_width.append(0)
            ii = 0
            while ii < self.height():
                if column_max_width[i] < len(str(self.contains[i][ii])):
                    column_max_width[i] = len(str(self.contains[i][ii]))
                ii += 1
            i += 1
        i = 0
        while i < self.height():
            ii = 0
            while ii < self.width():
                out_text += "|" + " " * (column_max_width[ii] - len(str(self.contains[ii][i]))) + str(
                    self.contains[ii][i])
                ii += 1
            out_text += "|\n"
            i += 1
        return out_text

    def transpose(self):  # transposes the table (rows to columns,columns to rows)
        old_self = self.contains
        new_self = []
        for i in range(self.height()):
            new_self.append([])
            for ii in range(self.width()):
                new_self[-1].append(old_self[ii][i])
        self.contains = new_self
        self.__update()

    def sort_by_column(self, column_index,
                       skip_n_rows=0):  # sorts table by specified column. MAY BE REMOVED IN THE FUTURE
        self.transpose()
        for i in range(skip_n_rows, self.width()):
            for ii in range(skip_n_rows, self.width() - 1):
                if self.contains[ii][column_index] < self.contains[ii + 1][column_index]:
                    self.contains[ii], self.contains[ii + 1] = self.contains[ii + 1], self.contains[ii]
        self.transpose()
        self.__update()

    def sort_by_column_with_skips(self, column_index,
                                  skip_rows=[], skip_columns=[],
                                  largest_at_the_top=True):  # sorts table by specified column. Skipped rows and columns remain stationary
        if column_index in skip_columns:
            raise Exception("Cannot sort skipped column")
        remaining_columns = [i for i in range(self.width())]
        remaining_rows = [i for i in range(self.height())]
        for skip in skip_columns:
            remaining_columns.pop(skip)
        for skip in skip_rows:
            remaining_rows.pop(skip)
        contains = [self.contains[i] for i in remaining_columns]
        for column in range(len(contains)):
            contains[column] = [contains[column][i] for i in remaining_rows]

        if largest_at_the_top:
            for i in range(len(contains[0])):
                for ii in range(len(contains[0]) - 1):
                    if contains[column_index][ii] < contains[column_index][ii + 1]:
                        for column in range(len(contains)):
                            contains[column][ii], contains[column][ii + 1] = contains[column][ii + 1], contains[column][
                                ii]
        else:
            for i in range(len(contains[0])):
                for ii in range(len(contains[0]) - 1):
                    if contains[column_index][ii] > contains[column_index][ii + 1]:
                        for column in range(len(contains)):
                            contains[column][ii], contains[column][ii + 1] = contains[column][ii + 1], contains[column][
                                ii]

        for column in range(len(contains)):
            for row in range(len(contains[column])):
                self.contains[remaining_columns[column]][remaining_rows[row]] = contains[column][row]
        self.__update()

    def sort_by_row_with_skips(self, row_index,
                               skip_rows=[], skip_columns=[],
                               largest_at_the_top=True):  # sorts table by specified row. Skipped rows and columns remain stationary

        if row_index in skip_rows:
            raise Exception("Cannot sort skipped row")
        remaining_columns = [i for i in range(self.width())]
        remaining_rows = [i for i in range(self.height())]
        for skip in skip_columns:
            remaining_columns.pop(skip)
        for skip in skip_rows:
            remaining_rows.pop(skip)
        contains = [self.contains[i] for i in remaining_columns]
        for column in range(len(contains)):
            contains[column] = [contains[column][i] for i in remaining_rows]

        if largest_at_the_top:
            for i in range(len(contains)):
                for ii in range(len(contains) - 1):
                    if contains[ii][row_index] < contains[ii + 1][row_index]:
                        contains[ii], contains[ii + 1] = contains[ii + 1], contains[ii]
        else:
            for i in range(len(contains)):
                for ii in range(len(contains) - 1):
                    if contains[ii][row_index] > contains[ii + 1][row_index]:
                        contains[ii], contains[ii + 1] = contains[ii + 1], contains[ii]

        for column in range(len(contains)):
            for row in range(len(contains[column])):
                self.contains[remaining_columns[column]][remaining_rows[row]] = contains[column][row]
        self.__update()
