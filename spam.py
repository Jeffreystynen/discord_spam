import requests
import random 

def send_messages(message, amount):
    payload = {
        'content' : message
    }

    # to get the authorization url:
    # go to the Discord channel in browser, open dev tools and go to network
    # send a message in the channel, under network activities click on messages
    # under headers go to Request Headers and copy authorization
    header = {
        'authorization' : ''
    }

    for i in range(amount):
        # to retrieve the request url follow the same steps as the authorization url, except under General, instead of Request Headers, copy the Request url
        r = requests.post('', data=payload, headers=header)


def wordlist(file):
    with open(file) as f:
        text = f.readlines()
        return text


def main():
    print("Set amount to 0 to quit")
    while(True):
        method = input("What method do you want to use?\nc - custom input\nw - wordlist\nr - random \nq - quit\n")
        if method == "c":
            amount = int(input("Enter the amount of messages you want to send: "))
            if amount == 0:
                break
            message = input("What do you want to say: ")
            send_messages(message, amount)

        elif method == "w":
            file = input("Enter the file path of the worldlist: ")
            text = wordlist(file)
            amount = 1
            for line in text:
                if line != '\n':
                    message = line
                    send_messages(message, amount)
        elif method == "r":
            file = input("Enter the file path of the worldlist: ")
            amount_random = int(input("Enter the amount of random words you want to send: "))
            amount = 1
            text = wordlist(file)
            for i in range(amount_random):
                message = text[random.randint(1, len(text))]
                send_messages(message, amount)
        elif method == "q":
            break

main()