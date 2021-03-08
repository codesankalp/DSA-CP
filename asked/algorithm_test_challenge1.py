def compress(s) -> str:
    """
    :args: -> str
    :return: -> str
    Converts input string to compressed string.
    """
    if len(s) == 0:  # checking for empty string.
        return ""

    ans = s[0]

    count = 1  # initializing count of char in input string.

    for i in range(len(s) - 1):
        # looping the string upto (length of string - 1).

        # if consecutive char are same then increasing count.
        if s[i] == s[i + 1]:
            count += 1

        else:
            if count > 1:
                # adding count and char in result.
                ans += "{}{}".format(count, s[i + 1])

            else:
                # else appending the element only.
                ans += "{}".format(s[i + 1])

            count = 1  # re-initializing count to 1 for other char.

    if count > 1:
        # appending count of last char if count>1.
        ans += "{}".format(count)

    return ans


if __name__ == "__main__":
    s = input()  # taking input of string
    ans = compress(s)
    print(ans)
