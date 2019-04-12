import client_api


if __name__ == '__main__':
    print("Flicker is running")
    api = client_api.ClientAPI()
    api.post_message("Flicker!")
    print("Posted a new message to Flicker!")
