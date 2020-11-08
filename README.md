<br />
<p align="center">
  <h1 align="center">BaD simulation</h1>

  <p align="center">
    A Simulation of the Effects of Tailgating on Traffic Flow.
  </p>
</p>

## About The Project
In this project we extend the NaSh model with tailgaters. This model is called the Bugel and Dijkstra model (BaD model).

## Getting Started
For this project we are using Python 3

Open the terminal and navigate to the root folder of the project.
Next, navigate to the src folder.

When you download Python, pip will automatically be installed. In order to make sure that pip is up to date, we can use the following command:

```
  python3 -m pip install --upgrade pip
```

First we will set up the virtual environment for python:
```
  python3 -m venv env
```

And we activate it using

```
  source env/bin/activate
```

Next we will install all the necessary packages. These packages are defined inside the requirements.txt

```
  pip install -r requirements.txt --no-cache-dir
```

If the above command did not work, try instead

```
  python3 -m pip install -r requirements.txt --no-cache-dir
```

Finally to run the application you can run
```
  python3 startSimulation.py
```

In the config file you can change different parameters of the model.
The parameters as they are in the config file are also the ones used in the paper.

## Overview
The simulation is composed of three important classes.

### Simulation

The backbone of the simulation, the starting point to start running the simulation (together with the \_\_init__ file).

### Highway

The highway, which consists of all cars, and executes all the simulation steps for all the cars.
It also keeps track of the data so that this can be used for the final plots.

### Car

The car class has the current position and velocity of the car.
It also knows wether or not it is a 'Tokkie' (Tailgater), also all steps are defined here, which are called from the highway class.