# 🏨 HappyBooking - Modern Data Engineering Project

![CI/CD](https://github.com/KULLANICI_ADINIZ/happybooking-fabric/workflows/CI%20-%20Tests%20and%20Quality%20Checks/badge.svg)
![Deployment](https://github.com/KULLANICI_ADINIZ/happybooking-fabric/workflows/CD%20-%20Deploy%20to%20Production/badge.svg)

## 📋 Project Overview

Modern data engineering project using Microsoft Fabric, implementing medallion architecture (Bronze → Silver → Gold) for hotel booking data analytics.

### 🎯 Key Features

- **Bronze Layer:** Raw data ingestion from batch, streaming, and APIs
- **Silver Layer:** Data cleaning and transformation with PySpark
- **Gold Layer:** Business logic and KPIs with DBT
- **Streaming:** Real-time data simulation with Docker
- **Automation:** Fabric Pipeline for daily orchestration
- **CI/CD:** GitHub Actions for testing and deployment
- **Visualization:** Interactive Power BI dashboard

---

## 🏗️ Architecture
```
┌─────────────────────────────────────────────┐
│  DATA SOURCES                               │
│  ├─ Kaggle CSV (1.05M records)             │
│  ├─ Docker Stream (450K events)            │
│  └─ APIs (Weather + Currency)              │
└────────────────┬────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────┐
│  BRONZE LAYER (Raw Data)                    │
│  ├─ bronze_hotel_bookings                   │
│  ├─ bronze_hotel_bookings_stream            │
│  ├─ bronze_weather_data                     │
│  └─ bronze_currency_rates                   │
└────────────────┬────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────┐
│  SILVER LAYER (Cleaned Data)                │
│  ├─ silver_hotel_bookings (~1M records)     │
│  ├─ silver_weather_data                     │
│  └─ silver_currency_rates                   │
└────────────────┬────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────┐
│  GOLD LAYER (Business Models)               │
│  ├─ gold_fact_booking (839K records)        │
│  ├─ gold_dim_hotel (2.9K hotels)           │
│  ├─ gold_dim_customer (10K customers)      │
│  ├─ gold_dim_city (727 cities)             │
│  ├─ gold_dim_date (1.1K dates)             │
│  └─ gold_kpi_revenue (330K KPIs)           │
└────────────────┬────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────┐
│  POWER BI DASHBOARD                         │
│  ├─ Overview Analytics                      │
│  ├─ Hotel Performance                       │
│  ├─ Customer Insights                       │
│  └─ KPI Dashboard                           │
└─────────────────────────────────────────────┘
```

---

## 🛠️ Technologies Used

| Category | Technology |
|----------|-----------|
| **Platform** | Microsoft Fabric |
| **Storage** | OneLake (Delta Lake) |
| **Processing** | PySpark |
| **Streaming** | Docker, Fabric Eventstream |
| **Transformation** | DBT (Data Build Tool) |
| **Orchestration** | Fabric Data Pipeline |
| **Visualization** | Power BI |
| **Version Control** | Git, GitHub |
| **CI/CD** | GitHub Actions |
| **Testing** | Pytest, Great Expectations |

---

## 📊 Data Statistics

| Layer | Tables | Records |
|-------|--------|---------|
| **Bronze** | 4 | 1,813,575 |
| **Silver** | 3 | ~1,000,000 |
| **Gold** | 6 | 1,183,697 |

---

## 🚀 Getting Started

### Prerequisites

- Microsoft Fabric workspace (60-day trial available)
- Python 3.10+
- Docker Desktop
- Git

### Installation
```bash
# Clone repository
git clone https://github.com/KULLANICI_ADINIZ/happybooking-fabric.git
cd happybooking-fabric

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v
```

---

## 📁 Project Structure
```
happybooking-fabric/
├── .github/workflows/     # CI/CD pipelines
│   ├── ci.yml            # Tests on PR
│   └── cd.yml            # Deploy on merge
├── data/                  # Data files (gitignored)
├── docker/                # Stream producer
│   ├── Dockerfile
│   └── stream_producer.py
├── notebooks/             # Fabric notebooks
│   ├── 01_bronze_ingest_batch.py
│   ├── 04_api_data_to_bronze.py
│   ├── 05_silver_transformations.py
│   └── 06_Gold_Layer_DBT_Models.py
├── tests/                 # Quality tests
│   └── test_data_quality.py
├── requirements.txt       # Python dependencies
├── .gitignore
└── README.md
```

---

## 🔄 CI/CD Pipeline

### Pull Request (CI)
- ✅ Run Pytest
- ✅ Code quality checks (flake8)
- ✅ Data quality validation

### Merge to Main (CD)
- ✅ Validate project structure
- ✅ Create deployment summary
- ✅ Production deployment

---

## 📈 Key Metrics

- **Total Data Processed:** 1.8M+ records
- **Data Quality:** 95%+ valid records
- **Pipeline Execution:** ~20-30 minutes
- **Automation:** Daily scheduled runs

---

## 👨‍💻 Author

**[Your Name]**
- GitHub: mustaphahaybat(https://github.com/mustaphahaybat)
- Project: Data Engineering Final Project
- Date: November 2024

---

## 📄 License

This project is for educational purposes.

---

## 🙏 Acknowledgments

- Kaggle for the hotel booking dataset
- Microsoft Fabric team
- Open-Meteo API (weather data)
- ExchangeRate-API (currency data)
