import pandas as pd

# File path to your dataset
file_path = r'E:/Qurratulain/FHP-performance-testing-mobile-apps/dataset/Test Cases for all Applications.xlsx'

# List of applications to merge (you can modify this for other applications)
applications_to_merge = {
    'Dropbox': ['Dropbox_1_User', 'Dropbox_10_User', 'Dropbox_50_User'],
    # Add other applications here if necessary
    'Dropbox': ['Dropbox_1_User', 'Dropbox_10_User', 'Dropbox_50_User'],
    'Easy Paisa': ['Easy Paisa_1_User', 'Easy Paisa_10_User', 'Easy Paisa_50_User'],
    'ALI EXPRESS': ['ALI EXPRESS_1_User', 'ALI EXPRESS_10_User', 'ALI EXPRESS_50_User'],
    'DARAZ': ['DARAZ_1_User', 'DARAZ_10_User', 'DARAZ_50_User'],
    'PAYONEER': ['PAYONEER_1_User', 'PAYONEER_10_User', 'PAYONEER_50_User'],
    'GITHUB': ['GITHUB_1_User', 'GITHUB_10_User', 'GITHUB_50_User'],
    'UBL': ['UBL_1_User', 'UBL_10_User', 'UBL_50_User'],
    'FOOD PANDA': ['FOOD PANDA_1_User', 'FOOD PANDA_10_User', 'FOOD PANDAx_50_User'],
    'UBER': ['UBER_1_User', 'UBER_10_User', 'UBER_50_User'],
     'AIRBNB': ['AIRBNB_1_User', 'AIRBNB_10_User', 'AIRBNB_50_User'],
      
}

# Function to merge sheets of the same application
def merge_application_sheets(app_name, sheet_names, output_file):
    merged_data = pd.DataFrame()

    # Loop through each sheet and append its data
    for sheet_name in sheet_names:
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
            merged_data = pd.concat([merged_data, df], ignore_index=True)
            print(f"Successfully merged {sheet_name}")
        except FileNotFoundError:
            print(f"File not found: {sheet_name}")
        except Exception as e:
            print(f"Error reading {sheet_name}: {e}")

    # Save the merged data to a new file
    merged_data.to_excel(output_file, index=False)
    print(f"Combined {app_name} data saved to {output_file}")

# Run the merge for each application
for app, sheets in applications_to_merge.items():
    output_file_path = f'E:/Qurratulain/FHP-performance-testing-mobile-apps/dataset/{app}_combined.xlsx'
    merge_application_sheets(app, sheets, output_file_path)
