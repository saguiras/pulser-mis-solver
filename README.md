# Pulser Maximum Independent Set (MIS) Solver

This Python module uses the Pulser library to find the Maximum Independent Set (MIS) of antennas in a telecommunication network, taking into account interference constraints.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/saguiras/pulser-mis-solver.git
    cd pulser-mis-solver
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
    or
    ```bash
    pip install pulser && pip install networkx
    ```
    

## Usage

The main functionality of this module is encapsulated in the `MIS_pulser` function. To use it in your code, you can follow these steps:

```python

# Define antenna coordinates and interference distance
antennas_coordinates = [(0, 0), (3, 5.2), (6, 0), (9, -5.2), (9, 0), (9, 5.2), (9, 10.4), (12, 0)]
max_interference_distance = 8.7

# Find the MIS
result = MIS_pulser(antennas_coordinates, max_interference_distance)
print("Maximum Independent Set:", result)