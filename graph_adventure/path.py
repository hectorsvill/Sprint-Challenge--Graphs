
from room import Room


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


# mapped[self.player.currentRoom.id] = {'n': "?", 's': "?",'e': "?",'w': "?", }

class Path:
    def __init__(self, player):
        self.player = player




    def getPath(self):
        exits = self.player.currentRoom.getExits()
        mapped = dict()

        mapped[self.player.currentRoom.id] = dict()
        dirID = None
        for e in exits:
            if self.player.currentRoom.getRoomInDirection(e) is not None:
                dirID = self.player.currentRoom.getRoomInDirection(e).id
                mapped[self.player.currentRoom.id][e] =  dirID
    

        
        print(dirID)
        
        print(mapped)
        return []


    def get_map(self):

        self.player.travel("n")

        # currentRoom = self.player.currentRoom
        # roomid = currentRoom.id
        
        # coord = (currentRoom.x, currentRoom.y)
        # print(exits, coord, roomid)
        path = []
        s = Stack()
        visited = {}
        
        s.push(self.player.currentRoom.getExits())
        while s.size() > 0:
            
            path = s.pop()
            v = path[-1]
            if v not in visited:
                self.player.travel(v)
                path.append(v)
                visited[v] = path
                exits = self.player.currentRoom.getExits()
                for e in exits:
                    path_copy = path.copy()
                    path_copy.append(e)
                    s.push(path_copy)
        return path



