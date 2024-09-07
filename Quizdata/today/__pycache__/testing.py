import speedtest
from tqdm import tqdm

def test_speed():
    print("Running network speed test...")

    st = speedtest.Speedtest()

    # Get the best server
    st.get_best_server()

    # Measure download speed
    print("Testing download speed...")
    download_speed = st.download()
    tqdm(range(100), desc="Download Speed Test Progress")

    # Measure upload speed
    print("Testing upload speed...")
    upload_speed = st.upload()
    tqdm(range(100), desc="Upload Speed Test Progress")

    # Get ping
    ping_result = st.results.ping

    # Display results
    print(f"Download Speed: {download_speed / 1_000_000:.2f} Mbps")
    print(f"Upload Speed: {upload_speed / 1_000_000:.2f} Mbps")
    print(f"Ping: {ping_result:.2f} ms")

import schedule
import time

def run_scheduled_tests():
    print("Network Optimization Tool is Running... Press Ctrl+C to stop.")
    schedule.every(10).minutes.do(test_speed)  # Change to desired interval

    while True:
        schedule.run_pending()
        # time.sleep(1)

run_scheduled_tests()
import logging
import csv
from datetime import datetime

# Setup logging
logging.basicConfig(filename='network_optimization.log', level=logging.INFO)

def log_results(download_speed, upload_speed, ping_result):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f"{timestamp} | Download: {download_speed:.2f} Mbps | Upload: {upload_speed:.2f} Mbps | Ping: {ping_result:.2f} ms"

    # Log to file
    logging.info(log_message)

    # Save to CSV
    with open('network_performance.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timestamp, download_speed, upload_speed, ping_result])

    print("Results logged successfully.")

# Call log_results inside test_speed after calculations
def optimize_network():
    # Placeholder function
    print("Analyzing network performance for optimizations...")

    # Example optimization logic
    # - Analyze trends
    # - Recommend server changes
    # - Suggest load balancing
    # For now, it's just a placeholder.
    print("Network optimization analysis complete. Suggestions will be available soon.")