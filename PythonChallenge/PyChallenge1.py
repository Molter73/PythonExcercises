'''
Created on 17 dic. 2018

@author: Molter
'''

inputString = "http://www.pythonchallenge.com/pc/def/map.html"

if __name__ == '__main__':
    transtable = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
    print(inputString.translate(transtable))