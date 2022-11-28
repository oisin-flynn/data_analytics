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
#     first_director = df[first_query][['actor_1_name', 'director_name']].dropna()
#     imdb = df['imdb_score'].mean()
#     # df2 = df.groupby('director_name')
#     df2 = df[first_director]['imdb_score'].mean()
#
#
#     second_query = df['director_name'] == df['actor_2_name']
#     second_director = df[second_query][['actor_2_name', 'director_name']].dropna()
#
#     third_query = df['director_name'] == df['actor_3_name']
#     third_director = df[third_query][['actor_3_name', 'director_name']].dropna()
#
#     null_query = (df['director_name'] != df['actor_1_name']) & (df['director_name'] != df['actor_2_name']) & (df['director_name'] != df['actor_3_name'])
#     null_director = df[null_query][['actor_1_name', 'director_name']].dropna()
#     # mean = np.mean(df['imdb_score'])
#     # print(df[first_director & mean])
#     print(df2)
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
#     x = ["Color", "Black & White"]
#     y = [int(color_count), int(black_count)]
#     plt.legend(['Black & White Vs Movies in Color'])
#     plt.xlabel('Movie Type')
#     plt.ylabel('No. of Movies')
#     plt.bar(x, y, bar_width, color='b')
#     # Color movies a lot more present than black & white movies
#     plt.show()
#
#
# Task2()
def Task3():
    genres = df['genres'].split('|')





Task3()
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
