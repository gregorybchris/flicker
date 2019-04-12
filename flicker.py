import client_api
import pprint


if __name__ == '__main__':
    print("Flicker is running")
    api = client_api.ClientAPI()

    message = "Flicker!"
    print("Posting message: ", message)
    response = api.post_message(message)
    print("Received: ", response.status_code, response.json())

    response = api.get_messages()
    messages = response.json()['messages']
    print("Get messages:")
    pprint.pprint(messages)
