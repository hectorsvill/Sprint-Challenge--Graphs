
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
        self.mapped = dict()


    def getRoomPaths(self):
        exits = self.player.currentRoom.getExits()
        self.mapped[self.player.currentRoom.id] = dict()
        for e in exits:
            if self.player.currentRoom.getRoomInDirection(e) is not None:
                dirID = self.player.currentRoom.getRoomInDirection(e).id
                self.mapped[self.player.currentRoom.id][e] =  dirID
            else :
                self.mapped[self.player.currentRoom.id][e] = "?"

    
    def dfs(self):
        path = []
        backTrack = []

        self.mapped[self.player.currentRoom.id] = self.player.currentRoom.getExits()

        while len(self.mapped) < 499:
            if self.player.currentRoom.id not in self.mapped:
                currentroomID = self.player.currentRoom.id
                
                exits = self.player.currentRoom.getExits()
                self.mapped[currentroomID] = exits

                self.mapped[currentroomID].remove(backTrack[-1])
            while not len(self.mapped[self.player.currentRoom.id])  :
                back = backTrack.pop()
                path.append(back)
                self.player.travel(back)


            move = self.mapped[self.player.currentRoom.id].pop(0)
            path.append(move)


            if move == "n":
                backTrack.append("s")
            elif move == "s":
                backTrack.append("n")
            elif move == "e":
                backTrack.append("w")
            elif move == "w":
                backTrack.append("e")


            
            self.player.travel(move)
        

        
        print(path)
        return path





    # def getPath(self):
    #     print(self.player)
        # currentRoom = self.player.currentRoom
        # roomid = currentRoom.id
        
        # coord = (currentRoom.x, currentRoom.y)
        # print(exits, coord, roomid)
        # path = []

        # s = Stack()
        # for e in self.player.currentRoom.getExits(): 
        #     s.push(e)
        # visited = set()
        
        # while s.size() > 0:
        #     v = s.pop()
        #     self.player.travel(v)
        #     if v not in visited:
        #         print(v)
                
        #         path.append(v)

        #         visited.add(v)

        #         exits = self.player.currentRoom.getExits()
        #         for e in exits:
        #             # path_copy = path.copy()
        #             # path_copy.append(e)
        #             s.push(e)
        
        # print(visited)
        # return path

    

