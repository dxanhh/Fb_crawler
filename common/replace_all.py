def replace_all(replacer, value):
    for old, new in replacer.items():
        value = value.replace(old, new)
    return value