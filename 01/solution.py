import functools


with open('input.txt') as fp:
    data = fp.read().splitlines()


def process_string(snd, s):
    match s:
        case '': return ''
        case _ as d if d[0].isdigit(): return d[0] + process_string(snd, d[1:])    
        case _ as d if snd and d.startswith('one'): return '1' + process_string(snd, d[1:])
        case _ as d if snd and d.startswith('two'): return '2' + process_string(snd, d[1:])
        case _ as d if snd and d.startswith('three'): return '3' + process_string(snd, d[1:])
        case _ as d if snd and d.startswith('four'): return '4' + process_string(snd, d[1:])
        case _ as d if snd and d.startswith('five'): return '5' + process_string(snd, d[1:])
        case _ as d if snd and d.startswith('six'): return '6' + process_string(snd, d[1:])
        case _ as d if snd and d.startswith('seven'): return '7' + process_string(snd, d[1:])
        case _ as d if snd and d.startswith('eight'): return '8' + process_string(snd, d[1:])
        case _ as d if snd and d.startswith('nine'): return '9' + process_string(snd, d[1:])
        case _ as d: return process_string(snd, d[1:])

def sum_of_values(data, f):
    return sum(map(
        lambda x: int(x[::len(x) - 1] if len(x) > 1 else x + x),
        map(f, data)
    ))


## Part I
print(sum_of_values(data, functools.partial(process_string, False)))

# Part II
print(sum_of_values(data, functools.partial(process_string, True)))
