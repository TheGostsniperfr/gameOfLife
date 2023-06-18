import tkinter as tk
from Core.Cell import Cell
import copy, threading, random
 

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
                        
    def randomGrid(self, chaos):
        """
        this function generate a random grid, each cell is set with a percentage of chaos
        
        Parameters :
            @input :
                -(float) -> chaos : number between 0 and 1 which set the percentage of luck to set a cell on
        """
        
        for x in range(self.Width):
            for y in range(self.Height):
                if(random.uniform(0, 1) > chaos):
                    self.switchCell(x, y, True)
                else:
                    self.switchCell(x, y, False)
                    
                

       
                                            
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
            self.switchCell(x, y, False)
        else:
            self.switchCell(x, y, True)
    
        
    def switchCell(self, x, y, state):
        """
        this function switch the cell state by the value of state parameters
        
        @inputs :
            -(int) -> x : coordonate x of the cell to edit
            -(int) -> y : coordonate y of the cell to edit
            -(bool) -> state : new state of the cell
        """
        
        if(state):
            self.Canvas.itemconfig(self.Grid[x][y].Rect, fill=self.CellColor)
        else:
            self.Canvas.itemconfig(self.Grid[x][y].Rect, fill=self.FenetreBgColor)           
            
        self.Grid[x][y].Alive = state
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
                
        self.randomGrid(0.5)
        
        self.Fenetre.mainloop()


