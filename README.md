# Sensor Plot Generator

A small script that generates synthetic temperature sensor data and creates three publication-quality visualizations in a single output image.

## Installation

1. Activate the `ece105` conda environment:

```bash
conda activate ece105
```

2. Install the required dependencies inside that environment:

```bash
conda install numpy matplotlib
```

If you prefer `mamba`, use:

```bash
mamba install numpy matplotlib
```

## Usage

Run the script from the project directory:

```bash
python generate_plots.py
```

## Example output

The script generates a single PNG file named `sensor_analysis.png` containing three side-by-side plots:

- A scatter plot of Sensor A and Sensor B temperature readings over time
- An overlaid histogram comparing the two temperature distributions
- A side-by-side box plot showing the distribution and overall mean for both sensors

## AI tools used and disclosure

This README and parts of the code were generated with the assistance of GitHub Copilot.
