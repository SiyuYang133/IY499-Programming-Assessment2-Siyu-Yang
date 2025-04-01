import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import statistics 
 
#Get data and save into csv file using Pandas 
def get_user_data():
    print("Enter numerical data separated by commas (e.g., 5,10,15,20):")
    user_input = input()
    try:
        data = [float(num.strip()) for num in user_input.split(',') if num.strip()]
        df = pd.DataFrame({'Data': data})
        df.to_csv('raw_data.csv', index=False)
        print("Data saved to raw_data.csv")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
     
#Read numerical data from CSV file using Panda 
def read_data():
    df = pd.read_csv('raw_data.csv')
    return df['Data'].tolist()
     
#Compute mean, median, mode, modal class, variance, and standard deviation using Statistics 
 
def compute_statistics(data, grouped_df, frequency, midpoints):
    mean = statistics.mean(data)
    median = statistics.median(data)
    try:
        mode = statistics.mode(data)
    except statistics.StatisticsError:
        mode = "No unique mode"

    modal_class_index = np.argmax(frequency)
    modal_class = grouped_df.iloc[modal_class_index]['Class Interval']
    
    variance = statistics.variance(data)
    std_dev = statistics.stdev(data)
    
    stats_df = pd.DataFrame({
        'Statistic': ['Mean', 'Median', 'Mode', 'Modal Class', 'Variance', 'Standard Deviation'],
        'Value': [mean, median, mode, modal_class, variance, std_dev]
    })
    return stats_df

#Draw a histogram from grouped data using MatPlotLib 
def draw_histogram(grouped_df):
    plt.bar(grouped_df['Class Interval'], grouped_df['Frequency'], edgecolor='black')
    plt.xlabel('Class Interval')
    plt.ylabel('Frequency')
    plt.title('Histogram of Grouped Data')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

 
#Main Method to run each function and see the result 
 
def main(): 
    get_user_data() 
    data = read_data() 
     
    class_width = float(input("Enter class width: ")) 
    grouped_df, frequency, midpoints = group_data(data, class_width) 
    print("\nGrouped Data Table:") 
    print(grouped_df) 
    grouped_df.to_csv('grouped_data.csv', index=False) 
    print("Grouped data saved to grouped_data.csv") 
     
    stats_df = compute_statistics(data, grouped_df, frequency, midpoints) 
    print("\nStatistics Table:") 
    print(stats_df) 
    stats_df.to_csv('statistics.csv', index=False) 
    print("Statistics saved to statistics.csv") 
     
    draw_histogram(grouped_df) 
 
 
#Run Main Method 
if __name__ == "__main__": 
    main()