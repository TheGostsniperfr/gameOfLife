import Cell
import tkinter as tk

class Grid :
    def __init__(self, width, height, gridLineSize, gridLineColor, cellSize, cellColor , fenetreBgColor):
        self.Height = height
        self.Width = width 
        self.GridLineSize = gridLineSize
        self.GridColor = gridLineColor
        self.CellSize = cellSize
        self.CellColor = cellColor
        self.Canvas = None
        self.FenetreBgColor = fenetreBgColor
        

        #create grid -> cell[][]
        self.Grid = []
        for x in range(self.Width):
            tempLine = []
            for y in range(self.Height):
                tempLine.append(Cell(x,y,False))

            self.Grid.append(tempLine)

        self.createGrid()

        
    def update(self):
        """
        this function update all cells contened in the grid
        """
        for x in range(self.Width):
            for y in range(self.Height):
                if(self.Grid[x][y].Alive and not  self.Grid[x][y].update(self.Grid)):
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
    
    def showDisplay(self):

        for x in range(self.Width):
            for y in range(self.Height):
                cell = self.Grid[x][y]
                #check if the cell has changed between the last update
                if(cell.HasChanged):
                    #calcule the coordonate of the cell to paint without the grid line

                    #(int, int) -> (x1,y1) is the coordonate of the upper left corner
                    #(int, int) -> (x2,y2) is the coordonate of the lower right corner

                    (x1, y1) = (self.GridLineSize * (x + 1) + self.CellSize * x, 
                                self.GridLineSize * (y + 1) + self.CellSize * y)
                    
                    (x2, y2) = ((self.GridLineSize + self.CellSize) * (x + 1), 
                                (self.GridLineSize + self.CellSize) * (y + 1))


                    #check is the cell is Alive
                    if(cell.Alive):
                        #show the cell
                        self.Canvas.create_rectangle(x1, y1, x2, y2, fill = self.CellColor)
                    else:
                        #remove the cell
                        self.Canvas.create_rectangle(x1, y1, x2, y2, fill = self.FenetreBgColor)

    def createGrid(self):
        totalSize = self.CellSize + self.GridLineSize


        self.Canvas = tk.Canvas(tk.Tk(), width= self.Width * totalSize, height=self.Height * totalSize)
        self.canvas.pack()


        #create the background of the window
        self.Canvas.create_rectangle(0,0, 
                                     self.X * (self.CellSize + self.GridLineSize), 
                                     self.Y * (self.CellSize + self.GridLineSize), 
                                     fill = self.FenetreBgColor)
        
        #create the grid

        for i in range(self.Width+1):

            tempX = i * totalSize            
            self.Canvas.create_rectangle(tempX,0, tempX, self.Y * totalSize, fill = self.FenetreBgColor)

        for i in range(self.Height + 1):
            tempY = y * totalSize
            self.Canvas.create_rectangle(0, tempY, self.X * totalSize, tempY, fill = self.FenetreBgColor)


        





