# Log Analyzer CLI

A command-line tool to analyze web server logs and extract useful insights such as traffic patterns, endpoint usage, and error statistics.

---

## 🚀 Features

* 📊 Top IP addresses (most active clients)
* 🔗 Most accessed endpoints
* ⚠️ HTTP status code distribution
* 🚨 Error categorization (4xx vs 5xx)
* 📈 Percentage-based analysis
* 🎯 Configurable output (top N results)
* 🔍 Optional error-only view

---

## 📂 Example Log Format

```log
127.0.0.1 - - [12/Feb/2024:10:00] "GET /index.html HTTP/1.1" 200
192.168.1.1 - - [12/Feb/2024:10:01] "POST /login HTTP/1.1" 401
127.0.0.1 - - [12/Feb/2024:10:02] "GET /about HTTP/1.1" 200
10.0.0.1 - - [12/Feb/2024:10:03] "GET /index.html HTTP/1.1" 500
```

---

## 🛠 Usage

Basic usage:

```bash
python main.py sample.log
```

---

### 🔧 Options

Show top N results:

```bash
python main.py sample.log --top 3
```

Show only error statistics:

```bash
python main.py sample.log --errors
```

---

## 📊 Example Output

```
Total Requests: 4

Top IPs:
127.0.0.1 → 2 (50.00%)

Top Endpoints:
/index.html → 2 (50.00%)

Status Codes:
200 → 2 (50.00%)
401 → 1 (25.00%)
500 → 1 (25.00%)

Error Summary:
4xx Errors → 1
5xx Errors → 1
```

---

## 🧠 Concepts Covered

* Regular Expressions (log parsing)
* File processing
* Data aggregation using `collections.Counter`
* CLI development using `argparse`
* Basic analytics and reporting

---

## ⚡ How It Works

1. Parses each log line using regex
2. Extracts IP, endpoint, and status code
3. Aggregates data using counters
4. Computes percentages and error categories
5. Displays results in a readable format

---

## 📁 Project Structure

```
003-log-analyzer
│
├── main.py
├── sample.log
├── README.md
└── requirements.txt
```

---

## 📌 Notes

* Works with standard web server logs (Apache/Nginx style)
* Ignores malformed log lines
* Designed for learning and extensibility

---

## 🔮 Possible Improvements

* Export results to JSON/CSV
* Time-based analysis (requests per minute/hour)
* Visualization (charts/graphs)
* Support for large log streaming
