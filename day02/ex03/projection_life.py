from load_csv import load
import matplotlib.pyplot as plt


def show_graph(income, expectancy):
    """
    Generates and displays a scatter plot of life expectancy versus income for the year 1900.

    Parameters:
    - income (pd.Series): The income data for the year 1900.
    - expectancy (pd.Series): The life expectancy data for the year 1900.
    """
    plt.scatter(income, expectancy)
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life Expectancy")
    plt.title("Life Expectancy in Relation to the Gross National Product of the Year 1900")
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.show()


def main():
    """
    Main function to load data and display the scatter plot.
    """
    # Load datasets
    dataset_income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    dataset_expectancy = load("life_expectancy_years.csv")

    # Extract data for the year 1900
    expectancy = dataset_expectancy['1900']
    income = dataset_income['1900']

    # Display the scatter plot
    show_graph(income, expectancy)


if __name__ == "__main__":
    main()
