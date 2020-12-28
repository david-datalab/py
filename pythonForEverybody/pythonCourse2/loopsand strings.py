#looping and strings
fruit = 'banana'
for letter in fruit :
  print(letter)

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
#looping and counting
word = 'banana'
count = 0
for letter in word:
    if letter =='a':
        count = count + 1
print(count)

text = "X-DSPAM-Confidence:    0.8475";
#if '0.8475' in text:
    #x = float(0.8475)
    #y = float(x)
    #print(x)
num = text.find('0.8475')
print(num)
f = text[23:]
i = float(f)
print(i, type(i))
