import Class
# le graphe est non orienté donc il suffit d'en faire un parcours en largeur pour determiner s'il est connexe
def connexite(graph, s):
    connexe = False
    parcouru = []
    stack = [s]
    while stack != []:
        node = stack.pop()
        if node not in parcouru:
            parcouru.append(node)
            stack = stack + list((graph.neighbors(node)))
    if len(parcouru)==len(graph):
        connexe = True
    return connexe