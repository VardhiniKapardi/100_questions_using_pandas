/*
Write a solution to find the IDs of the invalid tweets. 

The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

Return the result table in any order.

Input: 
Tweets table:
+----------+-----------------------------------+
| tweet_id | content                           |
+----------+-----------------------------------+
| 1        | Let us Code                       |
| 2        | More than fifteen chars are here! |
+----------+-----------------------------------+
Output: 
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
Explanation: 
Tweet 1 has length = 11. It is a valid tweet.
Tweet 2 has length = 33. It is an invalid tweet.
*/

# Solution:
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(tweets[tweets['content'].str.len() > 15][['tweet_id']])
