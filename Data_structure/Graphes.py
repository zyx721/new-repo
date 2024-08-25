class Graph:
    def __init__(self,edgs):
        self.edgs = edgs
        self.graph_dict={}
        for start ,end in self.edgs:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]
        print("Graph dict:",self.graph_dict)
    def get_path(self,start,end,path=[]):
        path= path + [start]
        if  start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths=[]
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_path(node,end,path)
                for p in new_path:
                    paths.append(p)
        return paths
    def getshortpath(self,start,end,path=[]):
        path = path+[start]
        if start not in self.graph_dict:
            return None
        if start == end:
            return path
        shortp= None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.getshortpath(node,end,path)
                if sp:
                    if shortp is None or len(sp)< len(shortp) :
                        shortp = sp

        return shortp


if __name__ == '__main__':
    routes=[
        ("Mumbai","Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]
    rout_graph = Graph(routes)
    d = {
        "Mumbai":["Paris","Dubai"]
    }
    start = "Paris"
    end = "New York"
    print(rout_graph.getshortpath(start,end))
