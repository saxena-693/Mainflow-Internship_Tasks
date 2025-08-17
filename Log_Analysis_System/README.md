# Log Analysis System :-

##  Objective:-
The **Log Analysis System** parses large Apache/Nginx log files and extracts useful insights such as:
- Most frequent **IP addresses**
- Most requested **URLs**
- Distribution of **response codes**

This helps in monitoring traffic, detecting suspicious activity, and analyzing server performance.


##  Features:-
- Parses **Apache/Nginx access logs** using regex.
- Supports **IPv4 and IPv6** addresses.
- Counts request frequency with Python's `Counter`.
- Displays **Top 5 IPs**, **Top 5 URLs**, and **all response codes**.
- Handles log files up to **100 MB** (as per project restriction).
- Works even if log file contains invalid/garbled lines.


## Technologies Used:-
- **Python 3**
- `re` → Regular expressions for log parsing  
- `collections.Counter` → Frequency analysis
