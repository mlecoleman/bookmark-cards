import pandas as pd
# Command for Jupyter notebook
# !pip install matplotlib
import matplotlib.pyplot as plt

# Name columns since columns in CSV aren't named
col_names = ['category',
             'subcategory',
             'url',
             'name',
             'tagline',
             'description']

# Read in CSV file of bookmarks
bookmarks = pd.read_csv('bookmarks.csv', names=col_names)

# Remove these columns because they are incomplete
bookmarks.pop('category')
bookmarks.pop('subcategory')

# Search for rows based on certain key-words, would be useful if I'm looking for a specific resource
bicycle = bookmarks[bookmarks['description'].str.lower().str.contains('bicycle')]
louisville = bookmarks[bookmarks['description'].str.lower().str.contains('louisville')]
print(bicycle)
print(louisville)

# Total number of bookmarks for reference
length = len(bookmarks)

# Look to see how many rows contain a certain key word in their description column
bike = bookmarks['description'].str.contains('bike').sum()
plant = bookmarks['description'].str.contains('plant').sum()
louisville = bookmarks['description'].str.contains('louisville').sum()

print(bike)
print(plant)
print(louisville)


# Create a bar graph to display the number of bookmarks with certain keywords in their descriptions.
key_words={'bike':[13],
           'plant':[8],
           'louisville':[6]}

dataframe=pd.DataFrame(key_words)

dataframe.plot(kind='bar')

plt.suptitle('Number of Bookmark Descriptions that Contain a Given Keyword')
plt.xlabel('Keywords')
plt.ylabel('Number of Bookmarks with Keywords in Description')




