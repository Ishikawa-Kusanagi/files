def create_cook_book(file_path):
    cook_book = {}

    with open(file_path, 'r', encoding= 'utf-8') as f:
        while True:
            dish_name = f.readline().strip()
            if not dish_name:
                break

            ingredients_count = int(f.readline().strip()) # убраить ошибку
            ingredients = []

            for _ in range(ingredients_count):
                ingredient_info = f.readline().strip().split(' | ')
                ingredient_name = ingredient_info[0]
                quantity = int(ingredient_info[1])
                measure = ingredient_info[2]

                ingredient = {
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                }
                ingredients.append(ingredient)

            cook_book[dish_name] = ingredients

    return cook_book


file_name = 'text.txt'
cook_book = create_cook_book(file_name)
# print(cook_book)
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
                else:
                    shop_list[ingredient_name]['quantity'] += quantity

    return shop_list


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
