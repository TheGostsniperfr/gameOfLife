
class Cell :
    def __init__(self, x, y, alive):
        self.X = x
        self.Y = y
        self.Alive = alive
        self.HasChanged = False
        self.Rect = None


    def nbNeighbours(self, grid):
        """
        Parameter :
            @input : (cell[][]) -> grid
            @output : (int) -> number of neighbours
        """
        nbNeighbours = 0

        #array of neighbours'coordonate  -> (x,y)
        potentialNeighbors = [(0, -1), (-1, 0), (1,0), (0,1)]

        for i in range(len(potentialNeighbors)):

            (tempX, tempY) = (self.X + potentialNeighbors[i][0], self.Y + potentialNeighbors[i][1])

            #check if is valid coordonate
            grid.Grid.isValidCoordonate(tempX, tempY)

            #check if the cell at the coordonates is not empty
            if(grid[tempX][tempY].Alive):
                nbNeighbours += 1            

        return nbNeighbours
    
    def update(self, grid):
        """
        this function update the cell
        
        Parameters : 
            @input : nothing
        """
        tempAlive = self.Alive
        nbNeighbours = self.nbNeighbours(grid)

        if(self.Alive):
            #check if alive (2 or 3 neighbours)
            if(not nbNeighbours == 2 and not nbNeighbours == 3):
                self.Alive = False 
        else:
            #check if the cell respawn
            if(nbNeighbours == 3):
                self.Alive = True
        
        #check if the cell has changed :
        if(tempAlive != self.Alive):
            self.HasChanged = True
        else:
            self.HasChanged = False
            
        

        