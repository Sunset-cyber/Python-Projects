# input number of cents and will output change

total_cents = int(input())

dollars = total_cents // 100
leftover_cents = total_cents % 100

quarters = leftover_cents // 25
leftover_cents = leftover_cents % 25

dimes = leftover_cents // 10
leftover_cents = leftover_cents % 10

nickels = leftover_cents // 5
leftover_cents = leftover_cents % 5

if total_cents == 0:
    print ('No change')

if dollars == 1:
    print(dollars, 'Dollar')
elif dollars > 1:
    print(dollars, 'Dollars')

if quarters == 1:
    print(quarters, 'Quarter')
elif quarters > 1:
    print(quarters, 'Quarters')

if dimes == 1:
    print(dimes, 'Dime')
elif dimes > 1:
    print(dimes, 'Dimes')

if nickels == 1:
    print(nickels, 'Nickel')
elif quarters > 1:
    print(nickels, 'Nickels')

if leftover_cents == 1:
    print(leftover_cents, 'Penny')
elif leftover_cents > 1:
    print(leftover_cents, 'Pennies')
