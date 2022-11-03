
def lexer(lexemes):
    keyword = ['while', 'for', 'if', 'then', 'else']
    separator = '();'
    operators = '<='
    reals = '1234567890.'
    result = []
    id = ''
    real = ''

    for lexime in lexemes:
        if lexime in keyword:
            result.append(('keyword',lexime))
        else:
            token_string = list(lexime)
            for token in token_string:
                if token in reals:
                    real += token
                elif token.isalpha():
                    id += token
                elif token in operators:
                    if len(id) > 0:
                        result.append(('identifier',id))
                        id = ''
                    if len(real) > 0:
                        result.append(('real', real))
                        real = ''
                    result.append(('operator', token))

                elif token in separator:
                    if len(id) > 0:
                        result.append(('identifier',id))
                        id = ''
                    if len(real) > 0:
                        result.append(('real', real))
                        real = ''
                    result.append(('separator', token))
    return result

with open('input_scode.tx') as f:
    lines = [line for line in f]

lex = lines[0].split()

output = lexer(lex)

with open('output.txt', 'w') as out:
    out.write('{:<20s} {:<10s}'.format('tokens','lexemes\n'))
    out.write('-----------------------------------------------\n')
    for each in output:
        out.write('{:<20s} {:<10s}\n'.format(each[0],each[1]))
