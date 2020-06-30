# This code is for a project work for descriptive statistics withreal retail data

import csv

with open("retail_data.csv", "r") as f:

    reader = csv.DictReader(f)
    retail_data = list(reader)

#To print the first transaction lines 
print(retail_data[0].values())

#To print the types of all values
for item in retail_data[0].values():
  d = {}
  d[item] = type(item)
#types_retail_data = [type(value) for value in retail_data[0]]
#print('\n',types_retail_data)
  print('\n',d)
#To determine the total number of lines
  print ('\nTotal number of lines is: ',len(retail_data))


#The function below takes a customer ID and prints a summary of the customer's transactions

def cust_stats(Customer_ID):

    total_customer_expenditure = 0
    number_unique_products = 0
    wooden_products_expenditure = 0
    total_quantity_purchased = 0
    unique_products = []
    
    for item in retail_data:
      
      if item['CustomerID']== Customer_ID:

        total_quantity_purchased += (int(item['Quantity'])) #This converts all quantities from strings to integers and sums all quantities belonging to the same customer_ID 
        
        total_customer_expenditure += (int(item['Quantity'])*float(item['UnitPrice'])) #This converts all quantites from strings to floats and sums the product of the quantity of items purchased multiplied by the unit price.

        if item['StockCode'] not in unique_products:# 'not in' is used so each item is counted only once
          unique_products.append(item['StockCode']) 
      
        if 'WOODEN'in item['Description']:
          wooden_products_expenditure += (int(item['Quantity'])*float(item['UnitPrice']))

        
    number_unique_products = len(unique_products)

    print(f'\nTotal quantity purchased by Customer ID {Customer_ID} is: {total_quantity_purchased} euro')
    print(f'\nTotal customer expenditure by Customer ID {Customer_ID} is: {total_customer_expenditure} euro')
    print(f'\nNumber of unique products purchased by Customer ID {Customer_ID} is: {number_unique_products} items')
    print(f'\nCost of wooden products purchased by Customer ID {Customer_ID} is: {wooden_products_expenditure} euro')
    

cust_stats('17850') #To check if the function works correctly


def total_customers():#The purpose of this function is to extract all customers and give their total numbers
  list_of_customers = set()

  for item in retail_data:
      list_of_customers.add(item['CustomerID'])

  number_of_customers = len(list_of_customers)

  print(f'\nTotal number of customers  are: {number_of_customers}')

total_customers() #To check if the function works correctly


def total_products():#The purpose of this function is to extract all products and give the total number
  list_of_products =set()

  for item in retail_data:
      list_of_products.add(item['StockCode'])

  number_of_products = len(list_of_products)

  print(f'\nTotal number of products  are: {number_of_products}')
  return

total_products() #To check if the function works correctly 
