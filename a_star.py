#!/usr/bin/env python3
import numpy as np

def eucledian(xi, xf,yi,yf): #Eucledian distance between vertexes, used for heuristic calculation
    cost = np.sqrt(((xi - xf)**2) + ((yi - yf)**2))
    return cost

def get_children(vedges, current): # get children nodes
    children = np.where(vedges == current)[0] 
    children = vedges[children] 
    children = np.unique(children) 
    children = children.tolist() 
    children.remove(current) 
    return children


def path_finder(start, goal, vertexes_list, vedges):
    
    #---------------Initialization------------------
    open_list = {start : [0,0,0,None]}
    closed_list = {}
    open_list[start][0] = 0                                                                                                      # Initializing g score
    open_list[start][1] = eucledian(vertexes_list[start].x,vertexes_list[goal].x, vertexes_list[start].y, vertexes_list[goal].y) # Heuristic value
    open_list[start][2] = open_list[start][0] + open_list[start][1]                                                              # Initializing f score
    #---------------Initialization------------------

    

    while(goal not in closed_list):

        current = list(open_list.keys())[0]                         # Set the element with the least f value as current
    
        children = get_children(vedges, current)                    # Each Adyacent vertex
        for child in children:                                      # For each adjacent vertex
            if child not in closed_list and child not in open_list: # If the adjacent vertex is not in the closed or open list

                g = open_list[current][0] + eucledian(vertexes_list[current].x,vertexes_list[child].x, vertexes_list[current].y, vertexes_list[child].y) # Calculate the cost from the start vertex
                h = eucledian(vertexes_list[child].x,vertexes_list[-1].x, vertexes_list[child].y, vertexes_list[-1].y)                                   # Calculate the heuristic to the goal vertex
                f = g + h                                                                                                                                # calculate the F score
                if (child not in open_list) or (f < open_list[child][2]):                                                                                # If the child is not in the open list or if the new f score is lower
                    open_list[child] = [g ,h ,f, current]

        closed_list[current] = open_list[current]    # Add current vertex to closed list
        open_list.pop(current)                       # Delete current vertex from the open list

        open_list = dict(sorted(open_list.items(), key=lambda x: x[1][2])) # Sort open_list in ascending order with respect the f value


        
    # Retrieve path following backpointer ----------------------------
    path = []
    i = list(closed_list.keys())[-1] 
    while i != start :
        path.append(i)
        i = closed_list[i][3]
    path.append(start)
    # ----------------------------------------------------------------

    total_distance = closed_list[goal][0] #Total distance to bbe travelled

    return path, total_distance


