# A* Path Planning Algorihtm on a Visibility Graph Built Using the Rotational Plane Sweep Algorithm

The present code is an implementation of the classical A* path planning algorithm on a Visibility Graph. The Visibility graph vertexes and edges are stored on the directories environmets (vertices) and graph_environments (edges) respectively.

The code implementation has a CLI to execute it as follows.

`python main.py environments/env_X.csv graph_environments/visibility_graph_env_X.csv`  where X is the environment number and it has to be the same for both arguments. Some execution examples are using the following commands.

The **start** and **goal** nodes (positions) are the first and last elements of the `env_X.csv` file respectively.

### Non-Convex Polygon

`python main.py environments/env_0.csv graph_environments/visibility_graph_env_0.csv`

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1bzxDYoWVYqHxWEl5pGydyXTdJLaUoFlq" width="300" height="300" />
</p>


### Mexico

`python main.py environments/env_11.csv graph_environments/visibility_graph_env_11.csv`

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=1hvctv4oRBdlHbB6y_C24xtVFETAciEag" width="400" height="300" />
</p>


