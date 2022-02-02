cash = 5
disc = 0.3
dc = (f'{disc:.1%}')
print(dc)
tax = 0.07
t = (f'{tax:.1%}')
print(t)
ip = str(float(79.5))

st1 = (float(ip) -float(cash))
print(st1)
st2 = st1 * disc
print(st2)
st3 = st2 + tax
st = (round(st3,2))
print(st)





