# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 14:11:57 2020

@author: michale_nath
"""
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df = pd.read_csv("export_dataframe (1).csv")

st.title('MLB Pitcher Salary Regression: Analysis of Variables')

st.sidebar.markdown('The data in this data frame was used to perform an OLS regression analysis to determine'
                    'which factors were statistically significant in predicting the salary of an MLB pitcher.'
                    'Using the selection box below, you can view the scatter plots of te relationship between'
                    'each of the statistics and natural log of salary. You will also be able to see the distribution'
                    'of the independent variable in a histogram. Please select a statistic below.')

option = st.sidebar.selectbox('Which statistic would you like to view the scatter plot of to examine the relationship '
                              'with the natural log of salary. You will also be able to view the histogram of the '
                              'distribution of this variable',
('Ln 2019 Salary', 'Age', 'W-L%', 'ERA', 'IP', 'H9', 'HR9', 'BB9', 'SO9'))

fig, ax = plt.subplots()
ax.scatter(df[[option]], df[['Ln 2019 Salary']])
ax.set_xlabel(option)
ax.set_ylabel('Ln 2019 Salary')
ax.set_title(f'Scatterplot of the Relationship Between {option} and LN 2019 Salary')
plt.show()
st.pyplot(fig)

fig, ax = plt.subplots()
ax.hist(df[option], bins=15)
ax.set_xlabel(option)
ax.set_ylabel('Frequency')
ax.set_title(f'Histogram of {option}')
plt.show()
st.pyplot(fig)