import time
import pandas as pd
import numpy as np
import datetime
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
   
                    
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    def get_city():
        city = ''
        while city not in ['chicago', 'new york', 'washington']:
            city = input('\nWould you like to see data for Chicago, New York, or'
                         ' Washington?\n').lower()
            if city == 'chicago':
                return 'chicago.csv'
            elif city == 'new york':
                return 'new_york_city.csv'
            elif city == 'washington':
                return 'washington.csv'
            else:
                print('Sorry, I do not understand your input. Please choose from '
                      'Chicago, New York, or Washington.')
    
    # TO DO: get user input for month (all, january, february, ... , june)
    def get_month():
        month = input('\nWhich month? January, February, March, April, May, June, or "all" to apply no month filter?\n').lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            return month
        else:
            print('\nI\'m sorry, I\'m not sure which month you\'re trying to filter by. Let\'s try again.\n')
        #month = ''
        #while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
            #month = input('\nWhich month? January, February, March, April, May, June, or "all" to apply no month filter?\n').lower()
            #if month == 'january':
               #return 'january'
            #elif month == 'february':
                #return 'february'
            #elif month == 'march':
                #return 'march'
            #elif month == 'april':
                #return 'april'
            #elif month == 'may':
                #return 'may'
            #elif month == 'june':
                #return 'june'
            #elif month == 'all':
                #return 'all'
            #else:
                #print('\nI\'m sorry, I\'m not sure which month you\'re trying to filter by. Let\'s try again.\n')
           
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    def get_day():    
        day = ''
        while day not in ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
            day = input('\nWhich day? Please type your response as an integer(e.g., 1=Sunday) or "all" to apply no day filter\n')
            if day == '1':
                return 'Sunday'
            elif day == '2':
                return 'Monday'
            elif day == '3':
                return 'Tuesday'
            elif day == '4':
                return 'Wednesday'
            elif day == '5':
                return 'Thursday'
            elif day == '6':
                return 'Friday'
            elif day == '7':
                return 'Saturday'
            elif day == 'all':
                return 'all'
            else:
                print('\nI\'m sorry, I\'m not sure which month you\'re trying to filter by. Let\'s try again.\n')
                
     
    
    print('-'*40)
    return get_city(), get_month(), get_day()

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
    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df

    """
    Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more.
    Continues asking until they say stop.
    """

def display_data(df):
    pd.set_option('expand_frame_repr', False)
    pd.set_option('display.max_columns', 999)
    display = ''
    head = 0
    tail = 5
    while display not in ['y', 'n']:
        display = input('\nWould you like to view individual trip data? Enter "Y" for Yes or "N" for No.\n').lower()
        if display == 'y':
            print(df[df.columns[0:-1]].iloc[head:tail])
            display_more = ''
            while display == 'y':
                display_more = input('\nWould you like to view additional individual trip data? Enter "Y" for Yes or "N" for No.\n').lower()
                if display_more == 'y':
                    head += 5
                    tail += 5
                    print(df[df.columns[0:-1]].iloc[head:tail])
                else:
                    break
        else:
            break
        

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('Most common month:', calendar.month_name[common_month])
    
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    common_day = df['day'].mode()[0]

    print('Most common day:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    common_start_station = df.groupby('Start Station')['Start Station'].size().sort_values(ascending=False).index[0]
    print('Most Common Start Station:', common_start_station)


    # TO DO: display most commonly used end station
    df['End Time'] = pd.to_datetime(df['End Time'])

    common_end_station = df.groupby('End Station')['End Station'].size().sort_values(ascending=False).index[0]
    print('Most Common End Station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_trip_start = df.groupby(['Start Station', 'End Station'])['Start Time'].size().sort_values(ascending=False).index[0][0]
    common_trip_end = df.groupby(['Start Station', 'End Station'])['Start Time'].size().sort_values(ascending=False).index[0][1]
    
    print('Most common trip combination was:' + '\n-From Start Station:', common_trip_start + '\n-To End Station:', common_trip_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_trip_duration, 60)
    hour, minute = divmod(minute, 60)
    print('The total trip duration: {} hours, {} minutes and {} seconds.'.format(hour, minute, second))
    
    # TO DO: display mean travel time
    avg_trip_duration = int(df['Trip Duration'].mean())
    minute, second = divmod(avg_trip_duration, 60)
    if minute > 60:
        hour, minute = divmod(minute, 60)
        print('The average trip duration: {} hours, {} minutes and {} seconds.'.format(hour, minute, second))
    else:
        print('The average trip duration: {} minutes and {} seconds.'.format(minute, second))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def get_user(df):
    start_time = time.time()
    
    def user_stats(df):
        """Displays statistics on bikeshare users."""
    
        print('\nCalculating User Stats...\n')
     
        # TO DO: Display counts of user types
        user_types = df['User Type'].value_counts()
        print('\nCount of User Types:\n', user_types)
    
        # TO DO: Display counts of gender
    def gender_counts(df):
        try:
            gender_counts = df['Gender'].value_counts()
            print('\nCount of Gender:\n', gender_counts)
        except:
            print('There is no gender data available.')
    
        # TO DO: Display earliest, most recent, and most common year of birth
    def birth_years(df):
        try:
            earliest_birth_year = df['Birth Year'].min()
            earliest_birth_year = str(int(df['Birth Year'].min()))
            common_birth_year = str(int(df['Birth Year'].mode()))
            recent_birth_year = str(int(df['Birth Year'].max()))
            print('Earliest Birth Year:', earliest_birth_year)  
            print('Most Common Birth Year:', common_birth_year)
            print('Most Recent Birth Year:', recent_birth_year)
        except:
            print('There is no birth year data available.')
    
    
    user_stats(df), gender_counts(df), birth_years(df)
    return (time.time() - start_time)
    
    


def main():
    while True:
        city, month, day = get_filters()
                       
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        time_get = get_user(df)
        
        print("\nThis took %s seconds." % time_get)
        print('-'*40)
                         
        
            
        restart = input('\nWould you like to restart? Enter "Y" for Yes or "N" for No.\n')
        if restart.lower() != 'y':
            print('\n\n\n')
            break

if __name__ == "__main__":
	main()
