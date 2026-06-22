# Retrieve basic information from the dataset
def get_dataset_info(df):

    # Extract the number of rows and columns
    rows, cols = df.shape

    # Count the total missing values in the dataset
    missing = df.isnull().sum().sum()

    # Return dataset details
    return rows, cols, missing


# Generate descriptive statistics for numerical columns
def get_summary_statistics(df):

    # Compute summary statistics and round to two decimal places
    return df.describe().round(2)