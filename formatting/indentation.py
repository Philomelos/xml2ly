text = """\score {\n {\n aaaa <<\n testing \n>> \n abc = \Partlkjsdf { lkjsdfsjlkj sdf } \n lkjdlkfj lskdjf { \n lkjdsfl kj \n } \n }
""" 

def format_text(s,indent=0):
    import re

    result = []
    if not len(s) > 0:
        return ''

    for x in re.split(r' ', s):

        if x.startswith('{'):
            result.append(x[0])
            indent += 1
            result.append(format_text(x[1:], indent=indent))

        elif x.startswith('<<'):
            result.append(x[:2])
            indent += 1
            result.append(format_text(x[2:], indent=indent))

        elif x.startswith('}'):
            result.append(x[0])
            indent -= 1
            if len(x) > 1:
                result.append(format_text(x[1:], indent=indent))

        elif x.startswith('>>'):
            result.append(x[:2])
            indent -= 1
            if len(x) > 1:
                result.append(format_text(x[2:], indent=indent))

        elif x.startswith('\n'):
            result.append(x[0])
            result.append('  ' * indent)
            if len(x) > 1:
                result.append(format_text(x[1:], indent=indent))

        else:
            result.append(x)

    return ' '.join(result)

print format_text(text)
