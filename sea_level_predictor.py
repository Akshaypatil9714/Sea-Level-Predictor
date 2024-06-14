import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("/workspace/boilerplate-sea-level-predictor/epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(20,12))
    df.plot(kind='scatter', x='Year', y='CSIRO Adjusted Sea Level', label='Original Data')
    


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = list(range(1880, 2051))
    y_pred = [slope * x + intercept for x in x_pred]
    plt.plot(x_pred, y_pred, label=f'Original Fit (R-squared: {round(r_value**2, 2)})')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = list(range(2000, 2051))
    y_pred_recent = [slope_recent * x + intercept_recent for x in x_pred_recent]
    plt.plot(x_pred_recent, y_pred_recent, label='Recent Fit')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()