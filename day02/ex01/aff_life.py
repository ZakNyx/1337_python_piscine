import matplotlib.pyplot as plt
from load_csv import load


def plot_life_expectancy(years, life_expectancy, tick_frequency=40):
    """
    Plot life expectancy over a range of years with a customizable tick 
    frequency on the x-axis.

    Parameters:
    -----------
    years : array-like
        A sequence of years representing the x-axis values.

    life_expectancy : array-like
        A sequence of life expectancy values corresponding to the years.

    tick_frequency : int, optional, default=40
        The frequency (interval) of the ticks displayed on the x-axis. 
        For example, if tick_frequency=40, x-axis labels will be shown 
        every 40 years.

    Returns:
    --------
    None
        The function plots the data and displays the figure. No value 
        is returned.
    """
    plt.plot(years, life_expectancy)
    plt.xlabel("Years")
    plt.ylabel("Life Expectancy")
    plt.title("Life Expectancy in Morocco Projections")

    # Customize x-axis ticks to show at every tick_frequency interval
    plt.xticks(years[::tick_frequency])

    # Display the plot
    plt.show()


def main():
    """
    Main function that loads life expectancy data and plots Morocco's life 
    expectancy over time.

    This function uses the `load` function to load a dataset from a CSV file,
    filters the dataset for Morocco, extracts the relevant columns (years and
    life expectancy), and passes them to the `plot_life_expectancy` function
    for visualization.

    >>> main()
    """
    # Load dataset
    dataset = load("life_expectancy_years.csv")

    # Filter for Morocco's life expectancy data
    morocco_life_expectancy = dataset[dataset['country'] == "Morocco"]

    # Get years and life expectancy values, convert years to integers
    years = morocco_life_expectancy.columns[1:].astype(int)
    life_expectancy = morocco_life_expectancy.values[0][1:]

    # Call the plot function
    plot_life_expectancy(years, life_expectancy)


if __name__ == "__main__":
    main()
