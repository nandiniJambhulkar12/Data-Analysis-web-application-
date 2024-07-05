import streamlit as st   
import pandas as pd     
from helpers import *
import matplotlib.pyplot as plt



summer,winter=data_preprocessor()

# st.dataframe(summer)
# st.dataframe(winter)
# st.write("before")
# st.write(summer.shape)
# st.write(winter.shape)
summer,winter=duplicate_rows_remover(summer,winter)
summer.dropna(subset=["region"],inplace=True)
winter.dropna(subset=["region"],inplace=True)


# st.write("After")
# st.write(summer.shape)
# st.write(winter.shape)
st.sidebar.title("MENU")
season=st.sidebar.radio("Choose season:",("Summer","Winter"))
options=st.sidebar.radio("Options:",("Medal-Tally","Country-Wise","year-Wise","year-Wise progress"))

# medal tally
if season=="Summer" and options=="Medal-Tally":
    st.subheader("Summer olympics Medal Tally")
    medal_pivot_summer=medals_tally_calculator(summer)
    medal_pivot_summer=medal_pivot_summer.sort_values(by=["Gold", "Silver", "Bronze"], ascending=False)
    st.dataframe(medal_pivot_summer,width=700)
    
    
elif season=="Winter" and options=="Medal-Tally":
    st.subheader("Winter olympics Medal Tally")
    medal_pivot_winter=medals_tally_calculator(winter)
    medal_pivot_winter=medal_pivot_winter.sort_values(by=["Gold", "Silver", "Bronze"], ascending=False)
    st.dataframe(medal_pivot_winter,width=700)
    
    
    
    # country wise
elif season=="Summer" and options=="Country-Wise":
    st.subheader("Summer Country-wise Search")
    medal_pivot_summer=medals_tally_calculator(summer)
    noc = st.selectbox("Select NOC:", medal_pivot_summer.index)
    details=country_wise_search(noc,medal_pivot_summer)
    table=pd.DataFrame.from_dict(details,orient="index",columns=["value"])
    st.dataframe(table)
    
elif season=="Winter" and options=="Country-Wise":
    st.subheader("Winter Country-wise Search")
    medal_pivot_winter=medals_tally_calculator(winter)
    noc = st.selectbox("Select NOC:", medal_pivot_winter.index.tolist())
    details=country_wise_search(noc,medal_pivot_winter)
    table=pd.DataFrame.from_dict(details,orient="index",columns=["value"])
    st.dataframe(table)
    
    # year wise
# elif season=="summer" and options=="Year-Wise":
#     st.subheader("summer Year-wise Search")  
    
#     years=sorted(summer["Year"].unique())
#     selected_year=st.selectbox("select year",Year)
# elif season == "Summer" and options == "Year-Wise":
#     st.subheader("Summer Year-wise Search")
    
#     # Ensure the DataFrame 'summer' is defined and has the 'Year' column
#     years = sorted(summer["Year"].unique())
#     selected_year = st.selectbox("Select Year", year)

#     countries= sorted(summer[summer["Year"]==selected_year]["region"].unique())
#     selected_country=st.selectbox("select country",country)
# import streamlit as st
# import pandas as pd

# # Example DataFrame (replace with your actual data loading)
# data = {
#     'Year': [2000, 2004, 2008, 2012, 2016],
#     'Event': ['100m', '200m', '400m', '800m', '1500m'],
#     'Medal': ['Gold', 'Silver', 'Bronze', 'Gold', 'Silver'],
#     'Season': ['Summer', 'Summer', 'Summer', 'Summer', 'Summer']
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Filter the DataFrame for Summer season
# summer = df[df['Season'] == 'Summer']

# # Streamlit app
# st.title("Olympics Analysis")

# Options for the user to choose
# season = st.sidebar.selectbox("Select Season", ["Summer", "Winter"])
# # options = st.sidebar.selectbox("Select Option", ["Year-Wise", "Country-Wise"])
# elif season=="Summer" and options=="Country-Wise":
#     st.subheader("Summer Year-wise Search")
    
#     # Ensure the DataFrame 'summer' is defined and has the 'Year' column
#     years = sorted(summer["Year"].unique())
#     selected_year = st.selectbox("Select Year", years)

    # Additional code to display data or plot based on the selected year
    # Example: Displaying the events and medals for the selected year
    # filtered_data = summer[summer["Year"] == selected_year]
    # st.write(filtered_data)
elif season == "Summer" and options == "year-Wise":
    st.subheader("Summer Year-wise Search")  
    
    years = sorted(summer["Year"].unique())
    selected_year = st.selectbox("Select Year", years)
    countries= sorted(summer[summer["Year"]==selected_year]["region"].unique())
    selected_country=st.selectbox("select country",countries)
    
    plot_medals(selected_year,selected_country,summer)


elif season == "Winter" and options == "year-Wise":
    st.subheader("Winter Year-wise Search")  
    
    years = sorted(winter["Year"].unique())
    selected_year = st.selectbox("Select Year", years)
    countries= sorted(winter[winter["Year"]==selected_year]["region"].unique())
    selected_country=st.selectbox("select country",countries)
    
    plot_medals(selected_year,selected_country,winter)
    
# year wise analysis
elif season == "Summer" and options == "year-Wise progress":
    st.subheader("year overall analysis of a country")
    countries= sorted(summer["region"].unique())
    selected_country=st.selectbox("choose country:",countries)
    year_analysis(selected_country,summer)


else:
    st.subheader("year overall analysis of a country")
    countries= sorted(winter["region"].unique())
    selected_country=st.selectbox("choose country:",countries)
    year_analysis(selected_country,winter)

    
