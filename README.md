# 🌃 UK Nighttime Economy Analytics Dashboard

[![Streamlit](https://img.shields.io/badge/Streamlit-1.54.0-red)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.3.3-blue)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-6.5.0-orange)](https://plotly.com/)

## 📊 About This Project

A comprehensive data analytics dashboard that explores and analyses the UK nighttime economy from 2012-2022. This interactive web application provides valuable insights into nighttime workforce demographics, business clustering patterns, and economic trends across different regions of the United Kingdom.

### 🌐 Live Demo
**Try the dashboard yourself**: [https://yingning-uk-nighttime-economy.streamlit.app/](https://yingning-uk-nighttime-economy.streamlit.app/)

### 🎯 What It Does

- **Multi-dimensional Data Visualisation**: Interactive maps, time-series analysis, and comparative charts
- **Geospatial Analysis**: Regional workforce distribution with dynamic filtering
- **Temporal Trend Analysis**: Year-on-year changes and growth patterns
- **Business Intelligence**: London nighttime business cluster mapping and operating hours analysis
- **Responsive Design**: Built with Streamlit for optimal user experience across devices

## 🚀 How It's Built

### Technical Architecture
- **Frontend**: Streamlit web framework with multi-page navigation
- **Data Processing**: Pandas for data manipulation and analysis
- **Visualisation**: Plotly for interactive charts and maps
- **Geospatial Mapping**: MapBox integration for regional analysis

### Data Sources
- **UK Office for National Statistics (ONS)**: Labour Force Survey data on nighttime workforce
- **Yelp Fusion API**: London business location and operating hours data
- **Regional Geographic Data**: Latitude/longitude coordinates for UK regions

### Core Analytics Modules

#### 1. **Nighttime Workforce Analysis** (`night_workforce.py`)
- Regional workforce distribution across UK regions (2012-2022)
- Industry-specific breakdowns (Culture & Leisure, Health Services, Support Activities)
- Growth rate analysis and trend identification
- Top-performing regions by absolute and percentage growth

#### 2. **Business Cluster Intelligence** (`night_business.py`)
- London nighttime business mapping with real-time filtering
- Category-based analysis (Restaurants, Pubs, Music Venues, Dance Clubs, etc.)
- Operating hours trend analysis (2019-2023)
- Geographic cluster identification (Soho, Central London, East London, Canary Wharf)

## 🛠️ Technical Skills Demonstrated

### Data Engineering
- **ETL Pipeline Development**: CSV data ingestion, cleaning, and transformation
- **Data Integration**: Multiple data source consolidation (ONS, Yelp APIs)
- **Geospatial Data Processing**: Coordinate mapping and regional aggregation
- **Time Series Analysis**: Temporal trend identification and forecasting

### Data Visualisation
- **Interactive Dashboard Design**: Multi-page Streamlit application
- **Advanced Charting**: Scatter plots, line charts, bar charts, and geographic maps
- **Custom Styling**: Theme consistency and professional UI/UX design
- **Responsive Layouts**: Adaptive design for various screen sizes

### Statistical Analysis
- **Descriptive Statistics**: Regional workforce distribution analysis
- **Growth Rate Calculations**: Year-on-year percentage changes
- **Comparative Analysis**: Cross-regional and cross-industry comparisons
- **Trend Identification**: Pandemic impact assessment and recovery patterns

### Programming & Development
- **Python Programming**: Object-oriented design and modular architecture
- **API Integration**: External data source consumption
- **Version Control**: Git-based development workflow
- **Dependency Management**: Requirements.txt for reproducible environments

## 📈 Key Insights Generated

### Workforce Trends
- Identified **24-hour health services** as the largest nighttime employer segment
- Discovered **COVID-19 impact** with 2021 showing negative growth across most sectors
- Revealed **regional disparities** with London boroughs showing highest absolute growth

### Business Patterns
- Mapped **nighttime business clusters** in London with geographic concentration analysis
- Analysed **operating hours evolution** pre/post pandemic (2019-2023)
- Identified **emerging nightlife hotspots** in East London

## 🏗️ Getting Started

### What You'll Need
- Python 3.12+
- pip package manager

### Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/uk-nighttime-economy.git
cd uk-nighttime-economy

# Install dependencies
pip install -r requirements.txt

# Launch the application
streamlit run app.py
```

Navigate to `http://localhost:8501/` to access the dashboard.

### Dependencies
```
numpy==2.4.2
pandas==2.3.3
plotly==6.5.0
streamlit==1.54.0
```

## 🎯 Real-World Applications

This project demonstrates comprehensive data analytics capabilities applicable to:

- **Economic Policy Analysis**: Regional economic development insights
- **Urban Planning**: Nighttime economy infrastructure planning
- **Business Intelligence**: Market analysis and location optimisation
- **Labour Market Research**: Employment trend analysis and forecasting
- **Public Policy**: Service planning and resource allocation

## 🔬 How It Works

### Data Processing Pipeline
1. **Data Collection**: ONS labour survey data and Yelp API integration
2. **Data Cleaning**: Missing value handling and data type standardisation
3. **Feature Engineering**: Growth rates, ratios, and regional aggregations
4. **Visualisation**: Interactive dashboard development with user-driven filtering

### Analytical Techniques
- **Time Series Analysis**: Trend identification and seasonal pattern detection
- **Geospatial Analysis**: Regional clustering and hot spot identification
- **Comparative Analysis**: Cross-regional and cross-industry benchmarking
- **Statistical Summarisation**: Descriptive statistics and key performance indicators

## 📊 Sample Visualisations

- **Interactive UK Map**: Regional nighttime workforce distribution with dynamic filtering
- **Time Series Charts**: Multi-year trend analysis with industry breakdowns
- **Comparative Bar Charts**: Top-performing regions by growth metrics
- **London Business Map**: Real-time business cluster visualisation
