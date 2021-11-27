from pprint import pprint
import os
 
path = os.path.join(os.getcwd(),'recipes.txt')
with open(path, encoding = "utf-8") as file:
     book_of_recipes = {}
     for recipe in file:
         recipe_name = recipe.strip()
         counter = int(file.readline().strip())
         temp_data = []
         for item in range(counter):
             name,quantity,units = file.readline().strip().split('|')
             temp_data.append({'name':name.strip(),'quantity':quantity.strip(),'units':units.strip()})
         book_of_recipes[recipe_name] = temp_data
         file.readline()
pprint (book_of_recipes,width=150)
print()
 
def list_of_products_by_dish (dishes, person_count):
     list_of_all_products ={}
     for dish in dishes:
          if dish in book_of_recipes:
             for product in book_of_recipes[dish]:
                 if product['name'] in list_of_all_products:
                     list_of_all_products[product['name']]['quantity'] += int(product['quantity']) * person_count
                 else:
                     list_of_all_products[product['name']] = {'units': product['units'],'quantity': int(product['quantity']) * person_count}

 
     print()
     pprint (list_of_all_products)
 
 
list_of_products_by_dish (['Омлет','Омлет'], 2)
