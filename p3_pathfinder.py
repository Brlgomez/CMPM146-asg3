from heapq import heappush, heappop
def find_path(src, dest, mesh):
    print mesh
    v = src
    q = []
    visited = []
    d = {}
    p = {}
    d[src] = True
    heappush(q,(d[src],src))
    visited.append(src)
    while q:
        dV, v = heappop(q)
        if v is dest:
            break
        neighbors = mesh['adj'].get(v,[])
        for w in neighbors:
            if w is dest:

             if d[w] is not True:
                visited.append(w)
                p[w] = v
                d[w] = True
                heappush(q, (d[w],w))
    if v is dest:
        path = []
        node = dest
        while node in p:
            path.append(node )
            node = p[node]
        path.append(src)
        path.reverse()
        return (path, visited)
    else:
        return []


