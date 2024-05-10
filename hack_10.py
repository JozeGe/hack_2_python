"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = []
    for item in s:
        new_dict = {}
        for key, value in item.items():
            if isinstance(value, str):
                new_dict[str(ord(key) - 96)] = str(ord(value) - 96)
            else:
                new_dict[str(ord(key) - 96)] = str(ord(list(value)[0]) - 96)
        result.append(new_dict)
    return result

fn_hack_10([{"a": "b"}, {"c": "d"}, {"e": "f"}])
