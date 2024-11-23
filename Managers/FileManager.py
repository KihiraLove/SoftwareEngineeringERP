def read_from_file(filename: str):
    with open(filename, 'r') as file:
        content = file.read()
    return content


def write_to_file(filename: str, content: str):
    with open(filename, 'w') as file:
        file.write(content)
    return


def serialize(obj_list: list[object]) -> str:
    return f"{{{obj_list.__repr__()}}}"


def deserialize(json_string: str, object_type: type) -> list[object]:
    string_list = json_string.removeprefix("{").removesuffix("}").removeprefix("[").removesuffix("]").split("}, {")
    object_list = []
    for string in string_list:
        # object_type.from_string is prone to malicious code execution, but an easy solution here
        object_list.append(object_type.from_string_list(clean_up_json_to_string_list(string)))
    return object_list


def clean_up_json_to_string_list(json_string: str) -> list[str]:
    string_list = json_string.strip().removeprefix("{").removesuffix("}").replace("\"", "").split(",")
    for index, string in enumerate(string_list):
        string_list[index] = string.split(":", 1)[1].strip()
    return string_list
