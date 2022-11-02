input = 'while  (s < upper)   t = 33.00;'
leximes = input.split()

keyword = ['while', 'for', 'if', 'then', 'else']
separator = '();'
operator = '<='
real = '1234567890.'
result = []

temp = list(real)
for t in temp:
    print(t)
    print(t in real)
for lexime in leximes:
    if lexime in keyword:
        result.append(('keyword',lexime))
    else:
        token_string = list(lexime)
        id = ''
        real = ''
        for token in token_string:
            if token in separator:
                if len(id) > 0:
                    result.append(('identifier',id))
                    id = ''
                if len(real) > 0:
                    result.append(('real', real))
                    real = ''
                result.append(('separator', token))
            if token in operator:
                if len(id) > 0:
                    result.append(('identifier',id))
                    id = ''
                if len(real) > 0:
                    result.append(('real', real))
                    real = ''
                result.append(('operator', token))
            if token in real:
                real += token
            elif token.isalpha():
                id += token

                
        if len(id) > 0:
            result.append(('identifier', id))
        if len(real) > 0:
            result.append(('real', real))
        

        # for token in lexime:
        #     token_string = token
        #     id = []
        #     real = []
        #     if token in separator:
        #         result.append(('separator',token))
        #     elif token in operator:
        #         result.append(('operator',token))
        #     elif token.isalpha():
        #         for t in token:


print(result)

