import requests

if __name__ == '__main__':
    url_ = 'https://superheroapi.com/api/'
    token = '2619421814940190'
    search_method = '/search/'
    array_of_names = ['Hulk', 'Captain America', 'Thanos']
    heroes_power = {}
    the_smartest = {}
    for heroes_names in array_of_names:
        answer_sheet = requests.get(url_+token+search_method+heroes_names)
        result_tag = (answer_sheet.json())['results'][0]
        tag_power = result_tag['powerstats']
        tag_intellect = tag_power['intelligence']
        heroes_power[heroes_names] = tag_intellect
    max_intelligence = 0
    for key, values in heroes_power.items():
        if int(values) > max_intelligence:
            max_intelligence = int(values)
            heroes_name = key
        else:
            if max_intelligence == int(values):
                print('Два(или более) героя с одинаковым интелектом')
                break
    the_smartest[heroes_name] = max_intelligence
    for name, intelligence in the_smartest.items():
        print(f'Самый умный: {name}\nИнтелект: {intelligence}')
