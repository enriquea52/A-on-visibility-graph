#!/usr/bin/env python3
import csv
import numpy as np
import matplotlib.pyplot as plt
import time
import sys

from lab import visibility
import as_utils
import a_star

if __name__ == "__main__":

    # Retrieve information from the command line ################################################## 
    if len(sys.argv) !=3:
        print("You should provide the path to the csv environment and to the visibility edges csv: ")
        print("Provide the correct number of arguments (2) in the following format as str: ")
        print("Path to env_X.csv, Path to visibility_graph_env_X.csv,  where X is the environment number")
        exit()
    else:
        path_env = sys.argv[1]
        path_graph = sys.argv[2]

    print("Specified environment: ", path_env,"Specified visibility graph: ", path_graph,"\n")
    #################################################################################################

    if (path_env[-5] != path_graph[-5]):
        print("Please make sure the environment csv file\n")
        print("and the visibility_graph csv file correspond to one another\n")
        print("For example: env_X.csv and visibility_graph_env_X.csv, where X is exactly the same number")
        exit()



    
    graph = visibility(path_env)

    E , vertexes_dict = graph.get_edges_vertexes()

    graph.plot_edges(E)

    graph.plot_vertexes(vertexes_dict)

    vertexes_list = graph.get_vertexes_from_dict(vertexes_dict) #This is the one to be used

    vedges,visibility_edges = graph.get_visibility_edges(path_graph,vertexes_list)

    graph.plot_edges(visibility_edges, ecolor='red', estyle='dashed', width=1.5)


    # A* path finding algorithm implementation--------------------------------------------------------
    
    start_node = 0

    goal_node = len(vertexes_list)-1

    path, total_cost = a_star.path_finder(start_node, goal_node, vertexes_list, vedges)

    # -----------------------------------------------------------------------------------

    # Plot path --------------------------------------------------------
    graph.plot_path( path, vertexes_list)
    print("Path: ",list(reversed(path)))

    # Print Total Cost -------------------------------------------------
    print("Distance: ",total_cost)


    plt.show()