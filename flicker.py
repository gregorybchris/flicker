import requests


def get_mortality_data():
    api_endpoint = 'https://mort-vis.herokuapp.com/summary'

    params = {
        'age': 23,
        'race': 'White',
        'gender': 'M'
    }

    response = requests.get(url=api_endpoint, params=params)
    return response.json()


if __name__ == '__main__':
    print("Flicker is running")
    data = get_mortality_data()
    deaths = data['summary']['deaths']
    print(f"Number of deaths: {deaths}")
