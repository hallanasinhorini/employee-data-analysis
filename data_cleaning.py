import pandas as pd

# Load the dataset
def load_data(file_path):
    df = pd.read_csv(file_path)  # Update with the actual file format if necessary
    return df

# Handle missing values
def handle_missing_values(df):
    # Example: Fill missing salary values with the median salary
    df['salary'].fillna(df['salary'].median(), inplace=True)
    return df

# Remove duplicates
def remove_duplicates(df):
    df.drop_duplicates(inplace=True)
    return df

# Correct data types
def correct_data_types(df):
    # Example: Convert 'hire_date' column to datetime
    df['hire_date'] = pd.to_datetime(df['hire_date'])
    return df

if __name__ == "__main__":
    file_path = "data/employee_data.csv"  # Update with the actual file path
    employee_data = load_data(file_path)
    
    # Perform data cleaning steps
    employee_data = handle_missing_values(employee_data)
    employee_data = remove_duplicates(employee_data)
    employee_data = correct_data_types(employee_data)
    
    # Save cleaned data to a new CSV file
    employee_data.to_csv("data/cleaned_employee_data.csv", index=False)
