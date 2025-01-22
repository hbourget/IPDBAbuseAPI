# IPDBAbuse Checker

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.7%2B-purple.svg)

## Overview

This python tool allows you to verify a list of IP addresses against the AbuseIPDB API. It checks each IP for reported abuse incidents, provides a detailed report, and saves the results in both a CSV file and a formatted table in the console.

## Prerequisites

- Python 3.7 or higher
- A IPDBAbuse API API key (register on [abuseipdb.com](https://www.abuseipdb.com/))

## Installation

1. **Clone the Repository**

   ```bash
   https://github.com/hbourget/IPDBAbuseAPI.git
   cd IPDBAbuseAPI
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Obtain an AbuseIPDB API Key**

   - Sign up at [AbuseIPDB](https://www.abuseipdb.com/) to get your API key.

2. **Set Up Environment Variables**

   - Create a `.env` file in the project root directory:

     ```bash
     touch .env
     ```

   - Add your API key to the `.env` file:

     ```env
     IPDBABUSE_API_KEY=your_abuseipdb_api_key_here
     ```

   > **Note:** Ensure that `.env` is listed in your `.gitignore` to prevent exposing your API key.

## Usage

1. **Prepare the IPs to check**

   - Create a file named `ips_to_check.txt` in the project root directory.
   - List the IP addresses you want to check, one per line. For example:

     ```txt
     192.168.1.1
     8.8.8.8
     1.1.1.1
     ```

2. **Run the Script**

   ```bash
   python main.py
   ```

3. **View the Results**

   - The script will display a formatted table in the console.
   - Results will also be saved to `results.csv` in the project directory.

## Output

 **CSV File:**

   - **File name:** `results.csv`
   - **Columns:**
     - Timestamp
     - IP Address
     - Reported?
     - Report Count
     - Abuse Confidence Score

   Example:

   ```csv
   Timestamp,IP Address,Reported?,Report Count,Abuse Confidence Score
   2025-01-22 14:30:00,192.168.1.1,No,0, 0
   2025-01-22 14:30:01,8.8.8.8,Yes,5,75
   2025-01-22 14:30:02,1.1.1.1,No,0,0
   ```

## License

This project is licensed under the [MIT License](LICENSE).
