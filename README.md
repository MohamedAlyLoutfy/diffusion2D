# diffusion2D

## Instructions for students

Please follow the instructions in [pypi_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/pypi_exercise.md).

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).

## Project description

`diffusion2D` is a Python package that numerically solves the 2D diffusion equation using the Finite Difference Method. The package simulates the process of heat diffusion in a square domain, with a circular heat source at the center. The simulation produces visual plots showing the temperature distribution at various time steps.

### Features:
- Solves the 2D diffusion equation numerically for a given domain and initial conditions.
- Visualizes the temperature distribution over time using Matplotlib.
- Parameters such as grid spacing (`dx`, `dy`) and thermal diffusivity (`D`) can be customized.

---

## Installing the package

### Using pip3 to install from PyPI
Once the package is uploaded to PyPI, you can install it using pip:
```bash
pip install --user --index-url https://test.pypi.org/simple/ youssemd_diffusion2d
