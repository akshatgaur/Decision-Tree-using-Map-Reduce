

l = [1,2,3,4]
l1 =[]
i = [1,3]
k = [ x for x in range(len(l))]
validation_idx = list(set(k) - set(i))
#print validation_idx
l1.append([l[x] for x in validation_idx])
print l1

