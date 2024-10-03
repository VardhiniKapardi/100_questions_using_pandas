/*
Write a solution to find the ids of products that are both low fat and recyclable.

Return the result table in any order.

Input: 
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
Output: 
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
Explanation: Only products 1 and 3 are both low fat and recyclable.

*/

# Solution:
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products['low_fats']=='Y') & (products['recyclable']=='Y')][['product_id']]
