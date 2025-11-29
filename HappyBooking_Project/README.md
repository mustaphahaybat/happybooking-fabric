# 🏨 HappyBooking - Modern Data Engineering Project

## 📋 Proje Özeti
Microsoft Fabric kullanarak hotel booking verisini işleyen modern data engineering projesi.

### 🎯 Kullanılan Teknolojiler
- Microsoft Fabric (Lakehouse, Warehouse, Eventstream)
- PySpark (Veri işleme)
- Docker (Stream simülatörü)
- DBT (Gold layer transformations)
- Great Expectations (Data quality)
- Power BI (Dashboard)
- GitHub Actions (CI/CD)

### 📊 Veri
- Batch: 1.05M satır
- Streaming: 450K satır
- API: Weather + Currency enrichment

### 🏗️ Mimari
Bronze Layer → Silver Layer → Gold Layer → Power BI

### 📁 Proje Yapısı
```
HappyBooking_Project/
├── data/
├── notebooks/
├── docker/
├── dbt_project/
├── tests/
└── docs/
```

---
**Kasım 2024 - Data Engineering Final Project**