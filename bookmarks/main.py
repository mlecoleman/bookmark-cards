import pandas as pd

col_names = ['Category',
             'Subcategory',
             'URL',
             'Company Name',
             'Tag Line',
             'Description']

bookmarks = pd.read_csv('bookmarks.csv', names=col_names)

bookmarks.pop('Category')
bookmarks.pop('Subcategory')

print(bookmarks.head())
