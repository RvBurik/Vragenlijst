import numpy as np
import time
import sys

beginVragen = ["Heeft u een computer/tablet/mobiel/smartphone?", "Heeft u een tablet?", "Heeft u een mobiel?", "Heeft u een smartphone?",
               "Heeft u een computer?", "Bent u een man?",];

vragenMannen = ["Kunt u overweg met het nieuws?", "Leest u via het internet het nieuws?", "Kunt u iets opzoeken op Google?", "Kunt u uw mail bekijken en hieropop reageren?",
                "Kunt u een bestand downloaden die u via de mail binnenkrijgt?", "Kunt u muziek/films/spelletjes downloaden?"];

vragenVrouwen = ["Heeft u contact met familie via het internet?", "Heeft u meer dan drie dagen per week contact met uw familie?" , "Doet u spelletjes op uw computer?", "Maakt u hierbij dan gebruik van het internet?", "Kunt u muziek/films/spelletjes downloaden?"];

eindVragen = ["Heeft u wel eens last gehad van?"];
#list met antwoorden
antwoorden = [];

#Functies
def toonVragen(vragen):
    for i in range(len(vragen)):
        print("")
        antwoord = input(vragen[i]);
        #Als een antwoord binnen de vragen mannenlijst nee is, worden er geen verdere vragen gesteld
        #en gaat de quiz verder bij de algemene vragen
        if antwoord == "n" and i == 0 and vragen[0] == beginVragen[0]:
            print("Bedankt voor het invullen!");
            data = open(filename, 'a');
            data.writelines("Beginvraag: Nee");
            data.close();
            sys.exit();
        
        if antwoord == "j" or antwoord == "n":
            antwoorden.append(antwoord); 
            if antwoord == "n" and vragen[0] != beginVragen[0] and vragen[0] != eindVragen[0]:
                break;
        else:
            print("U heeft niet het juiste antwoord  ingevuld! Automatisch antwoord 'Ja' toegevoegd!");
            antwoorden.append("j, (auto added)"); 

def supportLinesToevoegenAanBestand(m, antwoorden):
    if(m == len(antwoorden)-1):
        data.writelines("Eindvragen: " + "\n");
        antwoordenToevoegenAanBestand(m,antwoorden[m]);
        return;
    if(m > 5 and antwoorden[5] == 'j'):
        data.writelines("Hoofdvragen mannen:" + "\n");
    elif(m > 5 and antwoorden[5] == 'n'):
        data.writelines("Hoofdvragen vrouwen:" + "\n");
    antwoordenToevoegenAanBestand(m,antwoorden[m]);

def antwoordenToevoegenAanBestand(m, antwoord):
    if(antwoord == 'j'):
        data.writelines("Vraag: "   + str(m) + ": Ja"  + "\n");
    else:
        data.writelines("Vraag: " + str(m) + ": Nee"  + "\n");

#Main program
print("Welkom bij de vragenlijst!");
print("Het invullen zal niet lang duren! Alle vragen kunnen enkel beantwoorden met j (ja) of n (nee)");
naam = input("Vul uw naam in" + " ");
filename = "antwoorden-" + naam + "-" + time.strftime("%Y-%m-%d_%H-%M-%S") + ".txt";


#Toont de beginvragen en slaat deze op in de list "antwoorden"
toonVragen(beginVragen);
    
#als het antwoord op de 6de vraag JA is -> dus man, start de vragenlijst van de man
if antwoorden[5] == "j":
    toonVragen(vragenMannen);
    
#Gebruiker is dus een vrouw
else:
    toonVragen(vragenVrouwen);
    

    
#Toont de eindvragen
for k in range(len(eindVragen)):
    print("");
    antwoorden.append(input(eindVragen[k]));


data = open(filename, 'a');
for m in range(len(antwoorden)):
    supportLinesToevoegenAanBestand(m, antwoorden);   

data.close();





