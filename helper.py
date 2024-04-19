import json

def get_card_info(card_name):
    with open('card_data.json', 'r') as file:
        data = json.load(file)
        cards = data.get('cards', [])
        for card in cards:
            if card.get('name_short').lower() == card_name.lower():
                return card
    return None
