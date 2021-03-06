from textwrap import dedent

# Invalid inputs
first = [{'x': 4, 'y': 2}, ['x', 'y'], 4]
second = {'x': 1, 'y': 3}
third = [{'x': 2, 'y': 1, 'z': 5}]

# Valid input
fourth = [{'x': 5, 'y': 3},
          {'x': 0, 'y': 0},
          {'x': 4, 'y': 3},
          {'x': 3, 'y': 3},
          {'x': 2, 'y': 3},
          {'x': 1, 'y': 3},
          {'x': 0, 'y': 3},
          {'x': -1, 'y': 3},
          {'x': 5, 'y': 3},
          {'x': 0, 'y': 0},
          {'x': 5, 'y': 3}]

def item_is_list(coords_list):
    if type(coords_list) != list:
        return False
    return True

def item_is_dict(item):
    if type(item) != dict:
        return False
    return True

def coords_valid(coords_dict, first_key='x', second_key='y'):
    # Checks if the number of keys is not 2
    if len(coords_dict.keys()) != 2:
        return False
    else:  # Checks if the x and y are present in coords dict
        if coords_dict.get(first_key) is None and \
                coords_dict.get(second_key) is None:
            return False
        else:  # Checks if the values of the dict are integers
            for coord in coords_dict.values():
                if type(coord) != int:
                    return False
    return True

def coords_hash(item):
    # naive, works for the example
    return item['x'] + item['y']

def handle_invalid_input(msg):
    raise ValueError(msg)

def get_store_visits(coords_list):
    num_invalid_visits = 0
    store_visit_count_dict = {}

    # Handle invalid input
    if not item_is_list(coords_list):
        handle_invalid_input("Input is not a list")

    # Loop through coords list
    for item in coords_list:
        if not item_is_dict(item):
            num_invalid_visits += 1
        elif not coords_valid(item):
            num_invalid_visits += 1
        else:
            if store_visit_count_dict.get(coords_hash(item)) is None:
                store_visit_count_dict[coords_hash(item)] = {'x': item['x'], 'y': item['y'], 'visits': 1}
                continue
            store_visit_count_dict[coords_hash(item)]['visits'] += 1

    # Include invalid entries
    store_visit_count_dict['invalid_visits'] = num_invalid_visits

    return store_visit_count_dict

def display_store_visits(store_visit_data):
    for key in store_visit_data.keys():
        if key != "invalid_visits":
            print(dedent(f'''
                Store no: {key}
                Coordinates: (x: {store_visit_data[key]['x']} y: {store_visit_data[key]['y']})
                Number of Visits: {store_visit_data[key]['visits']}
            '''))
        else:
            print(dedent(f"Invalid Entries: {store_visit_data[key]}"))


store_visit_data = get_store_visits(fourth)
display_store_visits(store_visit_data)
