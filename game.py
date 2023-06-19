import random

def guess_the_number():
    print("Welkom bij raad het nummer")
    print("ik denk aan een nummer tussen de 1 and 100.")
    print("Je hebt 10 beurten om het te raden.")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            guess = int(input("Probeer het te raden: "))
        except ValueError:
            print("foutmelding. vul het juiste getal in!")
            continue

        attempts += 1

        if guess < secret_number:
            print("Te laag!")
        elif guess > secret_number:
            print("Te hoog!")
        else:
            print(f"gefeliciteerd! je hebt het geraden in: {attempts} beurten")
            play_again = input("Wil je het nog een keer spelen? (ja/nee): ")
            if play_again.lower() == "ja":
                guess_the_number()
            else:
                print("Bedankt voor het spelen!")
            return

    print(f"Loser je hebt verloren het nummer was {secret_number}.")
    play_again = input("Wil je opnieuw spelen? (ja/nee): ")
    if play_again.lower() == "ja":
        guess_the_number()
    else:
        print("Bedankt voor het spelen")

guess_the_number()