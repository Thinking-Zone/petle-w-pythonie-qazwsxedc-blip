pada = False 
licznik_nie = 0
while not pada:
    print("nie pada")
    odpowiedz = input("czy pada (t/n)")
    if odpowiedz == 'tak':
        print('powiedziales nie:' ,licznik_nie , 'razy')
        pada = True
    elif odpowiedz == 'nie':
        licznik_nie += 1 
    elif odpowiedz =='nie wiem':
        print("to sie dowiedz")
    else:
        print("odpowiedz t/n")
