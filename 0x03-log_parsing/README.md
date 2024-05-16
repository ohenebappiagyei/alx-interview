# Log Parsing

Welcome to the Log Parsing project! This project focuses on parsing and processing data streams in real-time using Python. The primary goal is to read logs from standard input (stdin), process the data, and compute various metrics.

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Example](#example)
- [Files](#files)
- [Author](#author)

## Description

In this project, you will create a Python script that reads log entries from standard input, processes the data, and computes key metrics. The log entries follow a specific format and your script will:
- Calculate the total file size from all entries.
- Count the number of lines for specific HTTP status codes.

Your script will print the computed statistics after every 10 lines of input and upon receiving a keyboard interruption (CTRL + C).

## Usage

To run the project, you need to have Python installed on your system. Follow these steps to execute the scripts:

1. Make sure the scripts are executable:
    ```sh
    chmod +x 0-generator.py 0-stats.py
    ```

2. Run the log generator and the statistics script together:
    ```sh
    ./0-generator.py | ./0-stats.py
    ```

## Example

Here is an example of how the output might look:

File size: 12345
200: 15
301: 3
404: 5
File size: 23456
200: 30
301: 5
400: 2
404: 10


## Files

- `0-generator.py`: This script generates random log entries and writes them to standard output.
- `0-stats.py`: This script reads log entries from standard input, processes them, and prints the required statistics.

## Author

This project was developed by Dr. Prince Alex Appiagyei, inspired by the teaching style of ALXSWE

