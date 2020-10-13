# This script extracts images of Pokemon from the Internet.
# If not sure, do not make changes. However, you may change the values of the variables for which I have provided comments to explain their usage.

import os
import urllib.request

while True:
    inp = input('Enter the Pokemon number till which you want to extract (simply press "Enter" if you want to extract all the images): ')
    if inp=='':
        e = 893  # This is the total number of Pokemon till date.
        break
    else:
        try:
            e = int(inp)
            break
        except:
            print('Oops, wrong input! Please try again.')

s = 1 # Extraction starts from this Pokemon number.

url = 'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/'
savedTo = 'Pokemon Images/'  # This is the directory in which the images will be saved.

fhand = open('stopFile.txt','w')
fhand.write('start')
fhand.close()
print('To stop the process, change the text in stopFile.txt to "stop".')

for i in range(s,e+1):
    try:
        fhand = open('stopFile.txt','r')
    except:
        input('Seems like you have deleted stopFile.txt. As a result, the process has ended. Press "Enter" to exit.')
        quit()
    if(fhand.read()=='stop'): break
    fhand.close()
    
    loc = savedTo+str(i)+'.png'
    if os.path.isfile(loc): continue
    
    try:
        urllib.request.urlretrieve(url+str(i).zfill(3)+'.png',loc)
    except:
        print('Could not extract '+str(i)+'.png.')

fhand.close()
os.remove('stopFile.txt')
input('Done. Press "Enter" to exit.')
