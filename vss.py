# -*- coding: utf-8 -*-
"""

Created on Mon Nov  6 11:43:59 2023

@author: mouli chand
"""

import matplotlib.pyplot as plt
import pandas as pd


def lineplot(screen_time):
    """ Line plot between usage of apps with date"""
    app_bool = screen_time['App'] == 'Instagram'
    instagram_data = screen_time[app_bool]
    Whatsapp_data = screen_time[~app_bool]
    screen_time.head()
    print(screen_time.head())
    plt.plot(instagram_data['Date'],
             instagram_data['Usage'], label='Instagram')
    plt.plot(Whatsapp_data['Date'], Whatsapp_data['Usage'], label='Whatsapp')
    plt.legend()
    plt.xlabel('Dates')
    plt.ylabel('Usage')
    plt.title('Usage of Apps')
    plt.savefig('line_chart.png')
    plt.xticks(rotation=90)
    plt.show()


def barplot(screen_time):
    """ Bar plot for notifications in each app"""
    plt.bar(screen_time['App'], screen_time['Notifications'])
    plt.xlabel('Apps')
    plt.ylabel('Notifications')
    plt.title('Apps Notifications')
    plt.savefig('bar_chart.png')
    plt.show()


def scatterplot(screen_time):
    """ Scatter plot for usage and notifications of each app"""
    plt.scatter(screen_time['Usage'], screen_time['Notifications'], alpha=0.7)
    plt.xlabel('Usage')
    plt.ylabel('Notifications')
    plt.title('Usage and Notifications of Apps')
    plt.savefig('scatter_plot.png')
    plt.show()


screen_time = pd.read_csv('screen time.csv')
lineplot(screen_time)
barplot(screen_time)
scatterplot(screen_time)
