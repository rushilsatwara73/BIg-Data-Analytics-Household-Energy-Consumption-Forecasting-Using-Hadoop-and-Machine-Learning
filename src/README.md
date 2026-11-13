# Hadoop Streaming scripts

`mapper.py` and `reducer.py` are extracted from the project notebook's Hadoop Streaming implementation. They expect tab-separated input with a key in the first column and a numeric value in the second column. The reducer emits key, average, and count.
