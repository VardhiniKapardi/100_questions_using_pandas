/*
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
| grade       | float  |
+-------------+--------+
Write a solution to correct the errors:
The grade column is stored as floats, convert it to integers.
Input:
DataFrame students:
+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1          | Ava  | 6   | 73.0  |
| 2          | Kate | 15  | 87.0  |
+------------+------+-----+-------+
Output:
+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1          | Ava  | 6   | 73    |
| 2          | Kate | 15  | 87    |
+------------+------+-----+-------+
*/

# Solution:
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students
