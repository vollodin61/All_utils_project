ORIGINAL = 'From.txt'
EDITED = 'Midway.txt'
TAGS = 'BADTAGS.txt'
count = 0

with open(ORIGINAL) as orig, \
        open(EDITED, 'w+', encoding='utf-8') as edit,\
        open(TAGS) as tags:

    tag = tags.readlines()

    for line in orig:
        if line not in tag:
            edit.write(line)

with open(EDITED, 'r') as edit, \
        open('RESULT.txt', 'w', encoding='utf-8') as result:

    for line in edit:
        if count < 30:
            result.write(line)
            count += 1
        else:
            count = 0
            result.write('\n')
