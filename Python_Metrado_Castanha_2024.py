
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

## Load the CSV file
file_path = 'data\DB_Castanha_cassia_04_02_2024.csv'
data = pd.read_csv(file_path)
# Load the Excel file


#data  = pd.ExcelFile(file_path)
# Display sheet names to understand its structure
sheet_names = data.sheet_names
sheet_names

# Display the first few rows of the dataframe for an initial overview
print(data.head())

# Basic statistics for the dataset
basic_stats = data.describe()
print(basic_stats)

# Setting the style for the plots
sns.set(style="whitegrid")

# Load the complete data from both sheets for detailed analysis
sheet1_data = pd.read_excel(xls, sheet_name=sheet_names[0])
sheet2_data = pd.read_excel(xls, sheet_name=sheet_names[1])

# Display the first few rows of each dataset to confirm successful loading and to plan the next steps of analysis
sheet1_data_head = sheet1_data.head()
sheet2_data_head = sheet2_data.head()

sheet1_data_head, sheet2_data_head


# Descriptive statistics for physical growth parameters (diameter and height) from the first sheet
# Calculate descriptive statistics for diameter and height grouped by treatment
descriptive_stats_growth = sheet1_cleaned.groupby('TRATAMENTO').agg(['mean', 'median', 'std', 'min', 'max'])

descriptive_stats_growth

# Cleaning up the second sheet's data for analysis
# Renaming columns for clarity based on the preview
sheet2_data.columns = ['Treatment', 'Repetition', 'Cla_Date', 'Clb_Date', 'A.FOL_Date', 'PFPA_Date', 'PSPA_Date', 'PFR_Date', 'PSR_Date', 'CR_Date']

# Dropping the first row which contained date information, not useful for numeric analysis
sheet2_data_cleaned = sheet2_data.drop(index=0)

# Convert numeric columns to float for analysis
numeric_cols = sheet2_data_cleaned.columns[2:]  # Assuming all columns after 'Repetition' are numeric
sheet2_data_cleaned[numeric_cols] = sheet2_data_cleaned[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Calculate descriptive statistics for physiological parameters grouped by treatment
descriptive_stats_physio = sheet2_data_cleaned.groupby('Treatment').agg(['mean', 'median', 'std', 'min', 'max'])

descriptive_stats_physio

from scipy import stats

# Selecting key growth parameters: Plant Height and Diameter at Collection
height_data = sheet1_cleaned[['TRATAMENTO', 'ALTURA_PLANTA']]
diameter_data = sheet1_cleaned[['TRATAMENTO', 'DIAM_COLETO']]

# Preparing data for ANOVA
height_groups = [height_data['ALTURA_PLANTA'][height_data['TRATAMENTO'] == i] for i in height_data['TRATAMENTO'].unique()]
diameter_groups = [diameter_data['DIAM_COLETO'][diameter_data['TRATAMENTO'] == i] for i in diameter_data['TRATAMENTO'].unique()]

# Performing ANOVA for Plant Height and Diameter
anova_height = stats.f_oneway(*height_groups)
anova_diameter = stats.f_oneway(*diameter_groups)

anova_height, anova_diameter

# Create a figure for 2 subplots (side by side)
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Boxplot for Plant Height
sns.boxplot(x='TRATAMENTO', y='ALTURA_PLANTA', data=sheet1_cleaned, ax=axes[0])
axes[0].set_title('Distribution of Plant Height by Treatment')
axes[0].set_xlabel('Treatment')
axes[0].set_ylabel('Plant Height (cm)')

# Boxplot for Diameter at Collection
sns.boxplot(x='TRATAMENTO', y='DIAM_COLETO', data=sheet1_cleaned, ax=axes[1])
axes[1].set_title('Distribution of Diameter at Collection by Treatment')
axes[1].set_xlabel('Treatment')
axes[1].set_ylabel('Diameter at Collection (cm)')

plt.tight_layout()
plt.show()
# Assuming 'Cla_Date' as a placeholder for a physiological parameter for visualization
# Note: The actual parameter for detailed physiological analysis should be selected based on scientific relevance

# Boxplot for a Physiological Parameter (using 'Cla_Date' as a placeholder)
plt.figure(figsize=(8, 6))
sns.boxplot(x='Treatment', y='Cla_Date', data=sheet2_data_cleaned)
plt.title('Distribution of a Physiological Parameter by Treatment')
plt.xlabel('Treatment')
plt.ylabel('Physiological Parameter Value')
plt.show()


# Hypothetical correlation analysis - selecting parameters for demonstration
# For accurate analysis, ensure parameters are properly aligned and represent the same samples

# Creating a hypothetical combined dataset with selected parameters
# Here, 'Cla_Date' is used as a placeholder for a physiological parameter. Actual analysis should use relevant parameters.
combined_data_hypothetical = sheet1_cleaned[['ALTURA_PLANTA', 'DIAM_COLETO']].copy()
combined_data_hypothetical['Physiological_Param'] = sheet2_data_cleaned['Cla_Date'].values

# Calculating the correlation matrix
correlation_matrix = combined_data_hypothetical.corr()

# Visualizing the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Growth and Physiological Parameters')
plt.show()
