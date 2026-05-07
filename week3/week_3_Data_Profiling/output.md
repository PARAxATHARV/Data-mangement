Which columns have many unique values?

The columns with many unique values are Order_ID, Customer_ID, Customer_Name, Order_Date, Ship_Date, Unit_Price, and Sales. These columns contain highly variable transaction and customer-level data, making them more distinct compared to categorical fields.

Which columns may be used as identifiers?

Order_ID and Customer_ID can be used as identifiers because they uniquely represent orders and customers. The Email column may also serve as a customer identifier where values are available and valid.

Are dates, emails, categories, and numeric values valid?

The dataset contains several validation issues. Dates use inconsistent formats and include invalid values such as “not available.” Emails are mostly valid but contain missing values. Categories have inconsistent capitalization and naming variations, while numeric fields are mostly valid except for currency symbols appearing in the Unit_Price column.

How should missing values be handled?

Missing values should be handled based on the importance of the column. Critical fields like Order_Date should be investigated or excluded if unusable, while optional fields such as Notes can remain null. Numerical fields like Age may be filled using median values, and categorical fields such as Payment_Method or Customer_Segment can be replaced with “Unknown.”

Which duplicate records should be removed?

Exact duplicate records should be removed to prevent inaccurate calculations and reporting. Duplicate Order_ID values such as O1005, O1018, O1029, O1048, and O1064 should keep only one valid occurrence.

Which invalid values should be corrected or excluded?

Invalid values such as mixed date formats, placeholders like “not available,” inconsistent category spellings, and currency symbols in numeric fields should be corrected. Records with critical missing or unusable values may need to be excluded from analysis.

In ETL, where would profiling happen?

In ETL, profiling happens after extraction and before loading into the target system. Data is validated, cleaned, standardized, and transformed during the transformation stage so that only high-quality data is loaded.

In ELT, where would profiling happen?

In ELT, profiling happens after the raw data has already been loaded into the data warehouse. Cleaning and transformation are then performed within the warehouse using SQL or other processing tools.

Which approach is better for this dataset and why?

ETL is the better approach for this dataset because it is relatively small and contains many data quality issues such as duplicates, inconsistent categories, mixed date formats, and invalid values. Cleaning the data before loading ensures more accurate and reliable reporting in Tableau Prep.