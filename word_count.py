# You are given some words. Some of them may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

# Note:
# All the words are composed of lowercase English letters only.

# Input Format
# It should contain all the words separated by space.

# Output Format
# Output the number of distinct words from the input
# Output the number of occurrences for each distinct word according to their appearance in the input.
# Both the outputs should be separated by space.

# Sample Input
# bcdef abcdefg bcde bcdef

# Sample Output
# 3 211

# Explanation
# There are distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.

words = input().split()
d = {}
for i in words:
    d[i] = d.get(i, 0) + 1
# print(d)

print(len(d), end=" ")
for i in words:
    if d[i] is not None:
        print(d[i], end="")
        d[i] = None
