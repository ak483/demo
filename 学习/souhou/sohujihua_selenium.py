
content=['dfdsf','jlkdjfldsf','sdfsdfsd','gsdfgdg','fsdfsdfs','','dfsdfsdf','','sdfsdfds']
# for c in range(len(content)):
    # content[c] = re.sub('\u3000\u3000', '', content[c])
    # if len(content[c]) == 0:
    #     del content[c]
        # content = filter(lambda content: x != 0, content)

content = [x for x in content if len(x)!=0]
print(content)
