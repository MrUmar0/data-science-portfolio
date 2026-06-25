Sales Dashboard

A data analysis project that analyzes 5000 rows of sales data using Pandas to uncover revenue trends, top products, and best performing cities.

What it does


Loads and explores real-world style sales data (5000 rows)
Calculates Revenue for each order (Quantity × Price)
Analyzes monthly revenue trends (Jan–Dec 2024)
Finds top performing products by revenue
Ranks cities by total revenue
Prints a clean summary dashboard


Results (sample output)

Total Revenue:   2,367,405,000
Total Orders:    5,000
Best Month:      October
Best Product:    Laptop
Best City:       Karachi

How to run


Install dependency:


   pip install pandas


Make sure sales_data.csv is in the same folder
Run:


   python sales_dashboard.py

Concepts used

ConceptCodeLoad CSVpd.read_csv()Date conversionpd.to_datetime()Extract monthdf["Date"].dt.monthRevenue calculationQuantity × PriceGroup by analysisdf.groupby().sum()Best performer.idxmax()Count occurrences.value_counts()

Dataset

ColumnDescriptionDateOrder date (2024)ProductLaptop, Phone, Tablet, Monitor, HeadphonesCityLahore, Karachi, Islamabad, Peshawar, Quetta, MultanQuantityUnits sold per orderPricePrice per unitRevenueCalculated — Quantity × Price

Folder structure

pandas-numpy/
└── sales-dashboard/
    ├── sales_dashboard.py
    ├── sales_data.csv
    └── README.md