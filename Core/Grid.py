import tkinter as tk
from Core.Cell import Cell

class Grid :
    def __init__(self, width, height, gridLineColor, cellSize, cellColor , fenetreBgColor):
        self.Height = height
        self.Width = width 
        self.GridColor = gridLineColor
        self.CellSize = cellSize
        self.CellColor = cellColor
        self.Canvas = None
        self.FenetreBgColor = fenetreBgColor
        self.Fenetre = tk.Tk()
        

        self.Canvas = tk.Canvas(self.Fenetre, width= (self.Width) * self.CellSize +1, height=(self.Height) * self.CellSize+1) 
        self.Canvas.pack()

        #create grid -> cell[][]
        self.Grid = []
        for x in range(self.Width):
            tempLine = []
            for y in range(self.Height):
                tempLine.append(Cell(x,y,False))

            self.Grid.append(tempLine)


        
    def update(self):
        """
        this function update all cells contened in the grid
        """
        for x in range(self.Width):
            for y in range(self.Height):
                if(self.Grid[x][y].Alive):
                    self.Grid[x][y].update(self.Grid)

    def isValidCoordonate(self, x, y):
        """
        check if the coordonate x, y in valid in the grid
        
        Parameters :
            @input :    (int) -> x
                        (int) -> y
                        
            @output :   (bool) -> isValid                    
        """
        return (x >= 0 and y >= 0) and (x < self.Width and y < self.Height)
    
    def createDisplay(self):
        for x in range(self.Width):
            for y in range(self.Height):
                cell = self.Grid[x][y]
                
                #calcule the coordonate of the cell to paint without the grid line

                #(int, int) -> (x1,y1) is the coordonate of the upper left corner
                #(int, int) -> (x2,y2) is the coordonate of the lower right corner

                (x1, y1) = (self.CellSize * (x) +2, 
                             self.CellSize * (y) +2)
                
                (x2, y2) = (self.CellSize * (x + 1) +2),  self.CellSize * (y + 1) +2
                
                cell.Rect = self.Canvas.create_rectangle(x1, y1, x2, y2, fill = self.FenetreBgColor)
                    
                #add event, on click for rect
                self.Canvas.tag_bind(cell.Rect, "<Button-1>", lambda event, X=x, Y=y: self.rectIsClicked(event, X, Y))  

                        
        self.Fenetre.update()

        
    def rectIsClicked(self, event, x, y):
        #switch the cell
        
        if(self.Grid[x][y].Alive):
            self.Canvas.itemconfig(self.Grid[x][y].Rect, fill=self.FenetreBgColor)
        else:
            self.Canvas.itemconfig(self.Grid[x][y].Rect, fill=self.CellColor)

        self.Grid[x][y].Alive ^= True
        self.Grid[x][y].HasChanged = True
        
       
        
        

    def start(self):
        
        self.createDisplay()
                
        self.Fenetre.mainloop()


