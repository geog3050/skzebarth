'''
Below is a miniature program developed by Samuel Taylor for Geoprogramming.

This code is developed to input a list of values as floats, although it functions
with integers as well, and a climate defined by the user to return an F or U.
The F or U determines the status of leaves at a given temperature and evaluates
whether or not the leaves are Folded or Unfolded. 

This was developed for the user to write in their climate via input, but not to
define temperature as an input but as a variable from a list. If you would like
to modify the temperatures being assessed, either create a new list or modify the
temp/temp2 variables below. 
'''

temp = [-0.96, -14.38, 11.66, 40.07, 48.72, 0.55, 4.73, 24.82, 32.55, 31.98, -3.08, 36.41, 39.16]
temp2 = [17, 24, 29, 31]



user_choice = input('Enter your climate of choice from Tropical, Continental, or Polar: ')

def temp_check_string(values, climate):
    tropical_threshold = 30
    continental_threshold = 25
    polar_threshold = 18

    
    if climate == "tropical" or climate == "Tropical":
        for x in values:
            if x <=tropical_threshold:
                print("F")
            else:
                print("U")
    elif climate == "continental" or climate == "Continental":
        for x in values:
            if x <=continental_threshold:
                print("F")
            else:
                print("U")
    elif climate == "polar" or climate == "Polar":
        for x in values:
            if x <=polar_threshold:
                print("F")
            else:
                print("U")
    else:
        print('You either specified a climate not listed, or misspelled your climate of choice. Running program assuming a Polar/Other climate.')
        for x in values:
            if x <=polar_threshold:
                print("F")
            else:
                print("U")
                
                
                
temp_check_string(temp2, user_choice)