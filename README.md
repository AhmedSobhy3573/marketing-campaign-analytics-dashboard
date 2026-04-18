# Marketing Campaign Analytics Project

## Introduction (Problem-Driven)

Marketing data is often fragmented, inconsistent, and not immediately usable for decision-making.

This project addresses a core business challenge:  
**How can raw campaign data be transformed into a structured analytical system that enables performance evaluation and strategic decision-making?**

---

## Business Understanding

Marketing teams require:

- Clear visibility into campaign performance  
- Audience segmentation insights  
- ROI-driven decision-making  

However, raw datasets typically lack:

- Structure  
- Consistency  
- Analytical readiness  

This project bridges that gap by transforming raw data into a **business-ready analytical model**.

---

## Data Cleaning & Preparation

The dataset was systematically transformed to ensure analytical usability:

### Audience Structuring

The `Target_Audience` column was decomposed into:

- `Target_Age`  
- `Target_Gender`  

This enables:

- Granular segmentation  
- Improved filtering in dashboards  

---

### Column Reordering

Columns were reorganized to follow an analytical flow:

**Identification → Targeting → Configuration → Metrics → Financials**

This enhances:

- Readability  
- Data modeling alignment  
- BI usability  

---

## Data Dictionary

A structured data dictionary was developed to standardize the dataset.

Includes:

- Column Name  
- Data Type  
- Business Description  

---

## Column Categorization (Foundation for Data Modeling)

| Category                  | Columns                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| Campaign Identification  | Campaign_ID, Company, Campaign_Type                                    |
| Audience Targeting       | Customer_Segment, Target_Age, Target_Gender, Location, Language        |
| Campaign Configuration   | Channel_Used, Duration, Date                                           |
| Engagement Metrics       | Impressions, Clicks, Engagement_Score                                  |
| Financial Metrics        | Conversion_Rate, Acquisition_Cost, ROI                                 |

---

## Project Structure

```text
Marketing_Project/
│
├── 00_Data/
│   ├── Raw Data/ 
|           # The raw dataset is private
│   ├── Cleaned Data/ 
|       └── Cleaned_Dataset.xlsx
│   └── Data Dictionary/
|       └── Data Dictionary.xlsx
│
├── 01_Data_Modeling/
│   ├── (Coming Soon)
│
├── 02_Dashboard/
│   ├── (Coming Soon)
│
├── 03_Insights_and_Recommendation/
│   ├── (Coming Soon)
│
└── README.md
```


---

## 🚧 Project Status

### ✅ Completed

- Data Cleaning  
- Data Structuring  
- Data Dictionary  

### ⏳ Upcoming

- Star Schema Data Modeling  
- Tableau Dashboard  
- Insights & Recommendations  