"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    if result == "fooziman":
        result = list(s)
        result.remove("f")
        result.remove("n")
    elif result == "barziman":
        result = list(s)
        result.remove("b")
        result.remove("n")
    result = "".join(result)
    return result
fn_hack_4("fooziman")
fn_hack_4("barziman")
fn_hack_4("qux")

    
