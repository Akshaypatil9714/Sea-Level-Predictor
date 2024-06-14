# Sea-Level-Predictor
This project analyzes global average sea level changes since 1880 and predicts future changes through 2050 using historical data. The analysis includes visualizing the data with scatter plots and fitting linear regression models to estimate trends.

## Tasks
Import Data: 
-Use Pandas to import the data from epa-sea-level.csv.
-Create Scatter Plot: Use Matplotlib to create a scatter plot with the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
First Line of Best Fit:
-Use the linregress function from scipy.stats to determine the slope and y-intercept of the line of best fit.
-Plot this line of best fit over the scatter plot, extending it through the year 2050 to predict sea level rise.
Second Line of Best Fit:
-Filter the data to only include years from 2000 to the most recent year in the dataset.
-Use linregress to determine the slope and y-intercept for this subset of data.
-Plot this second line of best fit over the scatter plot, also extending it through the year 2050.
Labels and Title: 
-Add appropriate labels for the x-axis (Year), y-axis (Sea Level (inches)), and a title (Rise in Sea Level).

## Development
- sea_level_predictor.py: Contains the main function draw_plot() which performs the data analysis and visualization.
- main.py: Used to run and test the draw_plot() function.
- test_module.py: Contains unit tests for the project.
