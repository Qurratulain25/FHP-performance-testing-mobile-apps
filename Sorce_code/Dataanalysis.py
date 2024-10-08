import os
import pandas as pd

# Paths for the dataset and the folder containing combined files
dataset_folder = r'E:/Qurratulain/FHP-performance-testing-mobile-apps/dataset'
original_file_path = os.path.join(dataset_folder, 'Test Cases for all Applications.xlsx')

# Function to combine sheets of the same application
def combine_sheets(app_name, sheet_names, output_file):
    combined_df = pd.DataFrame()
    for sheet in sheet_names:
        try:
            df = pd.read_excel(original_file_path, sheet_name=sheet, engine='openpyxl')
            print(f"Loaded sheet '{sheet}' with {df.shape[0]} rows and {df.shape[1]} columns.")
            # Adjust columns if necessary
            if df.shape[1] < 24:
                df = df.reindex(columns=[*df.columns.tolist(), *[f"Unnamed: {i}" for i in range(df.shape[1], 24)]])
                print(f"Adjusted '{sheet}' to have 24 columns.")
            combined_df = pd.concat([combined_df, df], ignore_index=True)
        except Exception as e:
            print(f"Could not load sheet '{sheet}': {e}")
    
    # Save the combined file
    combined_file_path = os.path.join(dataset_folder, f"{app_name}_combined.xlsx")
    combined_df.to_excel(combined_file_path, index=False)
    print(f"Combined {app_name} data saved to {combined_file_path}")
    return combined_df

# Function to check if the combined data matches the original sheet data
def check_combined_data(app_name, sheet_names, combined_df):
    total_rows = 0
    for sheet in sheet_names:
        try:
            df = pd.read_excel(original_file_path, sheet_name=sheet, engine='openpyxl')
            total_rows += df.shape[0]
        except Exception as e:
            print(f"Could not load sheet '{sheet}': {e}")
    
    print(f"Total rows in original {app_name} sheets: {total_rows}")
    print(f"Total rows in combined {app_name} sheet: {combined_df.shape[0]}")
    
    if total_rows == combined_df.shape[0]:
        print(f"The combined sheet for {app_name} matches the original sheets row count.")
        return True
    else:
        print(f"The combined sheet for {app_name} does NOT match the original sheets row count.")
        return False

# Main process to combine and verify the sheets
def process_applications():
    # Dictionary of applications and their associated sheet names
    applications = {
        'ALI EXPRESS': ['ALI EXPRESS 1 USER', 'ALI EXPRESS 10 USER', 'ALI EXPRESS 50 USER'],
        'DARAZ': ['DARAZ 1 USER', 'DARAZ 10 USERS', 'DARAZ 50 USERS'],
        'EASY PAISA': ['EASY PAISA 1 USER', 'EASY PAISA 10 USERS', 'EASY PAISA 50 USER'],
        'PAYONEER': ['PAYONEER 1 USER', 'PAYONEER 10 USERS', 'PAYONEER 50 USERS'],
        'GITHUB': ['GITHUB 1 USER', 'GITHUB 10 USERS', 'GITHUB 50 USERS'],
        'UBL': ['UBL 1 USER', 'UBL 10 USERS', 'UBL 50 USERS'],
        'FOOD PANDA': ['FOOD PANDA 1 USER', 'FOOD PANDA 10 USERS', 'FOOD PANDA 50 USERS'],
        'UBER': ['UBER 1 USER', 'UBER 10 USERS', 'UBER 50 USERS'],
        'AIRBNB': ['AIRBNB 1 USER', 'AIRBNB 10 USERS', 'AIRBNB 50 USERS'],
        'DROPBOX': ['DROPBOX 1 USER', 'DROPBOX 10 USERS', 'DROPBOX 50 USERS']
    }

    for app_name, sheet_names in applications.items():
        print(f"\nProcessing {app_name}...")
        combined_df = combine_sheets(app_name, sheet_names, f"{app_name}_combined.xlsx")
        
        # Check if the data is combined correctly
        if not check_combined_data(app_name, sheet_names, combined_df):
            # If incorrect, delete the combined file and try again
            combined_file_path = os.path.join(dataset_folder, f"{app_name}_combined.xlsx")
            if os.path.exists(combined_file_path):
                os.remove(combined_file_path)
                print(f"Deleted incorrect combined file for {app_name}.")
            # Re-combine the sheets
            combined_df = combine_sheets(app_name, sheet_names, f"{app_name}_combined.xlsx")
            # Check again
            check_combined_data(app_name, sheet_names, combined_df)

# Run the process
if __name__ == "__main__":
    process_applications()
