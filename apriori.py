# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def get_products():
	return ['almonds', 'antioxydant juice', 'asparagus', 'avocado', 'babies food', 'bacon', 'barbecue sauce', 'black tea', 'blueberries', 'body spray', 'bramble', 'brownies', 'bug spray', 'burger sauce', 'burgers', 'butter', 'cake', 'candy bars', 'carrots', 'cauliflower', 'cereals', 'champagne', 'chicken', 'chili', 'chocolate', 'chocolate bread', 'chutney', 'cider', 'clothes accessories', 'cookies', 'cooking oil', 'corn', 'cottage cheese', 'cream', 'dessert wine', 'eggplant', 'eggs', 'energy bar', 'energy drink', 'escalope', 'extra dark chocolate', 'flax seed', 'french fries', 'french wine', 'fresh bread', 'fresh tuna', 'fromage blanc', 'frozen smoothie', 'frozen vegetables', 'gluten free bar', 'grated cheese', 'green beans', 'green grapes', 'green tea', 'ground beef', 'gums', 'ham', 'hand protein bar', 'herb & pepper', 'honey', 'hot dogs', 'ketchup', 'light cream', 'light mayo', 'low fat yogurt', 'magazines', 'mashed potato', 'mayonnaise', 'meatballs', 'melons', 'milk', 'mineral water', 'mint', 'mint green tea', 'muffins', 'mushroom cream sauce', 'nonfat milk', 'oatmeal', 'oil', 'olive oil', 'pancakes', 'parmesan cheese', 'pasta', 'pepper', 'pet food', 'pickles', 'protein bar', 'red wine', 'rice', 'salad', 'salmon', 'salt', 'sandwich', 'shallot', 'shampoo', 'shrimp', 'soda', 'soup', 'spaghetti', 'sparkling water', 'spinach', 'strawberries', 'strong cheese', 'tomato juice', 'tomato sauce', 'tomatoes', 'toothpaste', 'turkey', 'vegetables mix', 'white wine', 'whole weat flour', 'whole wheat pasta', 'whole wheat rice', 'yams', 'yogurt cake']

def init():
	# Data Preprocessing
	dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
	transactions = []
	for i in range(0, 7501):
	    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

	# Training Apriori on the dataset
	from apyori import apriori
	rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

	# Visualising the results
	results = list(rules)

	# base = input('Enter a base: ')

	# result = set()
	# for v in results:
	#     bases =  set(v.ordered_statistics[0].items_add)
	#     suggestions = set(v.ordered_statistics[0].items_base)
	#     if base in bases or base in suggestions:
	#         result.add(f'\tsuggested items : {suggestions}')
	        
	# print(*result, sep="\n")