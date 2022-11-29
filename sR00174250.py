# -*- coding: utf-8 -*-
"""
Created on 9th November 2022

@Student Name: Oisín Flynn
@Student id: R00174250
@Cohort: SD3
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("movie_metadata.csv", encoding="ISO-8859-1")


# def Task1():
#     first_query = df['director_name'] == df['actor_1_name']
#     first_imdb = df[first_query][['imdb_score']].dropna()
#     first_mean = first_imdb.mean()
#
#     second_query = df['director_name'] == df['actor_2_name']
#     second_imdb = df[second_query][['imdb_score']].dropna()
#     second_mean = second_imdb.mean()
#
#     third_query = df['director_name'] == df['actor_3_name']
#     third_imdb = df[third_query][['imdb_score']].dropna()
#     third_mean = third_imdb.mean()
#
#     null_query = (df['director_name'] != df['actor_1_name']) & (df['director_name'] != df['actor_2_name']) & (df['director_name'] != df['actor_3_name'])
#     null_imdb = df[null_query][['imdb_score']].dropna()
#     null_mean = null_imdb.mean()
#
#     # Bar chart to compare values
#     bar_width = 0.25
#     mean_labels = ["First", "Second", "Third", "Null"]
#     means = [int(first_mean), int(second_mean), int(third_mean), int(null_mean)]
#     plt.title('Average Imdb Scores')
#     plt.xlabel('Director as Actor')
#     plt.ylabel('Imdb Mean No.')
#     plt.bar(mean_labels, means, bar_width, color='b')
#     # first, second actor/directors & null relatively similar means with third being the lowest
#     # meaning if director is third actor movie won't be as critically acclaimed
#     plt.show()
#
#
# Task1()


# def Task2():
#     # Cleaning data using str.replace to change to unique value
#     df['Type'] = df['Type'].str.replace(' Black and white', 'Black and White')
#     df['Type'] = df['Type'].str.replace('Black white', 'Black and White')
#     df['Type'] = df['Type'].str.replace(' Black and White', 'Black and White')
#     df['Type'] = df['Type'].str.replace(' Black And white', 'Black and White')
#     df['Type'] = df['Type'].str.replace(' Black and White', 'Black and White')
#     df['Type'] = df['Type'].str.replace(' Blackand White', 'Black and White')
#     df['Type'] = df['Type'].str.replace('Black Wite', 'Black and White')
#     df['Type'] = df['Type'].str.replace('Black white', 'Black and White')
#     df['Type'] = df['Type'].str.replace('Black and Whitee', 'Black and White')
#     df['Type'] = df['Type'].str.replace(' Black and Whitee', 'Black and White')
#     df['Type'] = df['Type'].str.replace(' Blackand white', 'Black and White')
#     df['Type'] = df['Type'].str.replace(' Black Wite', 'Black and White')
#     df['Type'] = df['Type'].str.replace(' Black and Wite', 'Black and White')
#     df['Type'] = df['Type'].str.replace(' Black White', 'Black and White')
#     df['Type'] = df['Type'].str.replace(' Black and Whit', 'Black and White')
#     df['Type'] = df['Type'].str.replace(' Black andWhite', 'Black and White')
#     df['Type'] = df['Type'].str.replace('Black White', 'Black and White')
#     df['Type'] = df['Type'].str.replace(' Black And White', 'Black and White')
#     # dropping null values
#     df['Type'] = df['Type'].dropna()
#
#     # use to check unique values
#     print(df['Type'].unique())
#
#     # pulling black and white, counting black and white movies
#     black_white = df[df['Type'].str.strip() == 'Black and White'][['Type']]
#     black_count = black_white.count()
#
#     # pulling color, counting color movies
#     color = df[df['Type'].str.strip() == 'Color'][['Type']]
#     color_count = color.count()
#
#     # Bar chart to compare values
#     bar_width = 0.45
#     movie_color = ["Black & White", "Color"]
#     color_comparison = [int(black_count), int(color_count)]
#     plt.title('Black & White Vs Movies in Color')
#     plt.xlabel('Movie Type')
#     plt.ylabel('No. of Movies')
#     plt.bar(movie_color, color_comparison, bar_width, color='b')
#     # Color movies a lot more present than black & white movies
#     plt.show()
#
#
#
# Task2()

# def Task3():
#     genres = df['genres'].str.split('|')
#     genres = genres.explode('genres')
#     # unique genres
#     unique = genres.unique()
#     genres = genres.value_counts()
#     # 5 most popular genres
#     genres = genres.nlargest(5)
#
#     # Bar chart to compare genres
#     bar_width = 0.45
#     genre_labels = ["Drama", "Comedy", "Thriller", "Action", "Romance"]
#     genre_total = [genres[0], genres[1], genres[2], genres[3], genres[4]]
#     plt.title('5 Most Popular Genres')
#     plt.xlabel('Genre')
#     plt.ylabel('No. of Genres')
#     plt.bar(genre_labels, genre_total, bar_width, color='b')
#     # Assuming were showing 5 most popular genres
#     plt.show()
#
#
# Task3()
# def Task4():
#     movie_length = df['length'].dropna()
#     movie_length = movie_length[pd.to_numeric(df['length'], errors='coerce').notnull()]
#     min = movie_length.min()
#     max = movie_length.max()
#     median = movie_length.median()
#     first_quartile = movie_length.quantile(0.25)
#     third_quartile = movie_length.quantile(0.75)
#     # movie_length = movie_length.describe()
#
#     # part b
#     df1 = pd.Series([min, max, median, first_quartile, third_quartile])
#     dict = {'b': df1}
#     dfb = pd.DataFrame(dict)
#     dfb.boxplot()
#     plt.show()
#
#     # TODO part c
#
#
#
#
# Task4()
def Task5():
    # find median
    c = df['budget'].median()

    # put median in null cells
    df['budget'] = df['budget'].fillna(c)

    # above and below median subgroups
    sub1 = df[df['budget'] < c][['budget']]

    sub2 = df[df['budget'] > c][['budget']]

    a = sub1.median()
    b = sub2.median()

    # TODO fix histogram
    dfh = pd.DataFrame(a, b, columns=['a', 'b'])
    dfh.hist()
    plt.title("Target Budget")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()



Task5()
