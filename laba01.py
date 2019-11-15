
#реверс
slogan = str(input ("Напишіть своє речення"))
sentence = slogan [::-1]
words = sentence.split()
sentence_rev = " ".join(reversed(words))
print ( sentence_rev)\

#хелло ворлд
("Hello world")

#калькулятор
a=int(input("Write your number"))
b=int(input("Write your number"))
c=a+b
print(c)

#шифр
i=5
while i < 15:
    alpha = 'abcdefghijklmnopqrstuvwxyz1234567890QWERTYUIOPASDFGHKLZXCVBNM'
    step = 1
    text = input("Please write your text").strip()
    res = ''
    for c in text:
        if c.isalpha():
         res += alpha[(alpha.index(c) + step) % len(alpha)]
        else:
         res += c
    print("Result " + res + "")

#подвоєння
word = input("Write your sentence: ")
a = "".join([x*2 for x in word])
print(a)