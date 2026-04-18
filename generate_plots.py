"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np


def generate_data(seed=None):
    """Generate synthetic sensor temperature data.

    Parameters
    ----------
    seed : int or None
        Seed for NumPy's random number generator. If None, the generator
        is initialized without a fixed seed.

    Returns
    -------
    sensor_a : ndarray, shape (200,)
        Simulated temperature readings from Sensor A in degrees Celsius.
    sensor_b : ndarray, shape (200,)
        Simulated temperature readings from Sensor B in degrees Celsius.
    timestamps : ndarray, shape (200,)
        Uniformly distributed timestamps from 0 to 10 seconds.
    """
    rng = np.random.default_rng(seed)
    sensor_a = rng.normal(loc=25, scale=3, size=200)
    sensor_b = rng.normal(loc=27, scale=4.5, size=200)
    timestamps = rng.uniform(low=0, high=10, size=200)
    return sensor_a, sensor_b, timestamps

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Create a scatter plot of sensor temperature readings over time.

    Parameters
    ----------
    sensor_a : array_like, shape (n,)
        Temperature readings from Sensor A in degrees Celsius.
    sensor_b : array_like, shape (n,)
        Temperature readings from Sensor B in degrees Celsius.
    timestamps : array_like, shape (n,)
        Time values in seconds corresponding to the sensor readings.
    ax : matplotlib.axes.Axes
        The Axes object on which to draw the scatter plot.

    Returns
    -------
    None
        Modifies the input Axes object in place.
    """
    ax.scatter(timestamps, sensor_a, color='blue', label='Sensor A', alpha=0.7)
    ax.scatter(timestamps, sensor_b, color='orange', label='Sensor B', alpha=0.7)
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Sensor Temperature Readings Over Time')
    ax.legend()
    ax.grid(True, alpha=0.3)


# Create plot_histogram(sensor_a, sensor_b, ax) that draws
# the overlaid histogram from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_histogram(sensor_a, sensor_b, ax):
    """Create an overlaid histogram of sensor temperature distributions.

    Parameters
    ----------
    sensor_a : array_like, shape (n,)
        Temperature readings from Sensor A in degrees Celsius.
    sensor_b : array_like, shape (n,)
        Temperature readings from Sensor B in degrees Celsius.
    ax : matplotlib.axes.Axes
        The Axes object on which to draw the histogram.

    Returns
    -------
    None
        Modifies the input Axes object in place.
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, color='blue', label='Sensor A', edgecolor='black', linewidth=0.5)
    ax.hist(sensor_b, bins=30, alpha=0.5, color='orange', label='Sensor B', edgecolor='black', linewidth=0.5)

    # Add vertical lines at the means
    ax.axvline(np.mean(sensor_a), color='blue', linestyle='--', linewidth=2, label=f'Sensor A mean: {np.mean(sensor_a):.1f}°C')
    ax.axvline(np.mean(sensor_b), color='orange', linestyle='--', linewidth=2, label=f'Sensor B mean: {np.mean(sensor_b):.1f}°C')

    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    ax.set_title('Temperature Distribution Comparison')
    ax.legend()
    ax.grid(True, alpha=0.3)


# Create plot_boxplot(sensor_a, sensor_b, ax) that draws
# the side-by-side box plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_boxplot(sensor_a, sensor_b, ax):
    """Create a side-by-side box plot comparing sensor temperature distributions.

    Parameters
    ----------
    sensor_a : array_like, shape (n,)
        Temperature readings from Sensor A in degrees Celsius.
    sensor_b : array_like, shape (n,)
        Temperature readings from Sensor B in degrees Celsius.
    ax : matplotlib.axes.Axes
        The Axes object on which to draw the box plot.

    Returns
    -------
    None
        Modifies the input Axes object in place.
    """
    ax.boxplot([sensor_a, sensor_b], labels=['Sensor A', 'Sensor B'], patch_artist=True,
               boxprops=dict(facecolor='lightblue', edgecolor='black'),
               medianprops=dict(color='red'),
               whiskerprops=dict(color='black'),
               capprops=dict(color='black'))

    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    ax.axhline(overall_mean, color='gray', linestyle='--', linewidth=2,
               label=f'Overall mean: {overall_mean:.2f}°C')

    ax.set_ylabel('Temperature (deg C)')
    ax.set_title('Sensor Temperature Distribution Comparison')
    ax.legend()
    ax.grid(True, alpha=0.3)


# Create main() that generates data, creates a 1x3 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.

def main():
    """Generate and save sensor data analysis plots.

    Creates synthetic temperature sensor data and produces three visualizations
    (scatter plot, histogram, and box plot) arranged in a single figure,
    then saves the result as a high-resolution PNG file.

    Returns
    -------
    None
        Saves plot to 'sensor_analysis.png' in the current directory.
    """
    # Generate the sensor data
    sensor_a, sensor_b, timestamps = generate_data(seed=1234)

    # Create a 1x3 subplot figure
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Create each plot
    plot_scatter(sensor_a, sensor_b, timestamps, axes[0])
    plot_histogram(sensor_a, sensor_b, axes[1])
    plot_boxplot(sensor_a, sensor_b, axes[2])

    # Adjust layout and save
    plt.tight_layout()
    plt.savefig('sensor_analysis.png', dpi=150, bbox_inches='tight')
    plt.close()


if __name__ == '__main__':
    main()