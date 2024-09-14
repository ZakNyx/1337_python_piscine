import matplotlib.pyplot as plt
from load_csv import load
import numpy as np


def convert_population_to_float(population):
    """
    Converts a population string to a float.
    
    This function converts population values that may contain the letter 'M' 
    (representing millions) into a float. If a value contains 'M', it will 
    be multiplied by 1,000,000. If the value does not contain 'M', it will 
    be directly converted to a float.

    Parameters:
    -----------
    population : array-like
        A sequence of population values (strings) to be converted to floats.

    Returns:
    --------
    np.array
        A NumPy array of the converted population values in floats.
    """
    converted_population = []
    for value in population:
        if 'M' in value:
            converted_population.append(float(value.replace('M', '')) * 1e6)
        else:
            converted_population.append(float(value))
    return np.array(converted_population)


def show_plot_population(years, populationMA, populationFR):
    """
    Plots population projections for Morocco and France over time.

    This function takes years and the populations of Morocco and France, 
    scales the population down to millions, and creates a line plot 
    comparing the population trends over time.

    Parameters:
    -----------
    years : array-like
        A sequence of years to be plotted on the x-axis.

    populationMA : array-like
        The population data of Morocco to be plotted.

    populationFR : array-like
        The population data of France to be plotted.
    """
    # Plot Morocco and France population data
    plt.plot(years, populationMA, label="Morocco", color="red")
    plt.plot(years, populationFR, label="France", color="green")

    # Label the axes
    plt.xlabel("Year")
    plt.ylabel("Population (M)")

    # Set x-ticks at regular intervals
    plt.xticks(years[::40])

    # Find the maximum population value
    max_population = max(populationMA.max(), populationFR.max())

    # Dynamically create Y-ticks at regular intervals
    yticks = np.arange(20, max_population , 20)

    plt.yticks(yticks)

    # Limit the x-axis to a maximum year of 2050
    plt.xlim([years.min(), 2050])

    # Add a title and legend
    plt.title("Population Projections")
    plt.legend()

    # Display the plot
    plt.show()


def main():
    """
    Loads population data and displays population projections for 
    Morocco and France.

    The main function loads the population data from a CSV file, filters 
    for Morocco and France, converts the population data from strings 
    to floats, scales the population to millions, and finally displays 
    the plot using `show_plot_population`.
    """
    dataset = load("population_total.csv")

    # Filter for Morocco and France
    moroccoData = dataset[dataset["country"] == "Morocco"]
    franceData = dataset[dataset["country"] == "France"]

    # Get years and population data, assuming the first column is 'year'
    years = moroccoData.columns[1:].astype(int)

    # Convert population data to float and handle 'M' for millions
    populationMA = convert_population_to_float(moroccoData.values[0][1:])
    populationFR = convert_population_to_float(franceData.values[0][1:])

    # Convert to millions
    populationMA = populationMA / 1e6  
    populationFR = populationFR / 1e6  

    # Show the plot
    show_plot_population(years, populationMA, populationFR)


if __name__ == "__main__":
    main()
