# Marketing Campaign Analytics Project

---

## Introduction (Problem-Driven)

Marketing data is often fragmented, inconsistent, and not immediately usable for decision-making.

This project addresses a core business challenge:

> **How can raw campaign data be transformed into a structured analytical system that enables performance evaluation and strategic decision-making?**

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

✔ This project transforms raw data into a **business-ready analytical model**.

---

## Data Cleaning & Preparation

The dataset was systematically transformed to ensure analytical usability.

### 🔹 Audience Structuring

The `Target_Audience` column was decomposed into:

- `Target_Age`  
- `Target_Gender`  

**Impact:**

- Enables granular segmentation  
- Improves dashboard filtering  

---

### 🔹 Column Reordering

Columns were reorganized into a logical analytical flow:

> **Identification → Targeting → Configuration → Metrics → Financials**

**Impact:**

- Improves readability  
- Aligns with data modeling practices  
- Enhances BI usability  

---

## Data Dictionary

A structured data dictionary was developed to standardize the dataset.

Includes:

- Column Name  
- Data Type  
- Business Description  

---

## Column Categorization (Modeling Foundation)

| Category                  | Columns                                                                 |
|--------------------------|-------------------------------------------------------------------------|
| Campaign Identification  | Campaign_ID, Company, Campaign_Type                                    |
| Audience Targeting       | Customer_Segment, Target_Age, Target_Gender, Location, Language        |
| Campaign Configuration   | Channel_Used, Duration, Date                                           |
| Engagement Metrics       | Impressions, Clicks, Engagement_Score                                  |
| Financial Metrics        | Conversion_Rate, Acquisition_Cost, ROI                                 |

---

## Data Modeling – Star Schema

To enable scalable and efficient analytics, a **Star Schema** was designed.

---

![](01_Data_Modeling/Entity_Relationship_Diagram/ERD.png)

### Fact Table

#### `Fact_Campaign_Performance`

Central table capturing measurable business events:

- Impressions  
- Clicks  
- Engagement_Score  
- Conversion_Rate  
- Acquisition_Cost  
- ROI  

---

### Dimension Tables

Descriptive tables providing analytical context:

- `Dim_Campaign` → Campaign details  
- `Dim_Audience` → Audience segmentation  
- `Dim_Channel` → Marketing channels  
- `Dim_Date` → Time-based analysis  

---

### Relationships

- One-to-many relationships from dimensions → fact table  
- Surrogate keys implemented for:
  - Data consistency  
  - Faster joins  
  - Scalability  

---

### Why Star Schema?

- Optimized query performance  
- Simplified dashboard development  
- Scalable for large datasets  
- Industry-standard BI architecture  

---

## Python Implementation

Using **Pandas**, the data model was programmatically built:

- Generated dimension tables  
- Constructed fact table with calculated metrics  
- Maintained relational integrity  
- Exported all tables into a single Excel file  

---

## Best Practices Applied

- ID columns positioned on the **left**  
- Consistent naming conventions  
- Clear separation of facts vs dimensions  
- Analytical-friendly structure  

---

## Project Structure

```text
Marketing_Project/
│
├── 00_Data/
│   ├── Raw Data/ 
│   │   └── (Private)
│   ├── Cleaned Data/
│   │   └── Cleaned_Dataset.xlsx
│   └── Data Dictionary/
│       └── Data Dictionary.xlsx
│
├── 01_Data_Modeling/
│   ├── Entity_Relationship_Diagram/
│   │   └── ERD.png
│   ├── Final_Dataset/
│   │   └── Marketing_Dataset.xlsx
│   └── Building_a_Star_Schema.py
│
├── 02_Dashboard/
│   └── (Coming Soon)
│
├── 03_Insights_and_Recommendation/
│   └── (Coming Soon)
│
└── README.md
```

--- 

## Project Status 

### ✅ Completed 

- Data Cleaning 
- Data Structuring 
- Data Dictionary 
- Star Schema Data Modeling 

### ⏳ Upcoming 

- Tableau Dashboard 
- Insights & Recommendations
