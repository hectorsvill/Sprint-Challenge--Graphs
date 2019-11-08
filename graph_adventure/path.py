
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

class Path:
    def __init__(self, player):
        self.player = player

    def getPath(self):
        pass
    
    def get_map(self):

        self.player.travel("n")

        # currentRoom = self.player.currentRoom
        # roomid = currentRoom.id
        # exits = self.player.currentRoom.getExits()
        # coord = (currentRoom.x, currentRoom.y)
        # print(exits, coord, roomid)
        
        q = Queue()
        visited = {}
        
        q.enqueue(self.player.currentRoom.getExits())
        while q.size() > 0:
            
            path = q.dequeue()
            v = path[-1]
            
            if v not in visited:
                self.player.travel(v)
                visited[v] = path
                exits = self.player.currentRoom.getExits()
                for e in exits:
                    path_copy = path.copy()
                    path_copy.append(e)
                    q.enqueue(path_copy)
        return visited
