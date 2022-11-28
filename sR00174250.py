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


def Task1():
    first_query = df['director_name'] == df['actor_1_name']
    first_imdb = df[first_query][['imdb_score']].dropna()
    first_mean = first_imdb.mean()

    second_query = df['director_name'] == df['actor_2_name']
    second_imdb = df[second_query][['imdb_score']].dropna()
    second_mean = second_imdb.mean()

    third_query = df['director_name'] == df['actor_3_name']
    third_imdb = df[third_query][['imdb_score']].dropna()
    third_mean = third_imdb.mean()

    null_query = (df['director_name'] != df['actor_1_name']) & (df['director_name'] != df['actor_2_name']) & (df['director_name'] != df['actor_3_name'])
    null_imdb = df[null_query][['imdb_score']].dropna()
    null_mean = null_imdb.mean()

    # Bar chart to compare values
    bar_width = 0.25
    x = ["first", "second", "third", "null"]
    y = [first_mean, second_mean, third_mean, null_mean]
    plt.legend('Imdb Mean')
    plt.xlabel('Mean Type')
    plt.ylabel('Mean')
    plt.bar(x, y, bar_width, color='b')
    plt.show()


Task1()


def Task2():
    # Cleaning data using str.replace to change to unique value
    df['Type'] = df['Type'].str.replace(' Black and white', 'Black and White')
    df['Type'] = df['Type'].str.replace('Black white', 'Black and White')
    df['Type'] = df['Type'].str.replace(' Black and White', 'Black and White')
    df['Type'] = df['Type'].str.replace(' Black And white', 'Black and White')
    df['Type'] = df['Type'].str.replace(' Black and White', 'Black and White')
    df['Type'] = df['Type'].str.replace(' Blackand White', 'Black and White')
    df['Type'] = df['Type'].str.replace('Black Wite', 'Black and White')
    df['Type'] = df['Type'].str.replace('Black white', 'Black and White')
    df['Type'] = df['Type'].str.replace('Black and Whitee', 'Black and White')
    df['Type'] = df['Type'].str.replace(' Black and Whitee', 'Black and White')
    df['Type'] = df['Type'].str.replace(' Blackand white', 'Black and White')
    df['Type'] = df['Type'].str.replace(' Black Wite', 'Black and White')
    df['Type'] = df['Type'].str.replace(' Black and Wite', 'Black and White')
    df['Type'] = df['Type'].str.replace(' Black White', 'Black and White')
    df['Type'] = df['Type'].str.replace(' Black and Whit', 'Black and White')
    df['Type'] = df['Type'].str.replace(' Black andWhite', 'Black and White')
    df['Type'] = df['Type'].str.replace('Black White', 'Black and White')
    df['Type'] = df['Type'].str.replace(' Black And White', 'Black and White')
    # dropping null values
    df['Type'] = df['Type'].dropna()

    # use to check unique values
    print(df['Type'].unique())

    # pulling black and white, counting black and white movies
    black_white = df[df['Type'].str.strip() == 'Black and White'][['Type']]
    black_count = black_white.count()

    # pulling color, counting color movies
    color = df[df['Type'].str.strip() == 'Color'][['Type']]
    color_count = color.count()

    # Bar chart to compare values
    bar_width = 0.45
    movies = ["Color", "Black & White"]
    y = [int(color_count), int(black_count)]
    plt.legend(['Black & White Vs Movies in Color'])
    plt.xlabel('Movie Type')
    plt.ylabel('No. of Movies')
    plt.bar(movies, y, bar_width, color='b')
    # Color movies a lot more present than black & white movies
    plt.show()


Task2()
# def Task3():
#     genres = df['genres'].str.str
#     print(genres)
#
#
#
# Task3()
# def Task4():
#
#
#
#
#
#
#
# def Task5():
#     # find median
#     c = df['budget'].median()
#
#     # put median in null cells
#     df['budget'] = df['budget'].fillna(c)
#
#     # above and below median subgroups
#     sub1 = df[df['budget'] < c][['budget']]
#
#     sub2 = df[df['budget'] > c][['budget']]
#
#     a = sub1.median()
#     b = sub2.median()
#
#     print(a)
#     print(b)
#
#
#
# Task5()
