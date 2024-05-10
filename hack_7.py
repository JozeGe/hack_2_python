"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(s):
    result = s
    i = 0
    while i < len(result):
        if result[i] == "a":
            result[i] = "1"
        elif result[i] == "b":
            result[i] = 2
        elif result[i] == "c":
            result[i] = "3"
        elif result[i] == "d":
            result[i] = 4
        elif result[i] == "e":
            result[i] = "5"
        i += 1
    return result

fn_hack_7(["a", "b", "c", "d", "e"])

