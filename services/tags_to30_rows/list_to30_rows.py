ORIGINAL = 'From.txt'
EDITED = 'Midway.txt'
TAGS = 'BADTAGS.txt'
count = 0

with open(ORIGINAL, 'r', encoding='utf-8') as ORIG, \
        open(EDITED, 'w+', encoding='utf-8') as EDIT, \
        open(TAGS) as T:

    [EDIT.write(line) for line in ORIG if line not in T.readlines()]

with open(EDITED, 'r') as EDIT, \
        open('RESULT.txt', 'w', encoding='utf-8') as result:

    for line in EDIT:
        if count < 30:
            result.write(line)
            count += 1
        else:
            count = 0
            result.write('\n')
