# Agricultural Yield Prediction & Data Platform

### Project Overview
This project implements a data transformation pipeline that pulls disparate source formats—specifically crop yield records and historical weather data—into a single, normalized analytical schema. This allows for deep diagnostic analysis of how environmental factors affect agricultural productivity.

### Technologies Used
* **Python**: Advanced data manipulation and feature engineering.
* **Pandas & NumPy**: Used for multi-source joins and metric calculations.
* **BigQuery Logic**: Designed for cloud-native analytical schemas.

### Pipeline Features
1. **Multi-Source Ingestion**: Merged crop records with regional weather time-series.
2. **Feature Engineering**: Calculated 'Yield Efficiency' metrics to identify regional performance trends.
3. **Business Intelligence**: Generated summary reports showing average efficiency by region to support stakeholder reporting.
