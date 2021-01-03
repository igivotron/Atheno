from tkinter import *
import matplotlib.pyplot as plt
fen=Tk()
cote=420
marge = 20
neutre=0
blanc=1
noir=2

y1=[]
y2=[]
x1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59]


can=Canvas(fen,bg="green",height=cote, width=cote)
can.pack()

nb_cases = 8
pas = 400/nb_cases

x=0
y=0
a=0




etat=[[neutre for row in range(cote)] for col in range(cote)]
temp=[[neutre for row in range(cote)] for col in range(cote)]


while (x<=nb_cases):
    can.create_line(marge,marge+pas*x,marge+cote,marge+pas*x, fill='black')
    x=x+1
while (y<=nb_cases):
    can.create_line(marge+pas*y,marge+cote,marge+pas*y,marge, fill='black')
    y=y+1

def trace_b (x,y):
    r=25
    x = marge+pas*(x-1/2)
    y = marge+pas*(y-1/2)
    return can.create_oval(x-r, y-r, x+r, y+r, fill = 'black')



def trace_w (x,y):
    r=25
    x = marge+pas*(x-1/2)
    y = marge+pas*(y-1/2)
    return can.create_oval(x-r, y-r, x+r, y+r, fill = 'white')

def init():
    for y in range(cote):
        for x in range (cote):
            etat[x][y] = neutre
            temp[x][y] = neutre


    pion_b = trace_b(4,4), trace_b(5,5)
    pion_w = trace_w(5,4), trace_w(4,5)
    etat[4][4] = noir
    etat[5][5] = noir
    etat[5][4] = blanc
    etat[4][5] = blanc

   

    
            
            
def clic (event):
    global y1
    global a
    r=25
    

    x, y =event.x, event.y
    i=0
    for i in range(8):
        if marge+i*pas<x<marge+(i+1)*pas:
            x=i+1
        
        if marge+i*pas<y<marge+(i+1)*pas:
            y=i+1

            
    if (a%2)==0:                                  ### noir
        if etat[x][y]==neutre:
           if etat[x-1][y] or etat[x+1][y] or etat[x][y-1] or etat[x][y+1] or etat[x-1][y-1] or etat[x-1][y+1] or etat[x+1][y-1] or etat[x+1][y+1] == noir:
                
                  
                    
                pion_b = trace_b(x,y)
                etat[x][y] = noir
                a=a+1
                test(x,y)
                print("Tour n°",a)
                fin()
            

    if (a%2)==1:                                  ### blanc
        if etat[x][y] == neutre:
            if etat[x-1][y] or etat[x+1][y] or etat[x][y-1] or etat[x][y+1] or etat[x-1][y-1] or etat[x-1][y+1] or etat[x+1][y-1] or etat[x+1][y+1] == noir:
                poin_w = trace_w(x,y)
                etat[x][y] = blanc
                a=a+1
                test(x,y)
                print("Tour n°",a)
                fin()
    

    

def test(x,y):
    m=0
    n=0
    if etat[x][y] == blanc:          
        if etat[x-1][y] == noir:
            for n in range(1,8):                    ### blanc droite à gauche
                if etat [x-1-n][y] == neutre:
                    break
                if etat [x-1-n][y] == blanc:
                    for m in range(1,n+1):
                        etat[x-m][y] = blanc
                        trace_w (x-m,y)
                        m=m+1

                    break
                n=n+1

    if etat[x][y] == noir:            
        if etat[x-1][y] == blanc:                   ### noir droite à gauche
            for n in range(1,8):
                if etat [x-1-n][y] == neutre:
                    break
                if etat [x-1-n][y] == noir:
                    for m in range(1,n+1):
                        etat[x-m][y] = noir
                        trace_b (x-m,y)
                        m=m+1

                    break
                n=n+1

    if etat[x][y] == noir:          
        if etat[x+1][y] == blanc:
            for n in range(1,8):
                if etat [x+1+n][y] == neutre:
                    break
                if etat [x+1+n][y] == noir:
                    for m in range(1,n+1):      ### noir gauche  à droite
                        etat[x+m][y] = noir
                        trace_b (x+m,y)
                        m=m+1

                    break
                n=n+1
       
    
    if etat[x][y] == blanc:                           
        if etat[x+1][y] == noir:
            for n in range(1,8):                ### blanc gauche à droite
                if etat [x+1+n][y] == neutre:
                    break
                if etat [x+1+n][y] == blanc:
                    for m in range(1,n+1):
                        etat[x+m][y] = blanc
                        trace_w (x+m,y)
                        m=m+1

                    break
                n=n+1
       
    

    if etat[x][y] == blanc:         
        if etat[x][y-1] == noir:
            for n in range(1,8):
                if etat [x][y-1-n] == neutre:
                    break
                if etat [x][y-1-n] == blanc:        
                    for m in range(1,n+1):
                        etat[x][y-m] = blanc
                        trace_w (x,y-m)
                        m=m+1

                    break
                n=n+1

    if etat[x][y] == noir:
        if etat[x][y-1] == blanc:
            for n in range(1,8):
                if etat [x][y-1-n] == neutre:
                    break
                if etat [x][y-1-n] == noir:         
                    for m in range(1,n+1):
                        etat[x][y-m] = noir
                        trace_b (x,y-m)
                        m=m+1

                    break
                n=n+1


    if etat[x][y] == blanc:
      
           
        if etat[x][y+1] == noir:                    
            for n in range(1,8):
                if etat [x][y+1+n] == neutre:
                    break
                if etat [x][y+1+n] == blanc:
                    for m in range(1,n+1):
                        etat[x][y+m] = blanc
                        trace_w (x,y+m)
                        m=m+1

                    break
                n=n+1

    if etat[x][y] == noir:
       
           
        if etat[x][y+1] == blanc:
            for n in range(1,8):
                if etat [x][y+1+n] == neutre:
                    break
                if etat [x][y+1+n] == noir:         
                    for m in range(1,n+1):
                        etat[x][y+m] = noir
                        trace_b (x,y+m)
                        m=m+1

                    break
                n=n+1



    if etat[x][y] == blanc:
       
            
        if etat[x-1][y-1] == noir:
            for n in range(1,8):
                if etat [x-1-n][y-1-n] == neutre:
                    break
                if etat [x-1-n][y-1-n] == blanc:    
                    for m in range(1,n+1):
                        etat[x-m][y-m] = blanc
                        trace_w (x-m,y-m)
                        m=m+1

                    break
                n=n+1



    if etat[x][y] == noir:
        if etat[x-1][y-1] == blanc:
            for n in range(1,8):
                if etat [x-1-n][y-1-n] == neutre:
                    break
                if etat [x-1-n][y-1-n] == noir:     
                    for m in range(1,n+1):
                        etat[x-m][y-m] = noir
                        trace_b (x-m,y-m)
                        m=m+1

                    break
                n=n+1


    if etat[x][y] == noir:      
        if etat[x+1][y+1] == blanc:
            for n in range(1,8):       
                if etat [x+1+n][y+1+n] == neutre:
                    break
                if etat [x+1+n][y+1+n] == noir:     
                    for m in range(1,n+1):
                        etat[x+m][y+m] = noir
                        trace_b (x+m,y+m)
                        m=m+1

                    break
                n=n+1


    if etat[x][y] == blanc:     
        if etat[x+1][y+1] == noir:
            for n in range(1,8):
                if etat [x+1+n][y+1+n] == neutre:
                    break
                if etat [x+1+n][y+1+n] == blanc:    
                    for m in range(1,n+1):
                        etat[x+m][y+m] = blanc
                        trace_w (x+m,y+m)
                        m=m+1
                    break
                n=n+1


    if etat[x][y] == blanc:        
        if etat[x+1][y-1] == noir:
            for n in range(1,8):
                if etat [x+1+n][y-1-n] == neutre:
                    break
                if etat [x+1+n][y-1-n] == blanc:    
                    for m in range(1,n+1):
                        etat[x+m][y-m] = blanc
                        trace_w (x+m,y-m)
                        m=m+1
                    break
                n=n+1



    if etat[x][y] == noir:         
        if etat[x+1][y-1] == blanc:
            for n in range(1,8):
                if etat [x+1+n][y-1-n] == neutre:
                    break
                if etat [x+1+n][y-1-n] == noir:    
                    for m in range(1,n+1):
                        etat[x+m][y-m] = noir
                        trace_b (x+m,y-m)
                        m=m+1
                    break
                n=n+1



    if etat[x][y] == blanc:      
        if etat[x-1][y+1] == noir:
            for n in range(1,8):
                if etat [x-1-n][y+1+n] == neutre:
                    break
                if etat [x-1-n][y+1+n] == blanc:    
                    for m in range(1,n+1):
                        etat[x-m][y+m] = blanc
                        trace_w (x-m,y+m)
                        m=m+1
                    break
                n=n+1


    if etat[x][y] == noir:     
        if etat[x-1][y+1] == blanc:
            for n in range(1,8):
                if etat [x-1-n][y+1+n] == neutre:
                    break
                if etat [x-1-n][y+1+n] == noir:    
                    for m in range(1,n+1):
                        etat[x-m][y+m] = noir
                        trace_b (x-m,y+m)
                        m=m+1
                    break
                n=n+1




def fin():
    nb_noir=0
    nb_blanc=0  
    for p in range(1,9):
        for q in range (1,9):
            if etat[p][q] == blanc:
                nb_blanc = nb_blanc +1
                
   
            if etat[p][q] == noir:
                nb_noir = nb_noir +1
                
        
            if nb_noir + nb_blanc == 64:
                print ("partie terminée")
                fig=plt.figure(figsize=[5,5])
                plt.plot(x1,y1, color='red')
                plt.plot(x1,y2, color='blue')
                plt.grid()
                plt.legend(['Nombre de blancs','Nombre de noir'])
                
                plt.show()
            

    print ("Blanc = ", nb_blanc)
    y1.append(nb_blanc)
    print ("Noir = ", nb_noir)
    y2.append(nb_noir)
        
    
    
        
        

   
can.bind("<Button-1>", clic)
init()

fen.mainloop()
