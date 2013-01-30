import os

IMG_BASE_PATH='imgs/'
elementFloderList=['aether', 'air', 'darkness', 'death', 'entropy', 'fire', 'life']
CARD_FILE='cards.txt'
IMG_NAME_COL=0

cardList=[]
##get card name by img's name
childFiles=os.listdir(IMG_BASE_PATH)
print(childFiles)
for i in childFiles:
    p=IMG_BASE_PATH+i
    if os.path.isdir(p) and i in elementFloderList:
        cardList+=os.listdir(p)

##print(cardList)


exist_cardList=[]
##get card.txt file exist name
file=open(CARD_FILE, 'r')
file.readline()
while True:
    ss=file.readline()
    if ss=='':
        break
    arr=ss.split('\t')
    exist_cardList.append(arr[IMG_NAME_COL])

file.close()
##print(exist_cardList)


## rewrite the file append
file=open(CARD_FILE, 'a')
for name in cardList:
    if name not in exist_cardList:
        file.write(name+'\n')

file.close()




