def read_cook_book(file_name):
    with open(file_name, 'r', encoding= 'utf-8') as f:
        cook_book = {}
        for line in f:
            dish_name = line.strip()
            if not dish_name:
                break
            cook_book[dish_name] = []
            num_ingredient = int(f.readline().strip())
            for i in range(num_ingredient):
                ingredient_name, quantity, measure = f.readline().split(' | ')
                cook_book[dish_name].append({
                    'ingredient_name' : ingredient_name,
                    'quantity' : int(quantity),
                    'measure' : measure.strip()
                })
    return cook_book
print(read_cook_book('text.txt'))
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_cook_book('text.txt')
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
    return shop_list
print(get_shop_list_by_dishes('Омлет', 2))
