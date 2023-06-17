import tkinter as tk
from Core.Cell import Cell
import copy
import threading

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
        self.nbIteration = 0
        self.NbIterationUI = None
        

        self.Canvas = tk.Canvas(self.Fenetre, width= (self.Width) * self.CellSize +1, height=(self.Height) * self.CellSize+1) 
        self.Canvas.pack()

        #create grid -> cell[][]
        self.Grid = []
        for x in range(self.Width):
            tempLine = []
            for y in range(self.Height):
                tempLine.append(Cell(x,y,False, (self.Width, self.Height)))

            self.Grid.append(tempLine)
            
        self.IsLaunch = False
            
        



        
    def update(self):
        """
        this function update all cells contened in the grid
        """
        #add one iteration
        self.nbIteration += 1
        self.NbIterationUI.config(text=str(self.nbIteration))
        
        
        #copy the current grid
        currentGrid = copy.deepcopy(self.Grid)
        
        for x in range(self.Width):
            for y in range(self.Height):
                cell = self.Grid[x][y]
                cell.update(currentGrid)                
                if(cell.HasChanged):
                    if(cell.Alive):
                        self.Canvas.itemconfig(self.Grid[x][y].Rect, fill=self.CellColor)
                    else:
                        self.Canvas.itemconfig(self.Grid[x][y].Rect, fill=self.FenetreBgColor)
                                            
        #self.Fenetre.update()


    def createDisplay(self):       
        
        # *****************************************************************************
        # *                                                                           *
        # *                            Grid generation                                 *
        # *                                                                           *
        # *****************************************************************************
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


        # *****************************************************************************
        # *                                                                           *
        # *                            UI generation                                 *
        # *                                                                           *
        # *****************************************************************************
        
        #launch btn
        launchBtn = tk.Button(self.Fenetre, text = "start", command = self.launchBtn)
        launchBtn.pack(side=tk.BOTTOM, pady=10)
                
        #+1 btn
        oneIterationBtn = tk.Button(self.Fenetre, text="+1", command=self.oneIteration)
        oneIterationBtn.pack(side=tk.BOTTOM, pady=10)
        
        
        
        
        #nb of iteration UI
        self.NbIterationUI = tk.Label(self.Fenetre, text = str(self.nbIteration))
        self.NbIterationUI.pack(side=tk.BOTTOM, anchor=tk.CENTER)
    
        # *****************************************************************************
        # *                                                                           *
        # *                            Update fenetre                                *
        # *                                                                           *
        # *****************************************************************************
          
        self.Fenetre.update()


    


    #Event function called by cell btn 
    def rectIsClicked(self, event, x, y):
        #switch the cell
        
        if(self.Grid[x][y].Alive):
            self.Canvas.itemconfig(self.Grid[x][y].Rect, fill=self.FenetreBgColor)
        else:
            self.Canvas.itemconfig(self.Grid[x][y].Rect, fill=self.CellColor)

        self.Grid[x][y].Alive ^= True
        self.Grid[x][y].HasChanged = True
    
    #Command function called by launch btn
    def oneIteration(self):
        self.update()
        
    def launchBtn(self):
       self.IsLaunch ^= True 
       
       if(self.IsLaunch):
           #start the loop in a new thread
            threading.Thread(target=self.loop).start()   
            
        
       
    def loop(self):
        while(self.IsLaunch):
            self.update()



    def start(self):
        
        self.createDisplay()
                
        self.Fenetre.mainloop()


