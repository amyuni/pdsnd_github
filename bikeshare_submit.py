import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all','january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def preview():
    preview = input("\nHi!\nWould you like to preview the first 5 rows of US bikeshare raw data? Enter yes or no.\n").lower()
    
    while preview:
        if preview == 'yes':
            city = input("\nEnter city to explore (chicago, new york city, washington): ").lower()
            while city not in (CITY_DATA.keys()):
                city = input("Invalid input.\nKindly select one of these cities (chicago / new york city / washington): ").lower()
            df = pd.read_csv(CITY_DATA[city])
            print(df[:][:5])
            preview = input("Would you like to preview the another city? Enter yes or no.\n").lower()
            continue
        elif preview == 'no':
            break
        else:
            preview = input("Invalid input. Enter yes or no.\n").lower()

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('-'*40)
    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = input("\n\nSelect a city (chicago / new york city / washington)\nEnter choosen city: ").lower()
    while city not in (CITY_DATA.keys()):
            city = input("Invalid input.\nKindly select one of these cities (chicago / new york city / washington): ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("\nSelect a month (all / january / february / etc.)\nEnter choosen month: ").lower()
    while month not in months:
        month = input("Invalid input.\nKindly select a valid month (all / january / february / etc.): ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\nSelect a day of week (all / monday / tuesday / etc.)\nEnter choosen day of week : ").lower()
    while day not in day:
        day = input("Invalid input.\nKindly select a valid day of week (all / monday / tuesday / etc.): ").lower()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month)

        # filter by month to create the new dataframe
        df = df.query('month == @month')

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.query('day_of_week == @day.title()')
       
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month_index = df['month'].mode()[0]
    print("Most Common Month: {}".format(months[common_month_index].title()))


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("Most Common Day of Week: {}".format(common_day))


    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End Station'] = df['Start Station'] + " - " + df['End Station']
    freq_station_combi = df['Start-End Station'].mode()[0]
    print('Most Frequent Start - End Station Combination:', freq_station_combi)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Travel Time'] = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])
    tot_travel_time = df['Travel Time'].sum()
    print("Total Travel Time: {}".format(tot_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Travel Time'].mean()
    print("Mean Travel Time: {}".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print("User Count:\n{}\n".format(user_count))
    
    while True: 
        try:
            # TO DO: Display counts of gender
            gender_count = df['Gender'].value_counts()
            print("Gender Count:\n{}\n".format(gender_count))
            break
        except:
            print("Raw data does not include 'Gender' column.")
            break
        
    while True:
        try:
            # TO DO: Display earliest, most recent, and most common year of birth
            # earliest birth year
            earliest_birth_yr = int(df['Birth Year'].min())
            print("Earliest Birth Year: {}".format(earliest_birth_yr))
            # most recent birth year
            recent_birth_yr = int(df['Birth Year'].max())
            print("Recent Birth Year: {}".format(recent_birth_yr))
            # most common birth year
            common_birth_yr = int(df['Birth Year'].mode()[0])
            print("Most Common Birth Year: {}".format(common_birth_yr))
            break
        except:
            print("Raw data does not include 'Birth Year' column.")
            break


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        preview()
        
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
