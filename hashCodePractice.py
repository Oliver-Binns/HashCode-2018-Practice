def readToStartOfNextLine(text, i):
    while i < len(text) and not text[i] == '\n':
        i += 1
    i += 1
    return i

def main():
    f = open('example.txt', 'r')

    text = f.read()
    i = 0

    print(text)

    r = text[i]
    while (text[i] != ' '):
        i += 1
    i += 1
    c = text[i]
    while (text[i] != ' '):
        i += 1
    i += 1
    l = text[i]
    while (text[i] != ' '):
        i += 1
    i += 1
    h = text[i]

    print("rows =", r)
    print("columns =", c)
    print("low =", l)
    print("high =", h)

    rowRange = range(int(r))
    colRange = range(int(c))
    pizza = [['\0' for _ in colRange] for _ in rowRange]

    i = readToStartOfNextLine(text, i)

    for row in rowRange:
        for col in colRange:
            pizza[row][col] = text[i]
            i += 1

        i = readToStartOfNextLine(text, i);

    print(pizza)

    f.close()

main()
