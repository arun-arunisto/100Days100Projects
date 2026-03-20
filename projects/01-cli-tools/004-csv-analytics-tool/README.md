# CSV Analytics CLI

A command-line tool to analyze CSV files and generate basic statistical insights for each column.

---

## 🚀 Features

* 📂 Reads and parses CSV files
* 🧾 Displays column names
* 🔢 Numeric column analysis:
  * Mean
  * Minimum
  * Maximum
* 🔤 Non-numeric column analysis:
  * Unique value count
* ⚡ Simple and fast CLI-based analysis

---

## 📂 Example CSV

```csv
name,age,salary
Alice,25,50000
Bob,30,60000
Charlie,35,70000
Alice,25,50000
```

---

## 🛠 Usage

Basic usage:

```bash
python main.py sample.csv
```

---

## 📊 Example Output

```id=
Columns:
- name
- age
- salary

Analysis:

Column: name
  Count: 4
  Unique Values: 3
------------------------------

Column: age
  Count: 4
  Mean: 28.75
  Min: 25.0
  Max: 35.0
------------------------------

Column: salary
  Count: 4
  Mean: 57500.00
  Min: 50000.0
  Max: 70000.0
------------------------------
```

---

## 🧠 Concepts Covered

* CSV file parsing (`csv` module)
* Data type detection (numeric vs non-numeric)
* Basic statistical calculations
* CLI development using `argparse`
* Data aggregation and analysis

---

## ⚙️ How It Works

1. Reads CSV using `DictReader`
2. Extracts column names
3. Iterates through each column:
   * Detects numeric values
   * Computes statistics
4. Prints formatted output

---

## 📁 Project Structure

```id=
004-csv-analytics
│
├── main.py
├── sample.csv
├── README.md
└── requirements.txt
```

---

## 📌 Notes

* Assumes well-formed CSV files with headers
* Ignores non-numeric values in numeric calculations
* Designed for small to medium datasets

---

## 🔮 Possible Improvements

* Stream large CSV files (memory optimization)
* Export results to JSON/CSV
* Column filtering options
* Data visualization (charts)
* Integration with Pandas for advanced analytics
