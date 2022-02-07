#!/usr/bin/env python3
import csv
import numpy as np
import as_utils
import matplotlib.pyplot as plt

# The present visibility class is mainly used for specific utilities such as plotting and printing results
# in order to have better code organization 
class visibility(object):
    def __init__(self , map):
        self.map = map


    def get_edges_vertexes(self):
        # This function reads a csv file to retrieve the vertexes in the enviornment (start, goal and obstacles' vertexes)
        # It creates a dictionary of list where each list represents the vertexes in a specific obstacle
        v = []
        with open(self.map,'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                v.append(row)

        v = np.array(v)
        v = v.astype(float)

        vertexes_dict = {}


        for i in v:
            if not(bool(vertexes_dict.get(int(i[0])))):
                vertexes_dict[int(i[0])] = []
            vertexes_dict[int(i[0])].append(as_utils.Point(i[1],i[2]))
        
        # This function also computes the Edges of each obstacle consdiering the vertexes that define it 
        E = []
        #Create obstacle edges
        for i in range(1,len(vertexes_dict)-1):
            for j in range(0,len(vertexes_dict[i])-1):
                E.append(as_utils.Segment(vertexes_dict[i][j],vertexes_dict[i][j+1]))
            E.append(as_utils.Segment(vertexes_dict[i][len(vertexes_dict[i])-1],vertexes_dict[i][0]))

        return E, vertexes_dict


    def get_visibility_edges(self, visibility_e,vertexes):
        VE = []
        with open(visibility_e,'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for row in csv_reader:
                VE.append(row)

            VE = np.array(VE)
            VE = VE.astype(int)
        vedges = []
        for edge in VE:
            vedges.append(as_utils.Segment(vertexes[edge[0]],vertexes[edge[1]]))
            
        return(VE,vedges)

    def plot_edges(self, edges, ecolor = "black", estyle = "solid", width=3):
        # The purpose of the function is to plot the obstacles' edges
        for j in edges:
            plt.plot([j.p1.x,j.p2.x], [j.p1.y,j.p2.y],color = ecolor,linewidth=width,linestyle = estyle) 

    def plot_vertexes(self, vertexes):
        # The purpose of the function is to plot vertexes in the environment
        counter = 0
        for i in range(0,len(vertexes)):
            for j in vertexes[i]:
                plt.scatter(j.x, j.y,color = 'green',zorder=3) 
                plt.annotate(counter, (j.x+0.1, j.y))
                counter +=1


    def plot_visibility(self, visibility_edges):
        # The purpose of the function is to plot the visibility edges emanating from each vertex
        for j in visibility_edges:
            plt.plot([j.p1.x,j.p2.x], [j.p1.y,j.p2.y],color = 'blue',linestyle = 'dashed')   

    def get_vertexes_from_dict(self, v_dict): # This function retrieves vertexes from a dictionary of lists and converts it to a list of vertexes.
        vertexes = []
        for i in v_dict:
            for i in v_dict[i]:
                vertexes.append(i)
        return vertexes

    def plot_path(self, path, vertexes_list):
        for i in range(0, len(path)-1):
            plt.plot([vertexes_list[path[i]].x,vertexes_list[path[i+1]].x], [vertexes_list[path[i]].y,vertexes_list[path[i+1]].y],color = 'blue',linestyle = 'dashed') 





