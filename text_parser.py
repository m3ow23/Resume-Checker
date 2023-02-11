def parse(file_name):
    lines = open(file_name).readlines()

    tokens = []
    for line in lines:
        if (line.strip() != ''):
            tokens.append(line.rstrip().split(' '))
    
    return tokens