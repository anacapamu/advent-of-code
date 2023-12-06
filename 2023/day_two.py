# --- Day 2: Cube Conundrum ---

# --- Part One ---

bag = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def process_line(line):
    '''
    Separate and reformat the game id and sets from one record

    Parameters:
    line (str): a game record in the input text file

    Returns:
    game_id (int)
    reformatted_game_sets (array): each set is a dict with color as key and quantity as value
    '''

    game, game_sets = line.split(':', 1) # Separates game id from sets
    game_id = int(game.strip().split(' ')[-1])  # Extract only the digit for ID

    game_sets = game_sets.strip().split(';') # Separates each set from each other

    # Convert each set to a dict with ex format {'blue': 3, 'red': 4}
    reformatted_game_sets = []
    for game_set in game_sets:
        items = game_set.strip().split(', ')
        set_dict = {item.split(' ')[1]: int(item.split(' ')[0]) for item in items}
        reformatted_game_sets.append(set_dict)

    return game_id, reformatted_game_sets

def convert_txt_to_dict(file_name):
    '''
    Convert each line from a text file to a key-value pair of a dict

    Parameters:
    file_name (str): name of input txt file in same directory as this one

    Returns:
    game_records (dict): maps game_id (int) to game_sets (array)
    '''

    game_records = {}

    with open(file_name, 'r') as file:
        for line in file:
            game_id, game_sets = process_line(line)
            game_records[game_id] = game_sets
    return game_records

def is_game_valid(game_sets):
    '''
    Checks if a game is valid based on the content of bag

    Parameters:
    game_sets (dict): maps color (str) to quantity (int) of each set; 3 sets in total

    Returns:
    True: if quantity of a color does not exceed quantity of same color in bag
    '''

    for game_set in game_sets:
        for color, quantity in game_set.items():
            if color not in bag or bag[color] < quantity:
                return False
    return True

def list_possible_games(game_records):
    '''
    Checks for all possible games in input file

    Parameters:
    game_records (dict): maps game_id (int) to game_sets (array)

    Returns:
    possible_game_ids (array): game_ids are all int
    '''

    possible_game_ids = []

    for game_id, game_sets in game_records.items():
        if is_game_valid(game_sets):
            possible_game_ids.append(game_id)

    return possible_game_ids

def sum_game_ids(game_ids):
    '''
    Adds up all the game IDs provided

    Parameters:
    game_ids (array): list of integers

    Returns:
    sum (int): sum of all game_ids
    '''

    sum = 0

    for game_id in game_ids:
        sum += game_id

    print("The sum of the possible game IDs =", sum)
    return sum

if __name__ == "__main__":

    game_records = convert_txt_to_dict("day_two_input.txt")
    possible_game_ids = list_possible_games(game_records)
    sum_game_ids(possible_game_ids)
