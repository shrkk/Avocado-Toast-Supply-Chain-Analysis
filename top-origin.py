import pandas as pd

#reading in the files
avocado = pd.read_csv('data/avocado.csv',sep = '\t')
olive_oil = pd.read_csv('data/olive_oil.csv',sep = '\t')
sourdough = pd.read_csv('data/sourdough.csv',sep = '\t')

#reading in relelvant .txt fields
with open('data/relevant_avocado_categories.txt', 'r') as file:
    relevant_avocado_categories = file.read().splitlines()
   # print(relevant_avocado_categories)
    file.close()

with open('data/relevant_olive_oil_categories.txt', 'r') as file:
    relevant_olive_oil_categories = file.read().splitlines()
    file.close()

with open('data/relevant_sourdough_categories.txt', 'r') as file:
    relevant_sourdough_categories = file.read().splitlines()
    file.close()
    
#subsetting columns based on relevance    
    
relevant_columns = ['code', 'lc', 'product_name_en', 'quantity', 'serving_size', 'packaging_tags', 'brands', 'brands_tags', 'categories_tags', 'labels_tags', 'countries', 'countries_tags', 'origins','origins_tags']
avocado = avocado[relevant_columns]
olive_oil = olive_oil[relevant_columns]
sourdough = sourdough[relevant_columns]

#reformatting function to compare if row values are within the relevant categories the analysis intends to identify.

def reformat(df, tag):
    dropset = True
    df.dropna(subset = 'categories_tags', inplace = True)
    df['categories_tags'] = df['categories_tags'].str.split(',')
    for i, r in df.iterrows():
        if tag == 1:
            for x in relevant_avocado_categories:
                if x == r['categories_tags']:
                    dropset = False
            if dropset == True:
                df.drop(i)
        if tag == 2:
            for x in relevant_olive_oil_categories:
                if x == r['categories_tags']:
                    dropset = False
            if dropset == True:
                df.drop(i)      
        if tag == 3:
            for x in relevant_sourdough_categories:
                if x == r['categories_tags']:
                    dropset = False
            if dropset == True:
                df.drop(i)
                
#running the reformatting function

reformat(avocado, 1)
reformat(olive_oil, 2)
reformat(sourdough, 3)

#identifying the top exporting region to the UK and cleaning the value 

def top_origin(df, tag):
    df = df[(df['countries']=='United Kingdom')]
    counts = df['origins_tags'].value_counts()
    country_name = counts.index[0]
    country_name = country_name.replace('en:','')
    country_name = country_name.replace('-',' ')
    print(country_name)
    
top_avocado_origin = top_origin(avocado, 1)
top_olive_oil_origin = top_origin(olive_oil,2)
top_sourdough_origin = top_origin(sourdough,3)
