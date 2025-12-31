import pandas as pd 
import streamlit as st 
import altair as alt

@st.cache_data
def load_data():
    df = pd.read_csv("AirCrachesAnalysis.csv")

    # Rename columns to match expected format
    df = df.rename(columns={
        "Month": "Month Name",
        "Country/Region": "Country",
        "Sum of Fatalities (air)": "Fatalities (air)",
        "Sum of Aboard": "Aboard",
        "Sum of Ground": "Ground"
    })
    df["Month"] = pd.to_datetime(df["Month Name"], format='%B', errors="coerce").dt.month
    df["Date"] = pd.to_datetime(df[["Year", "Month", "Day"]], errors="coerce")

    irrelevant_values = [
         '', ' ', '  ', "'-", '10', '100', '110', '116', '18', '325', '570', '800', 'Aaland', 'Aargau', 'Africa', 'Aichi', 'Air', 'Airlines',
    'Arizona', 'Airzona', 'Alberta', 'Algarve', 'Channel', 'Lowa', 'Mt', 'N', 'Chechnya', 'Argyll','Ayrshire', 'Azores', 'Azuay', 'BC',  'Besar',
    'Biafra', 'Bias', 'Black', 'British', 'Buea', 'Cape', 'Cargo', 'Central', 'FL', 'Inner', 'El', 'East', 'DR', 'De', 'de', 'Da', 'D.C.Capital', 'D.C.Air',
    'Crete', 'Corsica', 'Cook', 'Cocos', 'Cheshire', 'N/A', 'NE', 'near', 'North', 'Northern', 'Northwest', 'NSW', 'NWT', 'NYUS', 'off', 'OLD', 'ON', 'PE', 
    'PQ', 'QC', 'Qld.', 'Quebec', 'Queens', 'Queesland', 'SC', 'WYUS', 'West', 'The', 'Sri', 'New', 'St.', 'South-West', 'South', 'SK', 'Saint', 'Saskatchewan', 'Stirlingshire'
    ]
    df["Country"] = df["Country"].replace(irrelevant_values, "Not Specified")
    df["Country"] = df["Country"].fillna("Not Specified")

    country_corrections = {
    'Alaska': 'United States', ' Alaska': 'United States', 'Alaksa': 'United States', 'Alabama': 'United States', 'California': 'United States', 'Chicago': 'United States',
    'Idaho': 'United States', 'Illinois': 'United States', 'Kent': 'United States', 'Kansas': 'United States', 'Kentucky': 'United States', 'Louisinana': 'United States', 'Maine': 'United States',
    'Maryland': 'United States', 'Massachusetts': 'United States', 'Michigan': 'United States', 'Minnesota': 'United States', 'Oklahoma': 'United States', 'Oregan': 'United States', 'Tennesee': 'United States',
    'Tennessee': 'United States', 'Texas': 'United States', 'United': 'United States', 'Utah': 'United States', 'Mississippi': 'United States', 'Missouri': 'United States', 'Wyoming': 'United States', 'Wisconsin': 'United States',
    'Washington': 'United States', 'Virginia': 'United States', 'Virgin': 'United States', 'Vera': 'United States', 'Ohio': 'United States', 'Nevada': 'United States', 'Vermont': 'United States', 'Colorado': 'United States',
    'Coloado': 'United States', 'Florida?': 'United States', 'Indiana': 'United States', 'Austalila': 'Australia', 'Austrailia': 'Australia', 'Australlia': 'Australia', 'USA': 'United States', 'US': 'United States',
    'UK': 'United Kingdom','Britain': 'United Kingdom', 'England': 'United Kingdom', 'Scotland': 'United Kingdom','London': 'United Kingdom', 'Wales': 'United Kingdom', 'USSR': 'Russia', 'Soviet Union': 'Russia',
    'West Germany': 'Germany', 'East Germany': 'Germany', 'Beni': 'Benin', 'Brazil Amazonaves': 'Brazil','Brazil Loide': 'Brazil', 'Bugaria': 'Bulgaria', 'Calabria': 'Italy', 'Cameroons': 'Cameroon', 'Quebec': 'Canada',
    'Manitoba': 'Canada','Nunavut': 'Canada','China?': 'China','Corsica': 'France', 'French': 'France','Costa': 'Costa Rica', 'Democratic': 'Denmark', 'India Pawan': 'India', 'Zaire': 'Congo', 'Yugosalvia': 'Yugoslavia',
    'Norway CHC': 'Norway', 'Sarawak': 'Malaysia', 'Spain Moron': 'Spain', 'Terceira': 'Portugal', 'Canary': 'Spain', 'AKAlaska': 'United States', 'Afghanstan': 'Afghanistan', 'Alakska': 'United States', 'American': 'United States', ' NWT Canada': 'Canada',
    }
    df["Country"] = df["Country"].replace(country_corrections)

    continent = {
    'United States': 'North America',
    'Canada': 'North America',
    'Mexico': 'North America',
    'Guatemala': 'North America',
    'Belize': 'North America',
    'Honduras': 'North America',
    'El Salvador': 'North America',
    'Nicaragua': 'North America',
    'Costa Rica': 'North America',
    'Panama': 'North America',
    'Cuba': 'North America',
    'Jamaica': 'North America',
    'Haiti': 'North America',
    'Dominican Republic': 'North America',
    'Bahamas': 'North America',
    
    'Brazil': 'South America',
    'Argentina': 'South America',
    'Chile': 'South America',
    'Peru': 'South America',
    'Colombia': 'South America',
    'Venezuela': 'South America',
     'Ecuador': 'South America',
    'Bolivia': 'South America',
    'Paraguay': 'South America',
    'Uruguay': 'South America',
    'Guyana': 'South America',
    'Suriname': 'South America',
    
    'United Kingdom': 'Europe',
    'Germany': 'Europe',
    'France': 'Europe',
    'Italy': 'Europe',
    'Spain': 'Europe',
    'Portugal': 'Europe',
    'Netherlands': 'Europe',
    'Belgium': 'Europe',
    'Switzerland': 'Europe',
    'Austria': 'Europe',
    'Norway': 'Europe',
    'Sweden': 'Europe',
    'Denmark': 'Europe',
    'Finland': 'Europe',
    'Russia': 'Europe',  
    'Poland': 'Europe',
    'Czech Republic': 'Europe',
    'Slovakia': 'Europe',
    'Hungary': 'Europe',
    'Romania': 'Europe',
     'Bulgaria': 'Europe',
    'Greece': 'Europe',
    'Yugoslavia': 'Europe',
    'Croatia': 'Europe',
    'Serbia': 'Europe',
    'Bosnia': 'Europe',
    'Slovenia': 'Europe',
    'Ukraine': 'Europe',
    'Belarus': 'Europe',
    'Ireland': 'Europe',
    'Iceland': 'Europe',
    
    'China': 'Asia',
    'India': 'Asia',
    'Japan': 'Asia',
    'South Korea': 'Asia',
    'North Korea': 'Asia',
    'Thailand': 'Asia',
    'Vietnam': 'Asia',
    'Malaysia': 'Asia',
    'Singapore': 'Asia',
    'Indonesia': 'Asia',
    'Philippines': 'Asia',
    'Myanmar': 'Asia',
    'Cambodia': 'Asia',
    'Laos': 'Asia',
    'Nepal': 'Asia',
    'Bangladesh': 'Asia',
    'Pakistan': 'Asia',
    'Afghanistan': 'Asia',
    'Iran': 'Asia',
    'Iraq': 'Asia',
    'Saudi Arabia': 'Asia',
    'Turkey': 'Asia',
    'Israel': 'Asia',
    'Jordan': 'Asia',
    'Syria': 'Asia',
    'Lebanon': 'Asia',
    
    'Nigeria': 'Africa',
    'South Africa': 'Africa',
    'Kenya': 'Africa',
    'Ethiopia': 'Africa',
    'Ghana': 'Africa',
    'Egypt': 'Africa',
    'Morocco': 'Africa',
    'Algeria': 'Africa',
    'Tunisia': 'Africa',
    'Libya': 'Africa',
    'Sudan': 'Africa',
    'Uganda': 'Africa',
    'Tanzania': 'Africa',
    'Zambia': 'Africa',
    'Zimbabwe': 'Africa',
     'Botswana': 'Africa',
    'Namibia': 'Africa',
    'Angola': 'Africa',
    'Congo': 'Africa',
    'Cameroon': 'Africa',
    'Benin': 'Africa',
    'Somalia': 'Africa',
    
    'Australia': 'Oceania',
    'New Zealand': 'Oceania',
    'Papua New Guinea': 'Oceania',
    'Fiji': 'Oceania',
    
    'Not Specified': 'Not Specified'
    }
    df["Continent"] = df["Country"].map(continent)
    df['Continent'] = df['Continent'].fillna('Not Specify')

    df['Aircraft Manufacturer'] = df['Aircraft Manufacturer'].str.strip()  
    problematic_entries = ['??', '?VH', '?NC21V', 'Unknown /', 'C', 'UH', 'DC', 'PA', 'VC', '?139', '?VP', '?42', '']
    df['Aircraft Manufacturer'] = df['Aircraft Manufacturer'].replace(problematic_entries, 'Not Specified')

    manufacturer_corrections = {
    'Doublas': 'Douglas',
    'MD Douglas': 'McDonnell Douglas',
    'De Havilland': 'de Havilland',
    'de Hvilland 89A Dragon': 'de Havilland',
    'de Havilland  Canada': 'de Havilland Canada',
    'de Havilland DH106 Comet': 'de Havilland',
    'de Havilland DH.80 Puss': 'de Havilland',
    'Cessna 208B Caravan': 'Cessna',
    'Cessna  208B Grand': 'Cessna',
    'Cessna 208 Grand': 'Cessna',
    'Cessna 208B Grand': 'Cessna',
    'Cessna 208B Caravan I Super': 'Cessna',
    'Cessna  501': 'Cessna',
    'Boeing 377 Stratocruiser': 'Boeing',
    'Boeing Vertol CH47C': 'Boeing Vertol',
    'Boeing Vertol CH47B': 'Boeing Vertol',
    'Boeing Vertol': 'Boeing',
    'Lockheed 14': 'Lockheed',
    'Lockheed 18': 'Lockheed',
    'Lockheed 14 Super': 'Lockheed',
    'Lockheed 749A': 'Lockheed',
    'Lockheed 188C': 'Lockheed',
    'Lockheed 188A': 'Lockheed',
    'Lockheed 1049H Super': 'Lockheed',
    'Lockheed 1049G Super': 'Lockheed',
    'Lockheed Hudson': 'Lockheed',
    'Lockheed Super': 'Lockheed',
    'Lockheed 10': 'Lockheed',
    'Lockheed 10 Electra': 'Lockheed',
    'Lockheed 10B': 'Lockheed',
    'Lockheed 10E': 'Lockheed',
    'Lockheed 9': 'Lockheed',
    'Lockheed Orion 9E Explorer float': 'Lockheed',
    'Lockheed 5': 'Lockheed',
    'Lockheed Vega': 'Lockheed',
    'Lockheed Martin': 'Lockheed',
    'Embraer 110EJ Band./Embraer 110P': 'Embraer',
    'Embraer/Piper': 'Embraer',
    'Embraer 110P1': 'Embraer',
    'Embraer 120ER': 'Embraer',
    'Embraer 110': 'Embraer',
    'Embraer 120': 'Embraer',
    'Fokker FG': 'Fokker',
    'Vickers Vanguard': 'Vickers',
    'Vickers Viscount': 'Vickers',
    'Vickers 610 Viking': 'Vickers',
    'Vickers Viking 1B & Soviet': 'Vickers',
    'Vickers Valetta': 'Vickers',
    'Vickers Wellington': 'Vickers',
    'Vickers 757': 'Vickers',
    'Vickers 804': 'Vickers',
    'Vickers 634 Viking': 'Vickers',
    'Vickers 815': 'Vickers',
    'Vickers 708': 'Vickers',
    'Vickers Viscount 827 / Fokker': 'Vickers',
    'Vickers Viscount 764': 'Vickers',
    'Vickers Viking': 'Vickers',
    'AeroflotL5057': 'Antonov',
    'Avro 685 York': 'Avro',
    'Avro Shackleton': 'Avro',
    'Avro 691 Lancastrian': 'Avro',
    'Avro 688 Super': 'Avro',
    'Avro Lancaster': 'Avro',
    'Avro  685 York': 'Avro',
    'Bell 212FAC': 'Bell',
    'Bell 205': 'Bell',
    'Bell 206B': 'Bell',
    'Bell Huey': 'Bell',
    'British Aerospace BAe': 'British Aerospace',
    'Consolidated Canso': 'Consolidated',
    'Curtis': 'Curtiss',
    'Curtiss C': 'Curtiss',
    'Dassault Falcon': 'Dassault',
    'Eurocopter Deutschland': 'Eurocopter',
    'Let 410UVP': 'Let',
    'Let 410UVP Turbojet / Tupolev': 'Let',
    'LET 410M': 'Let',
    'Gates Learjet': 'Learjet',
    'Mi': 'Mil',
    'Mil Mi 8T': 'Mil',
    'Piper Aerostar 601 / Bell 412SPN3645D /': 'Piper',
    'Piper Navajo': 'Piper',
    'Pilatus Britten Norman': 'Pilatus',
    'Sikorsky S43 (flying': 'Sikorsky',
    'Sud Aviation Caravelle': 'Sud Aviation',
    'Sud Aviation SE 210 Caravelle': 'Sud Aviation',
    'Sud': 'Sud Aviation',
    'Swearingen SA227AC Metroliner': 'Swearingen',
    'Swearingen SA.227AC Metro': 'Swearingen',
    'Hadley Page 137Jetstream I / Cessna 206N11360 /': 'Handley Page',
    'B17G Flying': 'Boeing',
    'Catalina Flying': 'Consolidated',
    'Supermarine Stranraer (flying': 'Supermarine',
    'Beechcraft C99 / Rockwell': 'Beechcraft',
    'Short Sandringham (flying': 'Short',
    'Short Sandringham 5 (flying': 'Short',
    'Short S23 \'C\' Class flying': 'Short',
    'Latecoere 631 (flying': 'Latecoere',
    'Latécoère 23 (flying': 'Latecoere',
    'Latécoère 300 (float': 'Latecoere',
    'Avro 691 Lancastrian (flying': 'Avro',
    'Aerospatiale AS350 Eurocopter': 'Aerospatiale',
    'Aerospatiale Caravelle': 'Aerospatiale',
    'Aerocomp Comp Air': 'Aerocomp',
    'Bristol Britannia': 'Bristol',
    'Bristol 170 Freighter': 'Bristol',
    'Bristol 170': 'Bristol',
    'Bristol 175 Britannia': 'Bristol',
    'Bristol 28': 'Bristol',
    'Eurocopter EC225LP Super Puma M2+': 'Eurocopter',
    'Eurocopter AS 332L2 Super Puma': 'Eurocopter',
    'Grumman G73T Turbo': 'Grumman',
    'Hawker Siddeley Trident': 'Hawker Siddeley',
    'Hindustan Aeronautics 748': 'Hindustan Aeronautics',
    }
    df['Aircraft Manufacturer'] = df['Aircraft Manufacturer'].replace(manufacturer_corrections)

    manufacturer_type_category = {
    'Boeing': 'Major Commercial',
    'Airbus': 'Major Commercial',
    'McDonnell Douglas': 'Major Commercial',
    'Lockheed': 'Major Commercial',
    
    'Douglas': 'Legacy Commercial',
    'Convair': 'Legacy Commercial',
    'de Havilland': 'Legacy Commercial',
    'Vickers': 'Legacy Commercial',
    'Bristol': 'Legacy Commercial',
    'Avro': 'Legacy Commercial',
    
    'Cessna': 'General Aviation',
    'Piper': 'General Aviation',
    'Beechcraft': 'General Aviation',
    'Cirrus': 'General Aviation',
    
    'Fokker': 'Regional',
    'Embraer': 'Regional',
    'Bombardier': 'Regional',
    'ATR': 'Regional',
    'Saab': 'Regional',
    'Dornier': 'Regional',
    'de Havilland Canada': 'Regional',
    
    'Bell': 'Helicopter',
    'Sikorsky': 'Helicopter',
    'Eurocopter': 'Helicopter',
    'Mil': 'Helicopter',
    
    'Curtiss': 'Military/Historical',
    'Grumman': 'Military/Historical',
    'Consolidated': 'Military/Historical',
    'Junkers': 'Military/Historical',
    'Messerschmitt': 'Military/Historical',
    
    'Antonov': 'Soviet/Eastern Bloc',
    'Ilyushin': 'Soviet/Eastern Bloc',
    'Tupolev': 'Soviet/Eastern Bloc',
    'Yakovlev': 'Soviet/Eastern Bloc',
    
    'Not Specified': 'Not Specified',
    }
    df['Manufacturer_Category'] = df['Aircraft Manufacturer'].map(manufacturer_type_category)
    df['Manufacturer_Category'] = df['Manufacturer_Category'].fillna('Not Specify')

    df['Aircraft'] = df['Aircraft'].str.strip()
    non_valid_entries = ['??', '?NC21V', '?VH  TAT', 'Unknown / Unknown?', 'C  47(DC', '"Swallow', 'Swallow?"']
    df['Aircraft'] = df['Aircraft'].replace(non_valid_entries, 'Not Specified')  
    df['Aircraft'] = df['Aircraft'].str.replace(r'\s*\(\?\)', '', regex=True)

    aircraft_corrections = {
    'Boeing B 737': 'Boeing 737',
    'Boeing B 727': 'Boeing 727',
    'Boeing B 747': 'Boeing 747',
    'Boeing B 707': 'Boeing 707',
    'Airbus A 300': 'Airbus A300',
    'Airbus A 320': 'Airbus A320',
    'Lockheed L 188': 'Lockheed L-188',
    'Douglas DC 3': 'Douglas DC-3',
    'Douglas DC 4': 'Douglas DC-4',
    'Douglas DC 6': 'Douglas DC-6',
    'Fokker F 27': 'Fokker F-27',
    }
    df['Aircraft'] = df['Aircraft'].replace(aircraft_corrections)

    aircraft_type_category = {
    'Douglas DC-3': 'Vintage Commercial',
    'Douglas DC-4': 'Vintage Commercial',
    'Douglas DC-6': 'Vintage Commercial',
    'Lockheed Constellation': 'Vintage Commercial',
    
    'Boeing 707': 'Jet Commercial',
    'Boeing 727': 'Jet Commercial',
    'Boeing 737': 'Jet Commercial',
    'Boeing 747': 'Jet Commercial',
    'Boeing 757': 'Jet Commercial',
    'Boeing 767': 'Jet Commercial',
    'Airbus A300': 'Jet Commercial',
    'Airbus A310': 'Jet Commercial',
    'Airbus A320': 'Jet Commercial',
    'McDonnell Douglas DC-9': 'Jet Commercial',
    'McDonnell Douglas DC-10': 'Jet Commercial',
    'McDonnell Douglas MD-80': 'Jet Commercial',
    
    'Fokker F-27': 'Regional Prop',
    'ATR 42': 'Regional Prop',
    'ATR 72': 'Regional Prop',
    'de Havilland DHC-6': 'Regional Prop',
    
    'Cessna 172': 'Light Aircraft',
    'Cessna 182': 'Light Aircraft',
    'Piper Cherokee': 'Light Aircraft',
    'Piper Cub': 'Light Aircraft',
    
    'Bell 47': 'Helicopter',
    'Bell 206': 'Helicopter',
    'Sikorsky S-61': 'Helicopter',
    
    'Not Specified': 'Not Specified',
    }
    df['Aircraft_Category'] = df['Aircraft'].map(aircraft_type_category)
    df['Aircraft_Category'] = df['Aircraft_Category'].fillna('Not Specify')

    df['Severity_Level'] = pd.cut(
        df['Fatalities (air)'],
        bins=[-1, 0, 10, 50, 100, float('inf')],
        labels=['No Fatalities', 'Minor (1-10)', 'Moderate (11-50)', 'Severe (51-100)', 'Catastrophic (>100)']
    )

    df['Decade'] = (df['Year'] // 10) * 10
    df['Fatality_Rate'] = (df['Fatalities (air)'] / df['Aboard']) * 100

    return df

try:
    df = load_data()

    st.title("✈️ Aviation Crash Analysis Dashboard")
    st.write("""
        This dashboard provides an interactive analysis of aviation accidents throughout history. 
        Use the sidebar to filter data and explore various metrics and visualizations.
    """)

    st.sidebar.header("Filters")

    unique_countries = sorted(df["Country"].unique())
    selected_countries = st.sidebar.multiselect(
        "Select Countries",
        options=unique_countries,
        default=unique_countries
    )

    unique_continents = sorted(df["Continent"].unique())
    selected_continents = st.sidebar.multiselect(
        "Select Continents",
        options=unique_continents,
        default=unique_continents
    )

    unique_category = sorted(df["Manufacturer_Category"].unique())
    selected_category = st.sidebar.multiselect(
        "Select Manufacturer Categories",
        options=unique_category,
        default=unique_category
    )

    unique_months = sorted(df["Month Name"].unique(), key=lambda x: pd.to_datetime(x, format='%B', errors='coerce'))
    selected_months = st.sidebar.multiselect(
        "Select Months",
        options=unique_months,
        default=unique_months
    )

    unique_severity = ['All'] + sorted(df['Severity_Level'].dropna().unique().tolist())
    selected_severity = st.sidebar.selectbox(
        "Select Severity Level",
        options=unique_severity,
        index=0
    )

    unique_decades = sorted(df["Decade"].unique())
    decades_range = st.sidebar.slider(
        "Select Decade Range",
        min_value=int(unique_decades[0]),
        max_value=int(unique_decades[-1]),
        value=(int(unique_decades[0]), int(unique_decades[-1]))
    )

    filtered_df = df.copy()
    filtered_df = filtered_df[filtered_df["Country"].isin(selected_countries)]
    filtered_df = filtered_df[filtered_df["Continent"].isin(selected_continents)]
    filtered_df = filtered_df[filtered_df["Manufacturer_Category"].isin(selected_category)]
    filtered_df = filtered_df[filtered_df["Month Name"].isin(selected_months)]

    if selected_severity != 'All':
        filtered_df = filtered_df[filtered_df['Severity_Level'] == selected_severity]

    filtered_df = filtered_df[
        (filtered_df['Decade'] >= decades_range[0]) &
        (filtered_df['Decade'] <= decades_range[1])
    ]

    no_of_crashes = len(filtered_df)
    total_fatalities = filtered_df["Fatalities (air)"].sum()
    avg_fatalities = filtered_df["Fatalities (air)"].mean()
    fatality_rate = (filtered_df["Fatalities (air)"].sum() / filtered_df["Aboard"].sum()) * 100
    top_manufacturer = filtered_df['Aircraft Manufacturer'].value_counts().idxmax()

    st.write("### KPI Overview")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Total Crashes", no_of_crashes)
    with col2:
        st.metric("Total Fatalities", f"{total_fatalities:,}")
    with col3:
        st.metric("Avg. Fatalities", f"{avg_fatalities:.2f}")
    with col4:
        st.metric("Fatality Rate", f"{fatality_rate:.2f}%")
    with col5:
        st.metric("Top Manufacturer in Crashes", top_manufacturer)

    st.write("### Research Analysis Questions")

    st.header("1. Which Countries Experience The Most Aviation Accidents?")
    q1 = filtered_df.groupby('Country').size().sort_values(ascending=False).head(15)
    st.write(q1)
    q1_df = q1.reset_index(name='Crash_Count')
    chart1 = alt.Chart(q1_df).mark_bar().encode(
        x=alt.X("Crash_Count:Q", title="Number of Crashes"),
        y=alt.Y("Country:N", sort='-x', title="Country"),
        color=alt.Color("Crash_Count:Q", scale=alt.Scale(scheme="oranges")),
        tooltip=["Country", "Crash_Count"]
    ).properties(
        title="Top 15 Countries By Aviation Accidents"
    )
    st.altair_chart(chart1, use_container_width=True)

    st.header("2. Which Aircraft Manufacturers Have The Most Accidents?")
    q2 = filtered_df.groupby('Aircraft Manufacturer').size().sort_values(ascending=False).head(10)
    st.write(q2)
    q2_df = q2.reset_index(name='Accident_Count')
    chart2 = alt.Chart(q2_df).mark_bar(color='steelblue').encode(
        x=alt.X('Accident_Count:Q', title='Number of Accidents'),
        y=alt.Y('Aircraft Manufacturer:N', sort='-x', title='Manufacturer'),
        tooltip=['Aircraft Manufacturer', 'Accident_Count']
    ).properties(
        title='Top 10 Aircraft Manufacturers By Accident Count'
    )
    st.altair_chart(chart2, use_container_width=True)

    st.header("3. What Are The Trends In Aviation Accidents Over Time?")
    q3 = filtered_df.groupby('Year').size().reset_index(name='Accident_Count')
    st.write(q3)
    chart3 = alt.Chart(q3).mark_line(point=True, color='green').encode(
        x=alt.X('Year:O', title='Year'),
        y=alt.Y('Accident_Count:Q', title='Number of Accidents'),
        tooltip=['Year', 'Accident_Count']
    ).properties(
        title='Aviation Accidents Over Time'
    )
    st.altair_chart(chart3, use_container_width=True)

    st.header("4. Which Months See The Most Accidents?")
    q4 = filtered_df.groupby('Month Name').size().reset_index(name='Accident_Count')
    q4['Month_Order'] = pd.to_datetime(q4['Month Name'], format='%B').dt.month
    q4 = q4.sort_values('Month_Order')
    st.write(q4[['Month Name', 'Accident_Count']])
    chart4 = alt.Chart(q4).mark_bar(color='coral').encode(
        x=alt.X('Month Name:N', sort=list(q4['Month Name']), title='Month'),
        y=alt.Y('Accident_Count:Q', title='Number of Accidents'),
        tooltip=['Month Name', 'Accident_Count']
    ).properties(
        title='Accident Distribution By Month'
    )
    st.altair_chart(chart4, use_container_width=True)

    st.header("5. What Is The Distribution Of Crash Severity Levels?")
    q5 = filtered_df['Severity_Level'].value_counts().reset_index()
    q5.columns = ['Severity_Level', 'Count']
    st.write(q5)
    chart5 = alt.Chart(q5).mark_arc().encode(
        theta=alt.Theta('Count:Q'),
        color=alt.Color('Severity_Level:N', scale=alt.Scale(scheme='category10')),
        tooltip=['Severity_Level', 'Count']
    ).properties(
        title='Distribution of Crash Severity Levels'
    )
    st.altair_chart(chart5, use_container_width=True)

    st.header("6. How Do Survival Rates Vary By Decade?")
    filtered_df['Survival_Count'] = filtered_df['Aboard'] - filtered_df['Fatalities (air)']
    q6 = filtered_df.groupby('Decade').agg({
        'Survival_Count': 'sum',
        'Aboard': 'sum'
    }).reset_index()
    q6['Survival_Rate'] = (q6['Survival_Count'] / q6['Aboard']) * 100
    st.write(q6)
    chart6 = alt.Chart(q6).mark_line(point=True, color='purple').encode(
        x=alt.X('Decade:O', title='Decade'),
        y=alt.Y('Survival_Rate:Q', title='Survival Rate (%)'),
        tooltip=['Decade', alt.Tooltip('Survival_Rate:Q', format='.2f')]
    ).properties(
        title='Survival Rate Trends By Decade'
    )
    st.altair_chart(chart6, use_container_width=True)

    st.header("7. What Percentage Of Accidents Result In Total Loss For Each Manufacturer Category?")
    q7 = filtered_df.groupby('Manufacturer_Category').agg({
        'Fatalities (air)': 'sum',
        'Aboard': 'sum'
    }).reset_index()
    q7['Total_Loss_Percentage'] = (q7['Fatalities (air)'] / q7['Aboard']) * 100
    q7 = q7.sort_values('Total_Loss_Percentage', ascending=False)
    q7_pct = q7[['Manufacturer_Category', 'Total_Loss_Percentage']]
    q7_pct.columns = ['Manufacturer_Category', 'Total_Loss_Percentage']
    st.write(q7_pct)
    chart7 = alt.Chart(q7_pct).mark_bar().encode(
        x=alt.X('Total_Loss_Percentage:Q', title='Total Loss Percentage (%)'),
        y=alt.Y('Manufacturer_Category:N', sort='-x', title='Manufacturer Category'),
        color=alt.Color('Total_Loss_Percentage:Q', scale=alt.Scale(scheme='reds')),
        tooltip=['Manufacturer_Category', alt.Tooltip('Total_Loss_Percentage:Q', format='.2f')]
    ).properties(
        title='Total Loss Percentage By Manufacturer Category'
    )
    st.altair_chart(chart7, use_container_width=True)

    st.header("8. How Do Ground Casualties Per Crash Compare Across Continents?")
    q8 = filtered_df.groupby('Continent').agg({
        'Ground': 'sum',
        'Country': 'size'
    }).rename(columns={'Country': 'Crash_Count'})
    q8['Ground_Per_Crash'] = q8['Ground'] / q8['Crash_Count']
    q8 = q8.reset_index()
    st.write(q8)
    chart8 = alt.Chart(q8).mark_bar().encode(
        x=alt.X('Continent:N', title='Continent'),
        y=alt.Y('Ground_Per_Crash:Q', title='Avg Ground Casualties Per Crash'),
        color=alt.Color('Ground_Per_Crash:Q', scale=alt.Scale(scheme='purples')),
        tooltip=['Continent', alt.Tooltip('Ground_Per_Crash:Q', format='.2f'), 'Ground', 'Crash_Count']
    ).properties(
        title='Average Ground Casualties Per Crash By Continent'
    )
    st.altair_chart(chart8, use_container_width=True)

    st.header("9. Which Years Had The Deadliest Single Accidents?")
    q9 = filtered_df.groupby('Year')['Fatalities (air)'].max().sort_values(ascending=False).head(15)
    st.write(q9)
    q9_df = q9.reset_index()
    chart9 = alt.Chart(q9_df).mark_bar(color='darkred').encode(
        x=alt.X('Year:O', title='Year'),
        y=alt.Y('Fatalities (air):Q', title='Maximum Fatalities In Single Accident'),
        tooltip=['Year', 'Fatalities (air)']
    ).properties(
        title='Top 15 Years With Deadliest Single Accidents'
    )
    st.altair_chart(chart9, use_container_width=True)

    st.header("10. How Do Crash Incident Rates Compare Between Regional And Commercial Aircraft?")
    commercial_cats = ['Major Commercial', 'Legacy Commercial', 'Regional']
    q10 = filtered_df[filtered_df['Manufacturer_Category'].isin(commercial_cats)].groupby('Manufacturer_Category').size().reset_index(name='Incident_Count')
    st.write(q10)
    chart10 = alt.Chart(q10).mark_arc(innerRadius=50).encode(
        theta=alt.Theta('Incident_Count:Q', title='Incident Count'),
        color=alt.Color('Manufacturer_Category:N', title='Category'),
        tooltip=['Manufacturer_Category', 'Incident_Count']
    ).properties(
        title='Incident Distribution: Commercial vs Regional Aircraft'
    )
    st.altair_chart(chart10, use_container_width=True)

except FileNotFoundError:
    st.error("The file was not found. Please check the file path.")
except pd.errors.EmptyDataError:
    st.error("The file is empty. Please check the file contents.")
except Exception as e:
    st.error(f"An error occurred: {e}")
