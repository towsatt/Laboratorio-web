inp = open('input').read().split('\n\n')

s = ''

for par in inp:
    par = par.split('\n')
    if len(par) == 1:
        s += f"<h2>{par[0].strip()}</h2>\n"
        continue
    
    s += f'<dt>{par[0].strip()}</dt>\n<dd>\n<img src="">\n<dl>'
    for ind, i in enumerate(par[1:]):
        if ind%2 == 0:
            s+=f'<dt>{i.strip()}</dt>\n'
        else:
            s+=f'<dd>{i.strip()}</dd>\n'
    s+='</dl>\n</dd>'
open('out', 'w+').write(s)