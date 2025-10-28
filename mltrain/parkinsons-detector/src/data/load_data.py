def load_data(file_path):
    """
    Load the dataset from a specified CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing the dataset.

    Returns:
    DataFrame: A pandas DataFrame containing the loaded data.
    """
    import pandas as pd

    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def load_data_from_database(connection_string, query):
    """
    Load the dataset from a database using a SQL query.

    Parameters:
    connection_string (str): The connection string for the database.
    query (str): The SQL query to execute.

    Returns:
    DataFrame: A pandas DataFrame containing the loaded data.
    """
    import pandas as pd
    from sqlalchemy import create_engine

    try:
        engine = create_engine(connection_string)
        data = pd.read_sql(query, engine)
        return data
    except Exception as e:
        print(f"Error loading data from database: {e}")
        return None