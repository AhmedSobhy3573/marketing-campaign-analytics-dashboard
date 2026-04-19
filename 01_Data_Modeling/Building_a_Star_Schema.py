import pandas as pd

df = pd.read_excel('../00_Data/Cleaned Data/Cleaned_Dataset.xlsx', sheet_name="Marketing_Dataset")

# -----------------------------
# Transformations
# -----------------------------

# Duration → numeric
df["Duration_Days"] = df["Duration"].str.extract(r'(\d+)').astype(int)

# -----------------------------
# Audience Dimension
# -----------------------------
dim_audience = df[[
    "Customer_Segment","Target_Age","Target_Gender","Location","Language"
]].drop_duplicates().reset_index(drop=True)

dim_audience.insert(0, "Audience_ID", dim_audience.index + 1)

# Merge
df = df.merge(dim_audience, on=[
    "Customer_Segment","Target_Age","Target_Gender","Location","Language"
])

# -----------------------------
# Channel Dimension
# -----------------------------
dim_channel = df[["Channel_Used"]].drop_duplicates().reset_index(drop=True)
dim_channel.insert(0, "Channel_ID", dim_channel.index + 1)

df = df.merge(dim_channel, on="Channel_Used")

# -----------------------------
# Campaign Dimension
# -----------------------------
dim_campaign = df[["Campaign_ID","Company","Campaign_Type"]].drop_duplicates()

# Ensure Campaign_ID is first (already is, but safe)
cols = ["Campaign_ID","Company","Campaign_Type"]
dim_campaign = dim_campaign[cols]

# -----------------------------
# Date Dimension
# -----------------------------
dim_date = pd.DataFrame({
    "Date": pd.to_datetime(df["Date"].unique())
})

dim_date.insert(0, "Date_ID", dim_date["Date"])

dim_date["Day"] = dim_date["Date"].dt.day
dim_date["Month"] = dim_date["Date"].dt.month
dim_date["Year"] = dim_date["Date"].dt.year
dim_date["Quarter"] = dim_date["Date"].dt.quarter
dim_date["Weekday"] = dim_date["Date"].dt.day_name()

# -----------------------------
# Fact Table
# -----------------------------
fact = df[[
    "Campaign_ID","Audience_ID","Channel_ID","Date",
    "Impressions","Clicks","Engagement_Score",
    "Conversion_Rate","Acquisition_Cost","ROI"
]]

# Rename Date → Date_ID for consistency
fact = fact.rename(columns={"Date": "Date_ID"})

# Ensure IDs are first
fact = fact[[
    "Campaign_ID","Audience_ID","Channel_ID","Date_ID",
    "Impressions","Clicks","Engagement_Score",
    "Conversion_Rate","Acquisition_Cost","ROI"
]]

# -----------------------------
# Export to Excel (All Sheets)
# -----------------------------
with pd.ExcelWriter("Final_Dataset/Marketing_Dataset.xlsx", engine="xlsxwriter") as writer:
    fact.to_excel(writer, sheet_name="Fact_Campaign", index=False)
    dim_campaign.to_excel(writer, sheet_name="Dim_Campaign", index=False)
    dim_audience.to_excel(writer, sheet_name="Dim_Audience", index=False)
    dim_channel.to_excel(writer, sheet_name="Dim_Channel", index=False)
    dim_date.to_excel(writer, sheet_name="Dim_Date", index=False)

print("✅ Excel file with all sheets created successfully!")