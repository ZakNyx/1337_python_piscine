import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Parameters:
    -----------
    path : str
        The file path of the CSV file to be loaded.
        This must be a valid path pointing to a .csv file.

    Returns:
    --------
    pd.DataFrame
        A pandas DataFrame containing the data from the CSV file.
        Returns None if the path is incorrect or the file is not a CSV.

    Raises:
    -------
    AssertionError:
        If the file does not exist at the specified path.
        If the file is not of type CSV.
    """
    try:
        if not os.path.exists(path):
            raise AssertionError("Wrong Path!")
        if not path.lower().endswith(".csv"):
            raise AssertionError("Wrong file type")
        df = pd.read_csv(path)
        print(f'Loading dataset of dimensions {df.shape}')
        return df
    except AssertionError as e:
        print(f'{AssertionError.__name__}: {e}')
        return None
