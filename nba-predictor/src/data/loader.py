def load_data(file_path):
    import pandas as pd
    
    # Load the data from a CSV file
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    # Perform data preprocessing steps
    # Example: Handle missing values, convert data types, etc.
    data.fillna(method='ffill', inplace=True)
    return data

def load_and_process_data(file_path):
    data = load_data(file_path)
    processed_data = preprocess_data(data)
    return processed_data