from bs4 import BeautifulSoup # pip install bs4
import cfscrape # pip install cfscrape
import os
import random
import _thread
import time

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("[+] - prnt.sc image scraper\n")
    
    print("[1] - Random url")
    print("[2] - Predefined url part")
    print("[3] - Exit")

    menuInput = input("Choose an option: ")
    if menuInput == "1":
        amount = int(input('Number of threads: '))
        for thread in range(1, amount + 1):
            thread = str(thread)
            try:
                _thread.start_new_thread(fullRandom, (thread,))
            except:
                print('Error starting thread ' + thread)
        print('Succesfully started ' + thread + ' threads.')
        while True:
            time.sleep(1)
    elif menuInput == "2":
        predefRand()
    elif menuInput == "3":
        exit()

# Generating random prnt.sc url
def generateRandomUrl():
    return ''.join(random.choice(characters) for i in range(6))
    
# Scraping image url
def getImageLink(urlPart):

    c = scraper.get('https://prnt.sc/' + urlPart).content

    soup = BeautifulSoup(c, 'html.parser')

    all = soup.find_all('img', {'class':'no-click screenshot-image'})
    
    if len(all) > 0:
        return all[0].get('src')
    else:
        return 'Invalid url'

# Saving image if url is correct
def saveImage(url, name):
    os.makedirs('./img/', exist_ok = True)
    if url[0] == '/' or url == 'Invalid url':
        print('No image found')
        pass
    else:
        response = scraper.get(url).content
        with open(name + '.png', 'wb') as file:
            file.write(response)

# Using randomised url to scrape random pictures
def fullRandom(thread):
    while True:
        code = generateRandomUrl()
        print(f'Trying https://prnt.sc/{code}')
        saveImage(getImageLink(code), 'img/' + code)


# Using predefined url part, provided from user
def predefRand():
    counter = 0
    predefinedPart = str(input('Enter part of the url (3 - 5 characters): '))
    amount = int(input('Number of pictures to download: '))
    
    # Checking predefined part length to generate the rest
    if len(predefinedPart) == 3:
        for j in characters:
            for k in characters:
                for l in characters:
                    counter += 1
                    code = predefinedPart + j + k + l
                    print(f'{counter}: Trying https://prnt.sc/{code}')
                    saveImage(getImageLink(code), 'img/' + code)
                    
                    if counter == amount:
                        break
                if counter == amount:
                        break
            if counter == amount:
                        break
                    
    elif len(predefinedPart) == 4:
        for j in characters:
            for k in characters:
                counter += 1
                code = predefinedPart + j + k
                print(f'{counter}: Trying https://prnt.sc/{code}')
                saveImage(getImageLink(code), 'img/' + code)
                
                if counter == amount:
                    break
            
            if counter == amount:
                break
                
    elif len(predefinedPart) == 5:
        for j in characters:
            counter += 1
            code = predefinedPart + j
            print(f'{counter}: Trying https://prnt.sc/{code}')
            saveImage(getImageLink(code), 'img/' + code)
            
            if counter == amount:
                break
    end()

def end():
    os.system('cls' if os.name == 'nt' else 'clear')
    end = input("\nWould you like to continue? Y or N: ")
    if end == "Y" or end == "y":
        menu()
    elif end == "N" or end == "n":
        exit()
    else:
        print("Syntax error! Please provide Y or N!")
        end()

scraper = cfscrape.create_scraper()

characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

menu()
