import numpy as np
import pandas as pd

# url = 'https://raw.githubusercontent.com/FrancescoMariottini/project3/main/inputs/sales_data.csv'
url = './inputs/all_sales_data.csv'
df = pd.read_csv(url)
print(df)
print(df.dtypes)
# # 1- Done... ----------------- property_subtype  ----------------------
# print(df.property_subtype.unique())  # check all distinc data in the row
# # -----if the column exist this text delete that line because that records are abroud
# del_subtype = ['Wohnung', 'Triplexwohnung', 'Sonstige', 'Loft / �tico', 'Loft / Dachgeschoss', 'Loft / Attic','Gewerbe', 'Etagenwohnung', 'Erdgeschoss', 'Attico', 'Appartamento duplex', 'Apartamento', 'Altbauwohnung']
# new_df = df[df['property_subtype'].apply(lambda x: type(x) not in [int, float])]
# new_df = new_df[new_df['property_subtype'].apply(lambda x: "sqft" not in x)]
# new_df = new_df[new_df['property_subtype'].apply(lambda x: x not in del_subtype)]
#
# # 2- Done... ----------------- sale ----------------------
# print(df.sale.unique())  # check all distinc data in the row
# # USE new_df INSTEAD OF df WHEN YOU MERGE PROCESSES ABOVE
# # , na=False solved confusing about float
# new_df = df[~df['sale'].str.contains('annuity', na=False)]
# #

# ------ RULES of CLEANING DataSets ---------
# 1 - Messy Datasets
# 2 - Identify Columns That Contain unnecessary data
# 3 - Delete Columns That Contain unnecessary data
# 4 - Consider Columns That Have Very Few Values
# 5 - Remove Columns That Have A Low Variance
# 6 - Identify Rows that Contain Duplicate Data
# 7 - Delete Rows that Contain Duplicate Data
#   - No duplicates
#   - No blank spaces (ex: " I love python " => "I love python")
#   - No errors
#   - No empty values
# -----droping columns-----
# check distinct data and what to do
# to_drop = ['source',
#            'hyperlink']
# df.drop(to_drop, inplace=True, axis=1)
# print(df)
# print(df.dtypes)
# -----setting new index-----
# if df['anyID'].is_unique:
#     df = df.set_index('anyID')
# -----checking data and repairing-----
# df.loc[1905:, 'Should a be Numeric Column'].head(10)
# regex = r'^(\d{4})'
# extr = df['Should a be Numeric Column'].str.extract(regex, expand=False)
# print(df['Should a be Numeric Column'].dtype) # before
# df['Should a be Numeric Column'] = pd.to_numeric(extr)
# print(df['Should a be Numeric Column'].dtype) #after
# df['Date of Publication'].isnull().sum() / len(df) #to check how much percentage of null records in the column
# np.where(condition, then, else)
# np.where(condition1, x1,
#         np.where(condition2, x2,
#             np.where(condition3, x3, ...)))
# loc = df['locality']
# brussels = loc.str.contains('Brussels')
# anvers = loc.str.contains('Anvers')
# df['locality'] = np.where(brussels, 'Brussels',
#                                       np.where(anvers, 'Anvers',
#                                                loc.str.replace('-', ' ')))
# ----- applymap -----
# list=[]
# state = ''
# with open('Datasets/sample.txt') as file:
#     for line in file:
#         if 'criterion' in line:
#             print()
#             # list.append((column1,column2)) do anything
#         else:
#             print()
#             # list.append((column1,column2)) do anything
# new_df = pd.DataFrame(list,columns=['column1', 'column2'])
# def change(item):
#     if ' (' in item:
#         return item[:item.find(' (')]
#     elif '[' in item:
#         return item[:item.find('[')]
#     else:
#         return item
# new_df =  new_df.applymap(change)
# new_column_names = {'any text and ?/ char': 'column1',
#                     'some text and !?/ char': 'column2',
#                     'date text and :?/ char': 'column3',
#                     } # to change dataframe with one line
# olympics_df.rename(columns=new_names, inplace=True)
