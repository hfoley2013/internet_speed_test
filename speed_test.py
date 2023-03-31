import csv
import speedtest
import time

def run_speed_test():
    st = speedtest.Speedtest()
    download_speed = round(st.download() / (1024*1024), 2)  # convert bytes to megabytes
    upload_speed = round(st.upload() / (1024*1024), 2)
    ping = round(st.results.ping, 2)
    print(f"Download speed: {download_speed} Mbps")
    print(f"Upload speed: {upload_speed} Mbps")
    print(f"Ping: {ping} ms")
    with open('speedtest_results.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), download_speed, upload_speed, ping])

run_speed_test()
