author: Alex Camilleri
---- Agent-based Modelling
---- GEOG5003M Programming for Geographical Information Analysis
---- Model
---- Version 0.8

# [Project 1: Agent-based model](https://github.com/Jiinglelocks/Agent-based-modelling/tree/main/Model)
Description:
* Generate agents and predators on a digital elevation model
* Agents eat from the landscape, share resources between them if close to eachother.
* These resources are stored in their energy stores, which are depleted as they move (and vomited if they eat too much!)
* Agents will also reproduce asexually when conditions are just right.
* Predators move faster than agents and will eat them when close enough, jumping to the agent's position in space.
* All plotted in an interface as an animation, will output total energy and the post-activity environment as .txt files to the directory.

Skills:
* Learned in-depth python functionality; loops, list/2d lists, slicers, conditionals, functions, read/write files to directory and into functions/classes,
* Created classes with methods and sub-classes making use of inheritence,
* Plotted results in single frame and animated format,
* Created an interface using Tkinter,
* Webscraped data to intitialise the model,

Setup Notes:
* Uses two script files; agentframework.py and model.py which should be placed in the same directory, as well as a 300x300 grid of CSV's in .txt format. 
* Agentframework.py contains an environment generating function, an Agent superclass and a Predator sub-class.
* The model should be run from Model.py, and parameters (num_of_agents, num_of_predators, num_of_iterations and neighbourhood) to be set within source code of model.py
* Makes use of BeautifulSoup webscraping to initialise agents/predators x and y values from [this data](https://jiinglelocks.github.io/Agent-based-modelling/Model/data2.html)
* Agents move freely around a torus environment, eating from it, sharing resources and reproducing.
* Includes rudimentary GUI.
* Will output total energy and the post-activity environment as .txt files to the directory.
* Dependencies: random, operator, tkinter, matplotlib, csv, requests, bs4 (beautifulsoup), agentframeworklib, csv, requests, bs4 (beautifulsoup), agentframework