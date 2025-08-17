import re
from collections import Counter

#Regex for common Apache/Nginx log format
log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)\s'      #IP Address
    r'.*?"(?P<method>GET|POST|PUT|DELETE|HEAD)\s(?P<url>\S+)\s'  #Request Method + URL
    r'.*?"\s(?P<status>\d{3})'           #Response Code
)

def analyze_log(file_path):
    ip_counter = Counter()
    url_counter = Counter()
    status_counter = Counter()

    with open(file_path, 'r', encoding="utf-8", errors="ignore") as f:
        for line in f:
            match = log_pattern.search(line)
            if match:
                ip = match.group("ip")
                url = match.group("url")
                status = match.group("status")

                ip_counter[ip] += 1
                url_counter[url] += 1
                status_counter[status] += 1

    #Show top 5 results
    print("\n--- Top 5 IP Addresses ---")
    for ip, count in ip_counter.most_common(5):
        print(f"{ip} -> {count} requests")

    print("\n--- Top 5 URLs Accessed ---")
    for url, count in url_counter.most_common(5):
        print(f"{url} -> {count} hits")

    print("\n--- Response Codes ---")
    for status, count in status_counter.most_common():
        print(f"{status} -> {count} times")


#Example usage
if __name__ == "__main__":
    log_file = "access.log"  #Replace with your log file path
    analyze_log(log_file)
