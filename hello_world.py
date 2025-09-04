print("velkommen til min AI quiz")

# Input stopper programmet og venter på, at brugeren skriver noget i terminalen eller med andre ord bruges til at tage brugerens tekstinput med i programmet
playing = input("Vil du gerne deltage i quizzen? ")

# != betyder "er ikke". quit gør at programmet stoppes. og .lower() gør alle tekser/svar til lowercase, så det altid er rigtig ligemeget om det er lower/upper useren brugte
if playing.lower() != "ja":
    quit()

print("Godt! Lad os spille")

# sætter scoren på 0, da quizzen nu officielt går igang
score = 0

answer = input("Hvad står CNN for, når vi snakker om AI? ")
if answer.lower() == "convolutional neural network":
    print("Korrekt!")
# score += 1 betyder tag værdien af score og plus 1 til
    score += 1
else:
    print("Det er forkert, det står for convolutional neural network")

# Kan godt genbruge variablen "answer" da answer = ... anden gang, overskriver mand bare den gamle værdi
answer = input("Hvad står RNN for, når vi snakker om AI? ")
if answer.lower() == "recurrent neural network":
    print("Korrekt!")
    score += 1
else:
    print("Det er forkert, det står for recurrent neural network")

# str() konverterer tallet til en streng, så det kan sættes sammen med de andre strenge("").
print("Du fik i alt " + str(score) + " spørgsmål korrekte")

# Viser hvor mange procent vi fik rigtige
print("Du fik i alt " + str(score/2 * 100) + "%. rigtige")
