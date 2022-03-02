import cs50

#get the text
text = cs50.get_string ("Text: ")

#get variables
lCount=0
wCount=1
sCount=0
for i in text:
    if i.isalpha() == True:
        lCount = lCount +1

    elif i == ' ':
        wCount +=1

    elif i =='!' or i == '?' or i == '.':
        sCount = sCount + 1

L = float((lCount/wCount)*100)
S = float((sCount/wCount)*100)
index = (0.0588 * L - 0.296 * S - 15.8)
index = round(index)

if index > 16:
    print("rade 16+")
elif index  < 1:
    print("Before Grade 1")
else:
    print("Grade ", index)

