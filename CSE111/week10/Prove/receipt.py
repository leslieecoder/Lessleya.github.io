import csv

all_products = {}

#open the product.csv file and store its content into the 
#all_products dictionary
with open("products.csv", "rt") as infile:

    #use the csvmodule to create a reader object
    reader = csv.reader(infile)

    #skip first line
    next(reader)

    #Read each row from the csv file
    for row in reader:
        product_number = row[0]
        product_name = row[1]
        product_price = row[2]

        #store the data in the dictionary
        all_products[product_number] = [product_number, product_name, product_price]

print(all_products)