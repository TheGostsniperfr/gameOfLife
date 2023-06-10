import Cell

class Grid :
    def __init__(self, width, height, gridLineColor, cellSize, cellColor):
        self.Height = height
        self.Width = width 
        self.GridColor = gridLineColor
        self.CellSize = cellSize
        self.CellColor = cellColor

        #create grid -> cell[][]
        self.Grid = []
        for x in range(self.Width):
            tempLine = []
            for y in range(self.Height):
                tempLine.append(Cell(x,y,False, cellColor))

            self.Grid.append(tempLine)
        
    def update(self):
        """
        this function update all cells contened in the grid
        """
        for x in range(self.Width):
            for y in range(self.Height):
                if(self.Grid[x][y].Alive and not  self.Grid[x][y].Cell.update(self.Grid)):
                    #if the cell isn't alive, replace by None in the grid
                    self.Grid[x][y].Alive = False

    def isValidCoordonate(self, x, y):
        """
        check if the coordonate x, y in valid in the grid
        
        Parameters :
            @input :    (int) -> x
                        (int) -> y
                        
            @output :   (bool) -> isValid                    
        """

        return (x >= 0 and y >= 0) and (x < self.Width and y < self.Height)
    
    



