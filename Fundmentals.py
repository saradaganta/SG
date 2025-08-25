# Strings
print("Hello World")

fname = "siva"
lname = "kumar"
fullname = f"{fname} {lname}"
print(f"Hello, {fullname.title()}!")
print(f"Hello, {fullname}!")

sfname = "sarada"
slname = "ganta"
sfullname = f"{sfname} {slname}"
print(f"Hi, {sfullname.title()}!")
print(f"{fullname.title()} loves {sfullname.title()}!")

#Adding white spaces:
print("Siva")
print("\tKumar")

print("Languages:\nTelugu\nEnglish\nTamil")
print("Languages:\n\tTelugu\n\tEnglish\n\tTamil")
Languages = "'Tamil   '"
print(Languages)
Languages = Languages.rstrip()
print(Languages)

Languages = 'Taaaamil '
print(Languages)            # 'Tamil   '

Languages = Languages.rstrip()
print(Languages) # 'Tamil'

url = 'https://google.com'
print(url)
url = url.removeprefix('https://')
print(url)

name = "Mr.SKG Kumar"
print(name)
name = name.removeprefix("Mr.")
name = name.removesuffix("Kumar")
print(name)

#Exercise: Try IT YOURSELF
print('***************** Try IT YOURSELF ************')
name = "vikranth"
print(name)
print(name.upper())
print(name.title())

quote = "Only pain no gain"
print(f"Siva Gurram once said, {quote}? Python is way to gain.")

quote = "Only pain no gain.....!"
famous_person = "Mr.Siva Gurram"
print(f"{famous_person} once said, {quote}? Python is way to gain.")
print(f"{famous_person.removeprefix("Mr.")} once said, {quote.removesuffix(".....!")}? Python is way to gain.")