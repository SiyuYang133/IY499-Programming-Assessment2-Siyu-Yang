import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
from groupData import group_data, draw_histogram

def get_user_data():
    print("Enter numerical values separated by commas (e.g., 23, 45, 67):")
    user_input = input(">> ")
    try:
        data = list(map(float, user_input.split(',')))
        df = pd.DataFrame({'Values': data})
        df.to_csv("sampleData-1.csv", index=False)
        print("Data saved to sampleData-1.csv")
    except ValueError:
        print("Invalid input. Please enter numeric values only.")

def read_data():
    try:
        df = pd.read_csv("sampleData-1.csv")
        print("\n**** Data from CSV file ****\n")
        print(df)
        print("\nSummary Statistics:\n")
        print(df.describe())
        return df['Values'].tolist()
    except FileNotFoundError:
        print("CSV file not found. Please enter and save data first.")
        return []

def compute_statistics(data, grouped_df, frequency, midpoints):
    try:
        modal_class_index = frequency.index(max(frequency))
        modal_class = grouped_df.iloc[modal_class_index]['Classes']
    except:
        modal_class = "N/A"

    stats = {
        'Mean': statistics.mean(data),
        'Median': statistics.median(data),
        'Mode': statistics.mode(data),
        'Modal Class': modal_class,
        'Variance': statistics.variance(data),
        'Standard Deviation': statistics.stdev(data)
    }

    stats_df = pd.DataFrame(list(stats.items()), columns=["Statistic", "Value"])
    return stats_df

def main():
    menu = """***** Grouped Data Application *****
Menu
1- Enter Data and Save in CSV
2- Show Statistics
3- Draw Histogram
4- Exit
Enter your Choice (1..4): """

    while True:
        choice = input(menu).strip()
        
        if choice == '1':
            print("\nEnter data and Save in CSV file.\n")
            get_user_data()
        
        elif choice == '2':
            print("\n --- Show the Statistics here---\n")
            data = read_data()
            if not data:
                continue
            try:
                class_width = float(input("Enter class width: "))
                grouped_df, frequency, midpoints = group_data(data, class_width)
                print("\nGrouped Data Table:\n", grouped_df)
                grouped_df.to_csv("grouped_data.csv", index=False)
                print("Grouped data saved to grouped_data.csv")

                stats_df = compute_statistics(data, grouped_df, list(frequency), midpoints)
                print("\nStatistics Table:\n", stats_df)
                stats_df.to_csv("statistics.csv", index=False)
                print("Statistics saved to statistics.csv")
            except Exception as e:
                print("Error during statistical analysis:", e)

        elif choice == '3':
            print("\n --- Draw Histogram here---\n")
            data = read_data()
            if not data:
                continue
            try:
                class_width = float(input("Enter class width: "))
                grouped_df, _, _ = group_data(data, class_width)
                draw_histogram(grouped_df, class_width)
            except Exception as e:
                print("Error drawing histogram:", e)

        elif choice == '4':
            print("\nExiting .....\n")
            break
        else:
            print("\nInvalid input, Try again.\n")

if __name__ == "__main__":
    main()
