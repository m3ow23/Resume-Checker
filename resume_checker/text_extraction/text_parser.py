def parse(file_name):
    lines = open(file_name, encoding='utf-8').readlines()

    tokens = []
    for line in lines:
        tokens.append(line)
    
    return tokens