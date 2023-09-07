import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
def load_cleaned_data(file_path):
    df = pd.read_csv(file_path)  # Update with the actual file format if necessary
    return df

# Calculate summary statistics
def calculate_summary_statistics(df):
    summary = df.describe()
    return summary

# Create visualizations
def create_visualizations(df):
    # Example: Create a histogram of employee ages
    plt.figure(figsize=(10, 6))
    sns.histplot(df['age'], bins=20, kde=True)
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Distribution of Employee Ages')
    plt.show()

if __name__ == "__main__":
    cleaned_data_path = "data/cleaned_employee_data.csv"  # Update with the actual file path
    cleaned_employee_data = load_cleaned_data(cleaned_data_path)
    
    # Perform data analysis steps
    summary_statistics = calculate_summary_statistics(cleaned_employee_data)
    create_visualizations(cleaned_employee_data)
