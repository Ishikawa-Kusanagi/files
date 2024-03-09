cook_book = {}

with open('text.txt', encoding='utf-8') as f:
    for line in f:
        dish_name = line.strip()
        cook_book[dish_name] = []
        # print(cook_book)
        for i in range(int(f.readline())):
            ingredients = f.readline().strip().split(' | ')
            ingredient_name = ingredients[0]
            quantity = ingredients[1]
            measure = ingredients[2]
            cook_book[dish_name].append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
# print(cook_book[dish_name])
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                new_shop_list_item = ingredient
                new_shop_list_item['quantity'] = int(new_shop_list_item['quantity']) * person_count
                if new_shop_list_item['ingredient_name'] not in shop_list:
                    shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
                else:
                    shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
        else:
            return 'Такого рецепта нет в кулинарной книге'
        return shop_list
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))