import requests
import threading
import time
from colorama import Fore, Back, Style

def check_token(token, use_proxies):
    headers = {
        'Authorization': token
    }
    proxies = {'https': None} if not use_proxies else {'https': use_proxies}
    try:
        response = requests.get('https://discord.com/api/v9/users/@me', headers=headers, proxies=proxies)
        if response.status_code == 200:
            print('\033[1;37m'+ '[Cat] ' + '\033[32;76;1m' + 'Valid '+'\033[1;37m' + f'token: {token}')
            with open('valid_tokens.txt', 'a') as f:
                f.write(token + '\n')
        else:
            print('\033[1;37m'+ '[Cat] ' + '\033[31m' + 'Invalid '+'\033[1;37m' + f'token: {token}')
    except:
        pass

def main(use_proxies=True):
    output_file_path = 'valid_tokens.txt'
    output_file = open(output_file_path, 'w')
    # Read tokens from file
    with open('tokens.txt', 'r') as f:
        tokens = f.read().splitlines()

    # Check tokens using proxies in parallel
    threads = []
    for token in tokens:
        t = threading.Thread(target=check_token, args=(token, use_proxies))
        t.start()
        threads.append(t)

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Close the output file
    output_file.close()

if __name__ == '__main__':
        main(use_proxies=False)
