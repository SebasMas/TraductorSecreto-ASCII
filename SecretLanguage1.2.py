#Vamos a hacer una función que transforme cada caracter de la frase que introducimos a un valor ASCII

while True:

    print("¿Qué deseas hacer?")
    print("")
    print("1 - Convertir mensaje")
    print("2 - Traducir mensaje")
    print("")

    option = int(input("Ingrese una opción: "))

    if option == 1:

        def phrase_to_numbers(phrase):
            phrase = phrase.lower()
            numbers = []
            for character in phrase:
                ascii_value = ord(character)
                numbers.append(ascii_value)
            return numbers

        phrase = input("Ingrese una frase: ")
        print(phrase_to_numbers(phrase))  


    elif option == 2:
        def numbers_to_phrase(numbers):
            numbers = numbers.split(',')
            phrase = ""
            for number in numbers:
                character = chr(int(number))
                phrase += character
            return phrase

        numbers = input("Ingrese el mensaje (Ejemplo: 104-111-108-105): ")
        print(numbers_to_phrase(numbers)) 