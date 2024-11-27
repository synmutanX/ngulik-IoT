import matplotlib.pyplot as plt
import pandas as pd
import time

# File to monitor
CSV_FILE = 'od_data.csv'

# Real-time plotting function
def real_time_plot():
    plt.ion() # Interactive mode for real-time plotting
    """
    Real-time plotting function that continuously reads data from a CSV file and
    updates a line plot accordingly. The CSV file is expected to have two columns,
    'timestamp' and 'od_value', with the timestamp being a Unix epoch time and
    the OD value being a numerical value. The data is plotted on a line graph
    with a pause of 2 seconds between each update.

    Args:
        None

    Returns:
        None
    """
    fig, ax = plt.subplots()

    while True:
        try:
            # load data from CSV file
            data = pd.read_csv(CSV_FILE, header=None, names=['timestamp', 'od_value'])
            timestamps = data['timestamp']
            od_values = data['od_value']

            # Clear and re-plot data
            ax.clear()
            ax.plot(timestamps, od_values, label="Optical Density (OD)", color='b')
            ax.set_xlabel('Time (epoch)')
            ax.set_ylabel('Optical Density')
            ax.set_title('Real-Time OD Visualization')
            ax.legend()
            plt.pause(2) # Pause for 2 seconds before the next update
        except FileNotFoundError:
            print("CSV file not found. Waiting for data...")
            time.sleep(2)
        except Exception as e:
            print(f"Error reading or plotting data: {e}")
            time.sleep(2)

if __name__ == '__main__':
    real_time_plot()