
names = []
scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    scores.append(score)
    names.append(name)
    
    
st = dict(zip(names,scores))

sv = sorted(st.values())
sk= sorted(st, key=str.lower)
ab= list(dict.fromkeys(sv))
s_l = ab[2]
for s_l in sk:
    print(st.items(s_l))
