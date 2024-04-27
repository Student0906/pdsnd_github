#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks the user to specify a city, month, and day to analyze.

    Returns:
        (str) city: Name of the city to analyze.
        (str) month: Name of the month to filter by, or "all" for no month filter.
        (str) day: Name of the day of the week to filter by, or "all" for no day filter.
    """
    print("Hello! Let's explore some US bikeshare data!")

    cities = ['chicago', 'new york city', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

    # Get user input for city (chicago, new york city, washington)
    while True:
        city = input("Please enter one of the following cities: Chicago, New York City, or Washington: ").lower()
        if city in cities:
            break
        else:
            print("City name not valid. Please try again.")

    # Get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter month name or 'all' to see full data: ").lower()
        if month in months:
            break
        else:
            print("Month not valid. Please try again.")

    # Get user input for day of week (all, monday, tuesday, ... , sunday)
    while True:
        day = input("Please enter one of the following days: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or 'all': ").lower()
        if day in days:
            break
        else:
            print("Day not valid. Please try again.")

    print('-' * 40)
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
    # Load data for the specified city

    df = pd.read_csv(CITY_DATA[city])
    
    # Convert 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract the month from 'Start Time' column
    df['month'] = df['Start Time'].dt.month
    
    # Extract the day of the week from 'Start Time' column
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # Filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # Creating new data frame
        df = df[df['month'] == month]

    # Filter by day
    if day != 'all' :
        df = df[df['day_of_week'] == day.title()]    


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
       
    # Count the occurrences of each month
    month_counts = df['month'].value_counts()
    
    # Find the most common month
    most_common_month = month_counts.idxmax()  # This gives you the index (month) with the highest count
    
    # Convert the month number back to month name
    month_name_dict = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }
    most_common_month_name = month_name_dict[most_common_month]
    
    # Display the most common month
    print(f"The most common month is: {most_common_month_name}")
    
    # display the most common day of week
    print(f"The most common day is: ", df['day_of_week'].value_counts().idxmax())

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print(f"The most common hour is: ", df['hour'].value_counts().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most popular start station
    print(f"The most popular start station is: ", df ['Start Station'].value_counts().idxmax())

    # display most popular end station
    print(f"The most popular end station is: ", df['End Station'].value_counts().idxmax())

    # display most frequent combination of start station and end station trip

    # Group by 'Start Station' and 'End Station' and count occurrences
    combination_counts = df.groupby(['Start Station', 'End Station']).size()
    
    # Find the most frequent combination
    most_frequent_combination = combination_counts.idxmax()
    most_frequent_count = combination_counts.max()
    
    # Print the most frequent combination and its count
    print(f"The most frequent combination of start station and end station trip is: "
          f"{most_frequent_combination[0]} to {most_frequent_combination[1]} "
          f"with {most_frequent_count} trips.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time in minutes
    total_travel_time = (df['Trip Duration'].sum())/60    
    print(f"Total travel time in minutes: ", total_travel_time)



    # display mean travel time in minutes
    mean_travel_time = (df['Trip Duration'].mean())/60    
    print(f"Average travel time in minutes: ", mean_travel_time) 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    # Display counts of user types    
    user_type_counts = df['User Type'].value_counts()
    print("Counts of User Types:")
    print(user_type_counts)
    
    
    # Check if the 'Gender' column exists before calculating gender counts
    if 'Gender' in df.columns:
        # Replace blank values in 'Gender' column with 'Unknown'
        df['Gender'] = df['Gender'].fillna('Unknown')
        
        # Display counts of Gender    
        gender_counts = df['Gender'].value_counts()
        print("Counts of Gender:")
        print(gender_counts)
    else:
        print("Gender data not found for this city.")
    

    # Check if the 'Birth Year' column exists before calculating birth year stats
    if 'Birth Year' in df.columns:
        # Calculate the earliest year of birth
        earliest_birth_year = df['Birth Year'].min()
        
        # Calculate the most recent year of birth
        most_recent_birth_year = df['Birth Year'].max()
        
        # Calculate the most common year of birth
        most_common_birth_year = df['Birth Year'].mode()[0]
        
        # Display the results
        print("\nBirth Year statistics:")
        print(f"Earliest year of birth: {earliest_birth_year}")
        print(f"Most recent year of birth: {most_recent_birth_year}")
        print(f"Most common year of birth: {most_common_birth_year}")
    else:
        print("Birth Year data not found for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

    
def display_raw_data(df):
    """
    Iterates through the raw data and prints each line of data one by one.

    Args:
        df: The DataFrame containing the raw data.
    """
    # Start from the first row
    start_row = 0
    
    while True:
        # Prompt the user if they want to see raw data
        user_input = input("\nWould you like to see 5 lines of raw data? Enter 'y for yes' or 'n for no': ").lower()
        
        if user_input != 'y':
            # If the user doesn't want to see raw data, break the loop
            break
        
        # Print 10 lines of raw data
        for index in range(start_row, start_row + 10):
            if index < len(df):
                # Print the line of data at the current index
                print(df.iloc[index])
            else:
                # If there are no more rows, print a message and break the loop
                print("\nNo more raw data to display.")
                return
        
        # Move the start row forward by 5 to display the next set of data in the next iteration
        start_row += 5
   


    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Call the new function to display raw data
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()







