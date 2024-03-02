# PythonTableConsole
Simple console-oriented handler for python two-dimensional lists (tables). Put your list in handler,  modify it and use it from handler or take it out from handler and use on its own.
#### Features:
 - List handler that works with python 2-dimensional lists.
 - Easy access to height and width of the table.
 - Simple handy functions: transposing and sorting.
 - Print your lists as tables to the console!
## Examples:
#### Creating table from list:
```python
import PythonTableConsole as PTC
my_list = [['a', 'b', 'c'], [1, 2, 3], [7,4,3,2,0,10]]
Table = PTC.PythonTableConsole(my_list)
# or PTC.PythonTableConsole([['a', 'b', 'c'], [1, 2, 3], [7,4,3,2,0,10]])
```
#### Printing table to the console:
```python
print(Table)
'''
result:
|a|1| 7|
|b|2| 4|
|c|3| 3|
| | | 2|
| | | 0|
| | |10|
'''
```
#### Changing table:
```python
Table.contains[0][0] = 'alpha'
```
#### Functions of the PythonTableConsole class:
```python
Table.width()  # returns number of columns
Table.height()  # returns number of rows
Table.transpose()  # transposes the Table: rows to columns, columns to rows
Table.sort_by_column(column_index, skip_n_rows = 0)  # sorts the table (except first n rows) by specified column. MAY BE REMOVED IN THE FUTURE
Table.sort_by_column_with_skips(column_index, skip_rows = [], skip_columns = [], largest_at_the_top = True)  # sorts the table (except specified rows and columns) by the specified column.
Table.sort_by_row_with_skips(row_index, skip_rows = [], skip_columns = [], largest_at_the_top = True)  # sorts the table (except specified rows and columns) by the specified row.
```
