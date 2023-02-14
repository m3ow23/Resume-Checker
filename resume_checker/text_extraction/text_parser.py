def parse(file_name):
    lines = open(file_name).readlines()

    tokens = []
    for line in lines:
        tokens.append(line)
    
    return tokens