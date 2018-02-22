# A nutritonist who works for a fitness club helps members by evaluating their diets.
# As part of her evaluation, she asks members for the number of fat grams,
# carbohydrate grams, and protein grams that they consumed in a day.
# Then, she calculates the number of calories that result from the fat, using the following formula:
# calories from fat = fat grams X 9
# calories from carbs = carb grams X 4
# calories from protein = protein grams X 4
def calculate_calories_from_fat (fat_grams):
    calories_from_fat = fat_grams = 9
    return calories_from_fat
def calculate_calories_from_carbs (carb_grams):
    calories_from_carbs = carb_grams = 4
    return  calories_from_carbs
def caluculate_calories_from_protein (protein_grams):
    calories_from_protein = protein_grams = 4
def main():
    user_fat_grams = float(input("enter how many fat grams you consumed "))
    user_carb_grams = float(input("enter how many carb grams you consumed "))
    user_protein_grams = float(input("eneter how many protein grams you consumed"))
    calories_from_fat = calculate_calories_from_fat(user_fat_grams)
    calories_from_carbs = calculate_calories_from_carbs(user_carb_grams)
    calories_from_protein = caluculate_calories_from_protein(user_protein_grams)
    print(" calories form fat are " + format( calories_from_fat) + " calories", "calories from carbs are " + \
          format(calories_from_carbs) + " calories" " and calories from protein are " + format(calories_from_protein))
main()
