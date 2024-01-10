# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 14:34:53 2024

@author: losir
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

from matplotlib.gridspec import GridSpec

# Plot 1 Sales and Profit per Monthly
def plot_line(df, grid):
    plt.subplot(grid[0 , 0])
    #print( df.columns)
    month_Sales = df.groupby(['year','month'])['Sales'].sum().reset_index()
    month_Profit = df.groupby(['year','month'])['Profit'].sum().reset_index()
    month_Sales['year_month'] = month_Sales['year'].astype(str) + '-' + month_Sales['month'].astype(str)
    month_Profit['year_month'] = month_Profit['year'].astype(str) +'-' + month_Profit['month'].astype(str)
# Set the figure Size
    
    ax= sns.lineplot(data=month_Sales, x="year_month", y="Sales", label = "Sales")
    ax = sns.lineplot(data=month_Profit, x="year_month", y="Profit", label = "Profit")
    plt.xlabel("Year and month")
    plt.ylabel("Profit and Sales(USD)")
    plt.title("Sales and Profit Trends Across Years & Months")
    ax.xaxis.set_major_locator(ticker.MultipleLocator(6))
    #plt.legend()
    #fig.show()
    #plt.show()
  


# plot 2 Quantity by Category and Segment
def bar_plot_v(df, grid):
    plt.subplot(grid[0 , 1])
    df = pd.DataFrame(df)

    # Group by 'Category' and 'Segment' and sum the 'Quantity'
    grouped_df = df.groupby(['Category', 'Segment'])[['Quantity']].sum().reset_index()

    # Create a bar plot using plt.bar
    categories = grouped_df['Category'].unique()
    bar_width = 0.15  # Width of each bar
    index = range(len(categories))

    for i, segment in enumerate(grouped_df['Segment'].unique()):
        segment_data = grouped_df[grouped_df['Segment'] == segment]
        plt.bar([pos + i * bar_width for pos in index], segment_data['Quantity'], width=bar_width, label=segment)

    # Adding labels and title
    plt.legend(loc='upper left')
    plt.xlabel('Category')
    plt.ylabel('Quantity')
    plt.title('Quantity by Category and Segment')

    # Adding x-axis labels and legend
    plt.xticks([pos + bar_width for pos in index], categories)
    #plt.legend()

    # Show the plot
    #plt.show()
    
#plot 3
def pie_plot(df, grid):
    plt.subplot(grid[0 , 2])
    temp=pd.DataFrame(df.groupby('State')['Quantity'].sum().reset_index())
    temp = temp.sort_values('Quantity', ascending=False).head(10)
    explode = [0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0]   
    plt.pie(temp['Quantity'], labels=temp['State'], explode=explode, autopct='%1.1f%%')
    plt.title('Purchase rate in different states')

#plot 4
def bar_plot(df, grid):
    ax = plt.subplot(grid[1 , 2])
# Creating a DataFrame with sub-category sales data
    df = pd.DataFrame(df)

    sub_df = df.groupby('Sub-Category', as_index=False)['Sales'].sum().sort_values(by='Sales')

    ax.barh(sub_df['Sub-Category'], sub_df['Sales'])
    ax.set_xlabel('Sales')
    ax.set_ylabel('Sub-Category')
    ax.set_title('Sales by Sub-Category')

def print_detail():
    # Add a subplot for key insights
    plt.subplot(grid[1 , 1])
    text = "Highlights:\n\n" \
           "1. Profit is less  with the Sales compared\n"\
               "accross the Superstore.\n" \
           "2. Highest demand for office supplies is \n"\
               "from the consumer segment.\n" \
           "3.California has the highest purchase \n"\
               " among the top 10 cities in USA \n" \
           "4. Phones and Chairs are the highest \n" \
           "   Sub -category product from the Sales."
    plt.text(0.5 , 0.5 , text , ha='center' , va='center' , fontsize=12 ,
             color='gray' , fontstyle='italic' , fontweight='bold')
    plt.axis('off')

    # Add student information
    plt.subplot(grid[1 , 0])
    text = "Student Name: Changdra Shekar Losirlu\n" \
           "Student ID: 22081216"
    plt.text(0.5 , 0.5 , text , ha='center' , va='center' , fontsize=12 , color='gray' , fontweight='bold')
    plt.axis('off')

    # Main title for the entire dashboard
    fig.suptitle('Superstore Sales and Profit  Analysis Dashboard' , fontsize=25 , fontweight='bold')
    

#######################Main ##########################


df = pd.read_csv("Sample - Superstore.csv")
df['Order Date'] = df['Order Date'].str.replace('-', '/')
df['Ship Date'] = df['Ship Date'].str.replace('-', '/')
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%m/%d/%Y')
df['year']=df['Order Date'].dt.year
df['month'] = df['Order Date'].dt.month
sns.set_theme()
fig = plt.figure(figsize=(18 , 10),dpi=300)
grid = GridSpec(2 , 3 , width_ratios=[1 , 1 , 1] , height_ratios=[1 , 1])
plt.savefig('22081216.png' , dpi=300)


plot_line(df,grid)
bar_plot_v(df,grid)
pie_plot(df,grid)
bar_plot(df,grid)
print_detail()
plt.savefig('22081216.png' , dpi=300)

plt.show()