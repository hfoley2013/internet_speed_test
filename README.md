# Internet Speed Test Script

This Python script runs an internet speed test using the Speedtest library and records the results in a CSV file. You can use the script to monitor your internet speed over time and check if your internet service provider (ISP) is delivering the promised speed.

## Requirements

* Python 3.6 or higher
* `speedtest-cli` library (install via pip)
* (Optional) schedule library (install via pip if you want to run the script as a cron job)

You can install the required libraries by running:

```
pip install -r requirements.txt
```

## Usage

To run the script manually, open a terminal or command prompt, navigate to the directory where the script is saved, and run:

```
python speedtest.py
```

The script will run a speed test and print the results to the console. It will also record the results in a CSV file named `speedtest_results.csv`.

If you want to run the script automatically at a certain interval (e.g., every hour), you can set up a cron job. Here's an example of how to set up a cron job to run the script every hour:

1. Open the crontab editor by running `crontab -e` in the terminal or command prompt.
2. Add the following line at the bottom of the file:

```
0 * * * * /path/to/python /path/to/speedtest.py
```

Replace `/path/to/python` with the path to your Python interpreter (e.g., /usr/bin/python3) and replace `/path/to/speedtest.py` with the path to the script file. This line tells cron to run the script every hour at the beginning of the hour (i.e., at minute 0 of every hour).

Save and exit the crontab editor.
Now the script will run automatically every hour and record the results in the CSV file.

## Notes

* The script may not work properly if your computer is in sleep mode or disconnected from the internet.
* The script may not accurately reflect your actual internet speed due to various factors such as network congestion, server load, and hardware limitations. Use the script as a reference only and consult with your ISP for more accurate measurements.
* The script is provided as is without any warranties or guarantees. Use at your own risk.

## License

This script is licensed under the MIT License.
