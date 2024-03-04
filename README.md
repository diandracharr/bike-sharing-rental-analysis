# Bike Sharing Rental Analysis - Final Project Data Analyst
# 1. Background
Bike sharing systems are new generation of traditional bike rentals where whole process from membership, rental and return 
back has become automatic. Through these systems, user is able to easily rent a bike from a particular position and return 
back at another position. Currently, there are about over 500 bike-sharing programs around the world which is composed of 
over 500 thousands bicycles. Today, there exists great interest in these systems due to their important role in traffic, 
environmental and health issues. 

Apart from interesting real world applications of bike sharing systems, the characteristics of data being generated by
these systems make them attractive for the research. Opposed to other transport services such as bus or subway, the duration
of travel, departure and arrival position is explicitly recorded in these systems. This feature turns bike sharing system into
a virtual sensor network that can be used for sensing mobility in the city. Hence, it is expected that most of important
events in the city could be detected via monitoring these data.

# 2. Project Work Cycle
Data Wrangling:
+ Gathering data
+ Assessing data
+ Cleaning data

Exploratory Data Analysis:
+ Defined business questions for data exploration
+ Create Data exploration

Data Visualization:
+ Create Data Visualization that answer business questions

Dashboard:
+ Set up the DataFrame which will be used
+ Make filter components on the dashboard
+ Complete the dashboard with various data visualizations

# 3. Data Set
Bike-sharing rental process is highly correlated to the environmental and seasonal settings. For instance, weather conditions,
precipitation, day of week, season, hour of the day, etc. can affect the rental behaviors. The core data set is related to  
the two-year historical log corresponding to years 2011 and 2012 from Capital Bikeshare system, Washington D.C., USA which is 
publicly available in http://capitalbikeshare.com/system-data. We aggregated the data on two hourly and daily basis and then 
extracted and added the corresponding weather and seasonal information. Weather information are extracted from http://www.freemeteo.com. 

# 4. Install Required Library
Ensure that the essential Python libraries are installed before launching the dashboard. You can install them using the pip command and provided `requirements.txt`.
```
pip install -r requirements.txt
```
# 5. Run Streamlit App
``
python -m streamlit run bike-sharing-rental-analysis/dashboard/bike_share_dashboard.py
``
