import random

def guess_the_number():
    print("Welkom bij raad het nummer")
    print("ik denk aan een nummer tussen de 1 and 100.")
    print("Je hebt 10 beurten om het te raden.")
#dit zorgt ervoor dat je niet hoger dan 100, en niet lager dan 1 kan gaan
    secret_number = random.randint(1, 100)
    #dit zorgt ervoor dat je begint met 0 attempts en eindigd met 10 attempts
    attempts = 0
    max_attempts = 10
#dit zorgt ervoor dat als je attempts lager is dan je max attempts dat je het spel kan blijven spelen
    while attempts < max_attempts:
        try:
            guess = int(input("Probeer het te raden: "))
        except ValueError:
            #mocht je een letter of een getal hoger of lager invoert dan 1 of 100. dan geeft hij een foutmelding
            print("foutmelding. vul het juiste getal in!")
            continue
#deze line zorgt ervoor dat er een attempt bij komt
        attempts += 1
#dit zorgt ervoor dat als je nummer te hoog of te laag is dan geeft hij dat aan, als het nummer precies goed is geeft tie je een gefeliciteerd en heb je gewonnen
        if guess < secret_number:
            print("Te laag!")
        elif guess > secret_number:
            print("Te hoog!")
        else:
            print(f"gefeliciteerd! je hebt het geraden in: {attempts} beurten")
            #als je hebt gewonnen dan vraagt tie of je het opnieuw wilt spelen en kun je doen wat je zelf wilt
            play_again = input("Wil je het nog een keer spelen? (ja/nee): ")
            if play_again.lower() == "ja":
                guess_the_number()
            else:
                print("Bedankt voor het spelen!")
            return
#als je het niet heb gewonnen dan geeft hij een verloren message met de vraag of je het opnieuw wilt spelen
    print(f"Loser je hebt verloren het nummer was {secret_number}.")
    play_again = input("Wil je opnieuw spelen? (ja/nee): ")
    if play_again.lower() == "ja":
        guess_the_number()
    else:
        print("Bedankt voor het spelen")

guess_the_number()