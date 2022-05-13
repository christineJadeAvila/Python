#Asks for a name
def helloYou(name):
    print('Hell o ' + name)
    print('')

print('Whats ya name? ')
name = input()
helloYou(name)

# Asks for your order
def whatsYourOrder(order):
    print('Your order is ' + order)
    print(order + ' costs Php 100')
    print('')

print('What is your Order? ')
order = input()

whatsYourOrder(order)

#Asks who's your crush
def whosYaCrush(crush):
    print('Your crush is ' + crush + ' ? ^ o ^')
    print('for how long now ?')

    # Asks how long has she been your crush, yiiee 6 years
    def howLong(how):
        print(how)
        print('that long???' + how + ('!!!????'))
    how = input()
    howLong(how)

print('Who is your crush?' )
crush = input()
whosYaCrush(crush)