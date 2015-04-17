
def find_path(src, dest, mesh):
    print mesh

    temppath = []
    tempvisited = []
    temppath.append(((10, 10), (20, 20)))
    temppath.append(((30, 30), (40, 40)))
    tempvisited.append((10, 10, 20, 20))
    tempvisited.append((30, 30, 40, 40))
    return (temppath, tempvisited)

