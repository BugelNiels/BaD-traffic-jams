<br />
<p align="center">
  <h1 align="center">BaD simulation</h1>

  <p align="center">
    A Simulation of the Effects of Tailgating on Traffic Flow
  </p>
</p>

## About The Project
In this project we extend the NaSh model with tailgaters.

## Getting Started
Install a virtual environment. 
pip install all of the packages defined in requirements.txt
And then run python startSimulation.py

In the config file you can change different parameters of the model, which is also done in the paper.

## Overview
The simulation excist of three subclasses
### Simulation
The backbone of the simulaion, the starting point to start running the simulation (together with the \_\_init__ file).

### Hightway
The highway, which concists of all cars, and does all the steps for all the cars.
It also saves the history for the final plots

### Car
The car class has the current position and velocity of the car.
It also knows wether or not it is a 'Tokkie', also all steps are defined here, which are called from the highway class.