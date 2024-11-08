import random
pada = random.choice([True, False])
zgaduj = True
while zgaduj:
    odpowiedz = input("czy pada? (t/n) ").strip().lower()
    
    if odpowiedz not in ['t', 'n']:
        print("wpisz albo t albo n")
        continue
    
    if (pada and odpowiedz == 't') or (not pada and odpowiedz == 'n'):
        print ("hura zgadles")
        zgaduj = False
    else:
        print("jestes glupi spróbuj ponownie")
