from room import Room

class Path:
    def __init__(self, player):
        self.player = player
        # create adjacency list with room as key and exits array as value 
        self.mapped = dict() 

    def dfs(self):
        path = []
        backTrack = []

        # {0: ['n', 's', 'w', 'e']}
        self.mapped[self.player.currentRoom.id] = self.player.currentRoom.getExits()
        
        # graph consisting of 500 rooms
        while len(self.mapped) < 499:
            if self.player.currentRoom.id not in self.mapped:
                currentroomID = self.player.currentRoom.id
                exits = self.player.currentRoom.getExits()
                # not a mapped room add to map
                self.mapped[currentroomID] = exits
                self.mapped[currentroomID].remove(backTrack[-1])
            # when players hits dead end, backtrack and store path
            while not len(self.mapped[self.player.currentRoom.id]):
                back = backTrack.pop()
                path.append(back)
                self.player.travel(back)

            # Get next move
            move = self.mapped[self.player.currentRoom.id].pop(0)
            path.append(move)

            # get inverse room fro backTrack
            if move == "n":
                backTrack.append("s")
            elif move == "s":
                backTrack.append("n")
            elif move == "e":
                backTrack.append("w")
            elif move == "w":
                backTrack.append("e")
            
            # travel to next room
            self.player.travel(move)
        
        # print(self.mapped)
        # print(path)
        return path
