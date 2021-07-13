import random

def scrambled(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest

def get_combos(words: list):
    combos = []
    single = [i[:-2] for i in words if i.lower()[-1] == 's']
    for i in single:
        words.append(i)
    for i in words:
        for j in words:
            combos.append(i+j)
            combos.append(j+i)
            combos.append(i+' '+j)
            combos.append(j+' '+i)
            combos.append(i+' and '+j)
            combos.append(j+' and '+i)
            combos.append(i+'\'s '+j)
            combos.append(j+'\'s '+i)
            combos.append('top 10 '+i+'s')
            combos.append('top 10 '+j+'s')
            combos.append('most '+i+'s')
            combos.append('most '+j+'s')

    for i in words:
        combos.append(i)

    non_dup = []
    for i in combos:
        if not i in non_dup:
            non_dup.append(i)

    repeated = []
    for i in non_dup:
        for j in range(3):
            repeated.append(i)
            
    return scrambled(repeated)

def get_html(combos: list):
    metas = ','.join(combos)
    divs = ' '.join(combos)
    html = f'<meta name="keywords" content="{metas}"><div style="display:none;">{divs}</div>'
    return html
