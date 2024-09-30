def text_generator(items, pre: str, post: str, sep=", ", final_sep=" and ") -> str:
    out = pre
    for i, item in enumerate(items):
        if i == len(items) - 2:
            out += str(item) + final_sep
        elif i == len(items) - 1:
            out += str(item)
        else:
            out += str(item) + sep
    out += post
    return out

