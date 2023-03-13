import random

who = ['The dog','My grandma','His turtle','My bird'];
action = ['ate','peed','crushed','broke'];
what = ['my homework', 'the keys', 'the car'];
when = ['before the class','right on time','when I finished','during my lunch','while I was praying'];

r1 = random.randint(0, len(who)-1)
r2 = random.choice(action)
r3 = round(random.random()*(len(what)-1))
r4 = random.choice(when)

#1
excuse = who[r1]+' '+r2+' '+what[r3]+' '+r4
#2
excuse = f'{who[r1]} {r2} {what[r3]} {r4}'
print(excuse)