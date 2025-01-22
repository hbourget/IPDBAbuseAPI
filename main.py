import os
import requests
import csv
from datetime import datetime
from prettytable import PrettyTable
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("IPDBABUSE_API_KEY")
API_URL = "https://api.abuseipdb.com/api/v2/check"

with open('ips_to_check.txt', 'r') as file:
    ip_list = []
    for line in file:
        stripped_line = line.strip()
        if stripped_line:
            ip_list.append(stripped_line)

def check_ip(ip):
    headers = {
        'Accept': 'application/json',
        'Key': API_KEY
    }
    params = {
        'ipAddress': ip,
        'maxAgeInDays': 40
    }

    response = requests.get(API_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            'ip': ip,
            'is_reported': data['data']['totalReports'] > 0,
            'report_count': data['data']['totalReports'],
            'abuse_confidence_score': data['data']['abuseConfidenceScore']
        }
    else:
        return {
            'ip': ip,
            'error': response.text
        }

def save_to_csv(results, filename="results.csv"):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "IP Address", "Reported?", "Report Count", "Abuse Confidence Score"])
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for result in results:
            writer.writerow([
                timestamp,
                result['ip'],
                "Yes" if result.get('is_reported', False) else "No",
                result.get('report_count', "N/A"),
                result.get('abuse_confidence_score', "N/A")
            ])

def display_pretty_table(results):
    table = PrettyTable()
    table.field_names = ["IP Address", "Reported?", "Report Count", "Abuse Confidence Score"]

    for result in results:
        table.add_row([
            result['ip'],
            "Yes" if result.get('is_reported', False) else "No",
            result.get('report_count', "N/A"),
            result.get('abuse_confidence_score', "N/A")
        ])
    print(table)

def main():
    results = []
    for ip in ip_list:
        result = check_ip(ip)
        results.append(result)

    display_pretty_table(results)
    save_to_csv(results)

if __name__ == "__main__":
    main()
