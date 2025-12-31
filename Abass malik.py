import pandas as pd 
import streamlit as st 
import altair as alt

@st.cache_data
def load_data():
    df = pd.read_csv("AirCrachesAnalysis.csv")

    df = df.rename(columns={"Month" : "Month Name"})
    df = df.rename(columns={"Country/Region" : "Country"})
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
    'Boeing B 707': 'Boeing 707',
    'Boeing B 727': 'Boeing 727', 
    'Boeing B 737': 'Boeing 737',
    'Boeing B 747': 'Boeing 747',
    'Boeing B 757': 'Boeing 757',
    'Boeing B 767': 'Boeing 767',
    'Boeing B 777': 'Boeing 777',
    'Boeing KC': 'Boeing KC-135',
    'Boeing CH': 'Boeing CH-47',
    'Boeing 40': 'Boeing 40',
    'Boeing 377': 'Boeing 377',
    'Boeing 707': 'Boeing 707',
    'Boeing 720': 'Boeing 720',
    'Boeing 727': 'Boeing 727',
    'Boeing 737': 'Boeing 737',
    'Boeing 747': 'Boeing 747',
    'Boeing 777': 'Boeing 777',
    'Boeing Vertol CH47C': 'Boeing CH-47',
    'Boeing Vertol CH47B': 'Boeing CH-47',
    'Boeing Vertol CH': 'Boeing CH-47',
    'Doublas Dc': 'Douglas DC-3',
    'Douglas C': 'Douglas C-47',
    'Douglas DC': 'Douglas DC-3',
    'Douglas C 47': 'Douglas C-47',
    'Douglas C 47A': 'Douglas C-47',
    'Douglas C 47B': 'Douglas C-47',
    'Douglas C 47C': 'Douglas C-47',
    'Douglas C 47D': 'Douglas C-47',
    'Douglas DC 2': 'Douglas DC-2',
    'Douglas DC 3': 'Douglas DC-3',
    'Douglas DC 4': 'Douglas DC-4',
    'Douglas DC 6': 'Douglas DC-6',
    'Douglas DC 6A': 'Douglas DC-6',
    'Douglas DC 6B': 'Douglas DC-6',
    'Douglas DC 7': 'Douglas DC-7',
    'Douglas DC 8': 'Douglas DC-8',
    'Douglas DC 9': 'Douglas DC-9',
    'Douglas C 54': 'Douglas C-54',
    'Douglas C 54A': 'Douglas C-54',
    'Douglas C 54B': 'Douglas C-54',
    'Douglas C 54D': 'Douglas C-54',
    'Douglas C 118A': 'Douglas C-118',
    'Douglas C 124C': 'Douglas C-124',
    'MD Douglas DC': 'McDonnell Douglas DC-9',
    'McDonnell Douglas DC': 'McDonnell Douglas DC-9',
    'McDonnell Douglas MD': 'McDonnell Douglas MD-80',
    'McDonnell Douglas DC 8': 'McDonnell Douglas DC-8',
    'McDonnell Douglas DC 9': 'McDonnell Douglas DC-9',
    'McDonnell Douglas DC 10': 'McDonnell Douglas DC-10',
    'McDonnell Douglas MD 11': 'McDonnell Douglas MD-11',
    'McDonnell Douglas MD 82': 'McDonnell Douglas MD-82',
    'McDonnell Douglas MD 90': 'McDonnell Douglas MD-90',
    'Lockheed C': 'Lockheed C-130',
    'Lockheed L': 'Lockheed L-1011',
    'Lockheed 10': 'Lockheed L-10',
    'Lockheed 14': 'Lockheed L-14',
    'Lockheed 18': 'Lockheed L-18',
    'Lockheed Hudson': 'Lockheed Hudson',
    'Lockheed P': 'Lockheed P-3',
    'Lockheed 749A': 'Lockheed L-749',
    'Lockheed 1049G': 'Lockheed L-1049',
    'Lockheed 1049H': 'Lockheed L-1049',
    'Lockheed 1011': 'Lockheed L-1011',
    'Lockheed Martin L': 'Lockheed L-100',
    'Antonov AN': 'Antonov An-24',
    'Antonov An': 'Antonov An-24',
    'Antonov 12': 'Antonov An-12',
    'Antonov 26': 'Antonov An-26',
    'Antonov 28': 'Antonov An-28',
    'Antonov 32': 'Antonov An-32',
    'Antonov 74': 'Antonov An-74',
    'Ilyushin IL': 'Ilyushin Il-18',
    'Ilyushin Il': 'Ilyushin Il-18',
    'Tupolev TU': 'Tupolev Tu-154',
    'Tupolev Tu': 'Tupolev Tu-154',
    'Tupolev 134A': 'Tupolev Tu-134',
    'Tupolev 154B': 'Tupolev Tu-154',
    'Tupolev 154M': 'Tupolev Tu-154',
    'de Havilland Canada DHC': 'de Havilland DHC-6',
    'de Havilland DHC': 'de Havilland DHC-6',
    'De Havilland DH': 'de Havilland DH-114',
    'de Havilland DH': 'de Havilland DH-114',
    'de Hvilland': 'de Havilland Dragon Rapide',
    'Fokker F': 'Fokker F-27',
    'Fokker FG': 'Fokker F.VII',
    'Vickers Viscount': 'Vickers Viscount',
    'Vickers Viking': 'Vickers Viking',
    'Vickers 634': 'Vickers Viking',
    'Vickers 610': 'Vickers Viking',
    'Vickers 708': 'Vickers Viscount',
    'Vickers 745': 'Vickers Viscount',
    'Vickers 757': 'Vickers Viscount',
    'Vickers 764': 'Vickers Viscount',
    'Vickers 785': 'Vickers Viscount',
    'Vickers 804': 'Vickers Viscount',
    'Vickers 812': 'Vickers Viscount',
    'Vickers 815': 'Vickers Viscount',
    'Vickers 827': 'Vickers Viscount',
    'Curtis C': 'Curtiss C-46',
    'Curtiss C': 'Curtiss C-46',
    'Curtiss JN': 'Curtiss JN-4',
    'Airbus A300B4': 'Airbus A300',
    'Airbus A300F': 'Airbus A300',
    'Airbus A320': 'Airbus A320',
    'Airbus A330': 'Airbus A330',
    'Airbus A340': 'Airbus A340',
    'Cessna 172': 'Cessna 172',
    'Cessna 177': 'Cessna 177',
    'Cessna 185': 'Cessna 185',
    'Cessna 208B': 'Cessna 208',
    'Cessna 206': 'Cessna 206',
    'Cessna 402C': 'Cessna 402',
    'Cessna 501': 'Cessna Citation',
    'Bell 206': 'Bell 206',
    'Bell 212': 'Bell 212',
    'Bell 205': 'Bell 205',
    'Bell Huey': 'Bell UH-1',
    'UH': 'Bell UH-60',
    'Embraer 110': 'Embraer EMB-110',
    'Embraer 120': 'Embraer EMB-120',
    'Embraer ERJ': 'Embraer ERJ-190',
    'Junkers JU': 'Junkers Ju-52',
    'Junkers F': 'Junkers F-13',
    'Junkers G': 'Junkers G-31',
    'Messerschmitt M': 'Messerschmitt M-20',
    'Catalina Flying Boat': 'Consolidated PBY',
    'Short Sandringham': 'Short Sandringham',
    'Sikorsky S': 'Sikorsky S-43',
    'Consolidated PBY': 'Consolidated PBY',
    'DC': 'Douglas DC-3',  
    'PA': 'Piper PA-31',   
    'VC': 'Vickers Viking', 
    }
    df['Aircraft'] = df['Aircraft'].replace(aircraft_corrections)

    non_valid_entries = ['??', 'Pepa  -', 'Pindi-Khut  -', 'Taipei -', 'Near ', 'Off ', '?', '-']
    df['Location'] = df['Location'].replace(non_valid_entries, 'Not Specified')

    df['Operator'] = df['Operator'].fillna('Not Specify')

    spelling_corrections = {
        'Aeroflot': 'Aeroflot',
        'USSRAeroflot': 'Aeroflot USSR',
        'Airways World American Pan': 'Pan American World Airways',
        'Airways American Pan': 'Pan American Airways',
        'Airways Grace American Pan': 'Pan American Grace Airways',
        'Lufthansa Deutsche': 'Deutsche Lufthansa',
        'Airways Overseas British': 'British Overseas Airways Corporation',
        'Airways European British': 'British European Airways',
        'Airways British': 'British Airways',
        'Force Air U.S. - Military': 'U.S. Air Force',
        'Army U.S. - Military': 'U.S. Army',
        'Navy U.S. - Military': 'U.S. Navy',
        'Force Air Royal - Military': 'Royal Air Force',
        'Service Mail Aerial US': 'U.S. Aerial Mail Service',
        'Lines Air United': 'United Air Lines',
        'Lines Air Eastern': 'Eastern Air Lines',
        'Lines Air Delta': 'Delta Air Lines',
        'Airlines American': 'American Airlines',
        'Airlines Continental': 'Continental Airlines',
        'Airlines Korean': 'Korean Air',
        'Airlines China': 'China Airlines',
        'Force Air Republican Afghan - Military': 'Afghan Republican Air Force',
        'Corporation Aviation National China': 'China National Aviation Corporation',
        'Airways Dutch Royal KLM': 'KLM Royal Dutch Airlines',
        'Airlines Dutch Royal KLM': 'KLM Royal Dutch Airlines',
        'Aerolinie Ceskoslovenske': 'Czechoslovak Airlines',
        'Airlines Hungarian Malev': 'Malev Hungarian Airlines',
        'Airlines Polish Lot': 'LOT Polish Airlines',
        'Force Air Soviet - Military': 'Soviet Air Force',
        'Force Air Russian - Military': 'Russian Air Force',
        'Aviacion de Cubana': 'Cubana de Aviación',
        'Airlines International Pakistan': 'Pakistan International Airlines',
        'Corporation Aviation National': 'China National Aviation Corporation',
        'Swissair': 'Swissair',
        'Alitalia': 'Alitalia',
        'Air France': 'Air France',
        'France Air': 'Air France'
    }
    df['Operator'] = df['Operator'].replace(spelling_corrections)

    military_standardizations = {
        'Force Air U.S. Army - Military': 'U.S. Army Air Forces',
        'Forces Air Army U.S. - Military': 'U.S. Army Air Forces',
        'Corps Marine U.S. - Military': 'U.S. Marine Corps',
        'Corps Marine U.S. - VietnamMilitary': 'U.S. Marine Corps',
        'Army U.S. - VietnamMilitary': 'U.S. Army',
        'Force Air U.S. - VietnamMilitary': 'U.S. Air Force',
        'Force Air U.S. - GermanyMilitary': 'U.S. Air Force',
        'Force Air U.S. - PakistanMilitary': 'U.S. Air Force',
        'Force Air U.S. - VirginiaMilitary': 'U.S. Air Force',
        'Force Air U.S. - KoreaMilitary': 'U.S. Air Force',
        'Force Air U.S. - DekotaMilitary': 'U.S. Air Force',
        'Force Air U.S. - JerseyMilitary': 'U.S. Air Force',
        'Force Air U.S. - MexicoMilitary': 'U.S. Air Force',
        'Force Air U.S. - RicoMilitary': 'U.S. Air Force',
        'Navy States United - Military': 'U.S. Navy',
        'Navy US  - Military': 'U.S. Navy',
        'Navy U.S. - KoreaMilitary': 'U.S. Navy',
        'Navy U.S. - VietnamMilitary': 'U.S. Navy',
        'Navy U.S. - IslandsMilitary': 'U.S. Navy',
        'Navy U.S. - JerseyMilitary': 'U.S. Navy',
        'Navy German - Military': 'German Navy',
        'Navy German - SeaMilitary': 'German Navy',
        'Navy British Royal - Military': 'Royal Navy',
        'Force Air Canadian Royal - Military': 'Royal Canadian Air Force',
        'Force Air Royal - LankaMilitary': 'Sri Lankan Air Force',
        'Force Air Lanka Sri - LankaMilitary': 'Sri Lankan Air Force'
    }
    df['Operator'] = df['Operator'].replace(military_standardizations)

    df['Fatality_Rate'] = (df['Fatalities (air)'] / df['Aboard']) * 100
    df['Decade'] = (df['Year'] // 10) * 10
    df['Severity_Level'] = df['Fatality_Rate'].apply(lambda x: 
    'Minor' if x == 0 else 
    'Major' if x < 50 else 
    'Catastrophic' if x < 100 else 
    'Total Loss' if x == 100 else 'Not Specified')

    st.title("Aviation Accidents Historical Analysis Dashboard")
    st.write(df)
    return df

try:
    df = load_data()

    st.sidebar.header("Filter options")

    selected_countries = st.sidebar.multiselect(
        "Select Country",
        options=df["Country"].unique(),
        default=df["Country"].unique()
    )

    selected_continents = st.sidebar.multiselect(
        "Select Continent",
        options=df["Continent"].unique(),
        default=df["Continent"].unique()
    )

    selected_category = st.sidebar.multiselect(
        "Select Manufacturer Category",
        options=df["Manufacturer_Category"].unique(),
        default=df["Manufacturer_Category"].unique()
    )

    month_order= ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "December"]
    selected_months = st.sidebar.multiselect(
        "Select Month",
        options=month_order,
        default=month_order
    )

    Severity_order = ["Minor", "Major", "Catastrophic", "Total Loss"]
    selected_severity = st.sidebar.selectbox(
        "Select Severity Level",
        options= ["All"] + Severity_order,
        index=0
    )

    unique_decades = sorted(df['Decade'].unique())
    decades_range = st.sidebar.slider(
        'Select Decade Range',
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

    st.header("2. What Is The Average Fatality Rate By Aircraft Type?")
    q2 = filtered_df.groupby('Aircraft')['Fatality_Rate'].mean().sort_values(ascending=False).head(20)
    st.write(q2)
    q2_df = q2.reset_index()
    chart2 = alt.Chart(q2_df).mark_bar().encode(
        y=alt.Y("Aircraft:N", sort='-x', title="Aircraft Model"),
        x=alt.X("Fatality_Rate:Q", title="Average Fatality Rate (%)"),
        color=alt.Color("Fatality_Rate:Q", scale=alt.Scale(scheme="redpurple")),
        tooltip=["Aircraft", alt.Tooltip("Fatality_Rate:Q", format=".2f")]
    ).properties(
        title="Top 20 Aircraft Models By Average Fatality Rate"
    )
    st.altair_chart(chart2, use_container_width=True)

    st.header("3. How Do Crash Numbers Vary By Season Across Decades?")
    filtered_df['Season'] = filtered_df['Month'].apply(lambda m: 
        'Winter' if m in [12, 1, 2] else 
        'Spring' if m in [3, 4, 5] else 
        'Summer' if m in [6, 7, 8] else 'Fall')
    q3 = filtered_df.groupby(['Decade', 'Season']).size().reset_index(name='Count')
    st.write(q3)
    chart3 = alt.Chart(q3).mark_line(point=True).encode(
        x=alt.X('Decade:O', title='Decade'),
        y=alt.Y('Count:Q', title='Number of Crashes'),
        color=alt.Color('Season:N', title='Season'),
        tooltip=['Decade', 'Season', 'Count']
    ).properties(
        title='Seasonal Crash Patterns Across Decades'
    )
    st.altair_chart(chart3, use_container_width=True)

    st.header("4. Which Operators Have The Highest Number of Incidents?")
    q4 = filtered_df.groupby('Operator').size().sort_values(ascending=False).head(15)
    st.write(q4)
    q4_df = q4.reset_index(name='Incidents')
    chart4 = alt.Chart(q4_df).mark_bar(color='steelblue').encode(
        x=alt.X("Incidents:Q", title="Number of Incidents"),
        y=alt.Y("Operator:N", sort='-x', title="Operator"),
        tooltip=["Operator", "Incidents"]
    ).properties(
        title="Top 15 Operators By Incident Count"
    )
    st.altair_chart(chart4, use_container_width=True)

    st.header("5. What Is The Relationship Between Passengers Aboard And Survival Rate?")
    filtered_df['Survival_Count'] = filtered_df['Aboard'] - filtered_df['Fatalities (air)']
    filtered_df['Survival_Rate'] = (filtered_df['Survival_Count'] / filtered_df['Aboard']) * 100
    q5 = filtered_df[['Aboard', 'Survival_Rate']].dropna()
    st.write(q5.describe())
    chart5 = alt.Chart(q5).mark_circle(size=60, opacity=0.5).encode(
        x=alt.X('Aboard:Q', title='Passengers Aboard'),
        y=alt.Y('Survival_Rate:Q', title='Survival Rate (%)'),
        color=alt.Color('Survival_Rate:Q', scale=alt.Scale(scheme='viridis')),
        tooltip=['Aboard', alt.Tooltip('Survival_Rate:Q', format='.2f')]
    ).properties(
        title='Passengers Aboard vs Survival Rate'
    )
    st.altair_chart(chart5, use_container_width=True)

    st.header("6. How Has Aviation Safety Improved Over Different Decades?")
    q6 = filtered_df.groupby('Decade').agg({
        'Fatality_Rate': 'mean',
        'Fatalities (air)': 'sum'
    }).reset_index()
    st.write(q6)
    base = alt.Chart(q6).encode(x=alt.X('Decade:O', title='Decade'))
    line1 = base.mark_line(color='red', point=True).encode(
        y=alt.Y('Fatality_Rate:Q', title='Avg Fatality Rate (%)', axis=alt.Axis(titleColor='red'))
    )
    line2 = base.mark_line(color='blue', point=True).encode(
        y=alt.Y('Fatalities (air):Q', title='Total Fatalities', axis=alt.Axis(titleColor='blue'))
    )
    chart6 = alt.layer(line1, line2).resolve_scale(y='independent').properties(
        title='Safety Improvement Analysis: Fatality Rate & Total Deaths By Decade'
    )
    st.altair_chart(chart6, use_container_width=True)

    st.header("7. What Percentage Of Crashes Result In Total Loss By Manufacturer Category?")
    q7 = filtered_df[filtered_df['Severity_Level'] == 'Total Loss'].groupby('Manufacturer_Category').size()
    total_crashes = filtered_df.groupby('Manufacturer_Category').size()
    q7_pct = (q7 / total_crashes * 100).sort_values(ascending=False).reset_index()
    q7_pct.columns = ['Manufacturer_Category', 'Total_Loss_Percentage']
    st.write(q7_pct)
    chart7 = alt.Chart(q7_pct).mark_bar().encode(
        y=alt.Y('Manufacturer_Category:N', sort='-x', title='Manufacturer Category'),
        x=alt.X('Total_Loss_Percentage:Q', title='Total Loss Percentage (%)'),
        color=alt.Color('Total_Loss_Percentage:Q', scale=alt.Scale(scheme='reds')),
        tooltip=['Manufacturer_Category', alt.Tooltip('Total_Loss_Percentage:Q', format='.2f')]
    ).properties(
        title='Total Loss Rate By Manufacturer Category'
    )
    st.altair_chart(chart7, use_container_width=True)

    st.header("8. How Many Ground Casualties Occur Relative To Crash Frequency By Continent?")
    q8 = filtered_df.groupby('Continent').agg({
        'Ground': 'sum',
        'Continent': 'count'
    }).rename(columns={'Continent': 'Crash_Count'})
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
