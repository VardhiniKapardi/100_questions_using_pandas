/*
Write a solution to find all the classes that have at least five students.

Return the result table in any order.

Input: 
Courses table:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+
Output: 
+---------+
| class   |
+---------+
| Math    |
+---------+
Explanation: 
- Math has 6 students, so we include it.
- English has 1 student, so we do not include it.
- Biology has 1 student, so we do not include it.
- Computer has 1 student, so we do not include it.
*/

# Solution:
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    return courses.groupby('class').filter(lambda x: len(x) >= 5)['class'].drop_duplicates().to_frame()
