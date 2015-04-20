from heapq import heappush, heappop
def find_path(src, dest, mesh):
    v = src
    dF = dest
    q = []
    visited = []
    d = {}
    p = {}
    for z in mesh:
        if (z[0] <= src[0] and z[2] >= src[0] and z[1]<= src[1] and z[3] >= src[1]):
            v = z
            visited.append(v)
            d[v]= True
        if(z[0] <= dest[0] and z[2] >= dest[0] and z[1] <= dest[1] and z[3] >= dest[1]):
            dF = z

   # print mesh

    heappush(q,(d[v],v))
    #visited.append(src)
    while q:
        dV, v = heappop(q)
        if v is dF:
            break
        neighbors = mesh['adj'].get(v,[])
        for w in neighbors:

            if d[w] is not True:
                visited.append(w)
                p[w] = v
                d[w] = True
                heappush(q, (d[w],w))

    return ([(src, dest)], visited)



