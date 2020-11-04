# import library
import plot_chart as pc

'''
this module/library takes 3 arguments, first two arguments are column names
this two arguments are for ploting x-axis and y-axis third argument is for
key value from google spread sheet in drive
'''

z = '1jbcRvatx1DmtxWWwC7dcEwSyYOAxD0iFICGN33JoUSk'  # this is key from my googledrive sheet

# i know my sheet have 3 columns named as A, B, C
# i like to plot for A and B

pc.plot_chart('A','B',z)
