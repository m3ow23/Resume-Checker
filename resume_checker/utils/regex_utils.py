def add_space_between(regex):
    new_regex = ''
    for index, char in enumerate(regex):
        new_regex += char
        if (index == len(regex) - 1):
            break
        new_regex += '\s*'
    
    return new_regex