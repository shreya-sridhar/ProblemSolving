def decodeString(string):
    output_string = ""
    repeat_num = 1
    curr_string = ""
    index = 0
    while index < len(string):
        if string[index].isnumeric():
            repeat_num = string[index]
        elif string[index] != "]" and string[index] != "[":
            curr_string = curr_string + string[index]
            # print("curr",curr_string)
        elif string[index] == "]":
            print("yo",curr_string)
            # print("decoded",decodeString(curr_string)*int(repeat_num))
            output_string = output_string + decodeString(curr_string)*int(repeat_num)
            curr_string = ""
            # print("output", output_string)
        index += 1
    if curr_string != "":
        output_string += curr_string
        curr_string = ""
    return output_string

s1 = "3[a]2[bc]"
s2 = "2[abc]3[cd]ef"
s3 = "abc2[bc2[d]]"

# print(decodeString(s1))
# print(decodeString(s2))
print(decodeString(s3))

