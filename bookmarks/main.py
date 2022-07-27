import pandas as pd

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


# Look to see how many rows contain a certain key word in their description column
bike = bookmarks['description'].str.contains('bike').sum()
plant = bookmarks['description'].str.contains('plant').sum()
louisville = bookmarks['description'].str.contains('louisville').sum()

# Search for rows based on certain key-words, would be useful if I'm looking for a specific resource
bicycle = bookmarks[bookmarks['description'].str.lower().str.contains('bicycle')]
louisville = bookmarks[bookmarks['description'].str.lower().str.contains('louisville')]

# Total number of bookmarks for reference
length = len(bookmarks)

# filtered_row = bookmarks[ bookmarks["description"]("bike")]
print(bike)
print(plant)
print(louisville)
print(bicycle)
print(length)





