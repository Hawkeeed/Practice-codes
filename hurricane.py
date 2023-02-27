# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}


# test function by updating damages

def convert_damages(list):
    conversion = {"M": 1000000,
                  "B": 1000000000}
    updated_damages = []
    for i in damages:
        if i == "Damages not recorded":
            updated_damages.append(i)
        elif i[-1] == "M":
            i=i.strip("M")
            i=float(i)
            updated_damages.append(i*conversion["M"])
        else:
            i=i.strip("B")
            i=float(i)
            updated_damages.append(i*conversion["B"])
    return updated_damages


#print(convert_damages(damages))


# 2
# Create a Table
def huracanes(names, months, years, max_sustained_winds, areas_affected,deaths, damages):
    hurracanes={}
    cuenta=0

    for i in range(len(names)):
        hurracanes[names[i]]={"Name":names[i],
                    "Month":months[i],
                    "Years":years[i],
                    "Max_sustined_winds":max_sustained_winds[i],
                    "Areas_affected":areas_affected[i],
                    "Deaths":deaths[i],
                    "Damages":damages[i]}

    return hurracanes

total_huracanes=(huracanes(names,months,years,max_sustained_winds,areas_affected,deaths,convert_damages(damages)))


# Create and view the hurricanes dictionary

# 3
# Organizing by Year
def dic_year(huracanaes):
    hura_year={}
    for i in range(len(years)):
        hura_year[years[i]]={"Name":names[i],
                    "Month":months[i],
                    "Years":years[i],
                    "Max_sustined_winds":max_sustained_winds[i],
                    "Areas_affected":areas_affected[i],
                    "Deaths":deaths[i],
                    "Damages":damages[i]}


    return hura_year

total_year_huracanaes=dic_year((names,months,years,max_sustained_winds,areas_affected,deaths,convert_damages(damages)))


# create a new dictionary of hurricanes with year and key


# 4
# Counting Damaged Areas
def total_areas(diccionario):
    areas_count = {}

    for area in total_huracanes:
        for affected in total_huracanes[area]["Areas_affected"]:
            if affected not in areas_count:
                areas_count[affected]=1
            else:
                areas_count[affected]+=1
    return areas_count
print(total_areas(total_huracanes))


# create dictionary of areas to store the number of hurricanes involved in
def max_deaths(dic):
    most_lethal=""
    total_deaths=0
    for huracane in total_huracanes:
        if total_huracanes[huracane]["Deaths"]>total_deaths:
            most_lethal=huracane
            total_deaths=total_huracanes[huracane]["Deaths"]
    return total_deaths, most_lethal

total_deaths, most_lethal=max_deaths(total_huracanes)
#print(f"{most_lethal} {total_deaths}")


# 5
# Calculating Maximum Hurricane Count
def mortality(hurricanes):
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}
    hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: []}
    for hurracane in total_huracanes:
        num_deaths=total_huracanes[hurracane]["Deaths"]
        if num_deaths==0:
            hurricanes_by_mortality[0].append(total_huracanes[hurracane])
        elif num_deaths >mortality_scale[0] and num_deaths < mortality_scale[1]:
            hurricanes_by_mortality[1].append(total_huracanes[hurracane])
        elif num_deaths>mortality_scale[1] and num_deaths <mortality_scale[2]:
            hurricanes_by_mortality[2].append(total_huracanes[hurracane])
        elif num_deaths>mortality_scale[2] and num_deaths< mortality_scale[3]:
            hurricanes_by_mortality[3].append(total_huracanes[hurracane])
        else:
            hurricanes_by_mortality[4].append(total_huracanes[hurracane])

    return hurricanes_by_mortality

#print(mortality(total_huracanes))



# find most frequently affected area and the number of hurricanes involved in
def most_damage(list):
    most_destruc=""
    total_damage=0
    for hurricane in total_huracanes:
        if total_huracanes[hurricane]["Damages"]=="Damages not recorded":
            pass
        elif total_huracanes[hurricane]["Damages"]>total_damage:
            most_destruc=hurricane
            total_damage=total_huracanes[hurricane]["Damages"]
    return most_destruc, total_damage

most_destruc,total_damage=most_damage(total_huracanes)
print(f"the most destructive hurricane is {most_destruc} with total damages : {total_damage}")


# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths

# 7
# Rating Hurricanes by Mortality


# categorize hurricanes in new dictionary with mortality severity as key


# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost


# 9
# Rating Hurricanes by Damage
def total_damage(list):

    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}
    hurricanes_by_damages = {0: [], 1: [], 2: [], 3: [], 4: []}
    for hurricane in total_huracanes:
        count_damages=total_huracanes[hurricane]["Damages"]
        if total_huracanes[hurricane]["Damages"]=="Damages not recorded":
            hurricanes_by_damages[0].append(total_huracanes[hurricane])
        elif count_damages>damage_scale[0] and count_damages< damage_scale[1]:
            hurricanes_by_damages[1].append(total_huracanes[hurricane])
        elif count_damages>damage_scale[1] and count_damages< damage_scale[2]:
            hurricanes_by_damages[2].append(total_huracanes[hurricane])
        elif count_damages>damage_scale[2] and count_damages<damage_scale[3]:
            hurricanes_by_damages[3].append(total_huracanes[hurricane])
        else:
            hurricanes_by_damages[4].append(total_huracanes[hurricane])
    return hurricanes_by_damages

print(total_damage(total_huracanes))





# categorize hurricanes in new dictionary with damage severity as key
