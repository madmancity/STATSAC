import math
import random

#To initialize bracket and seeds, enter dictionary pairs where the key is the team name, and the value is the seed
#If seeds aren't being used, other statistics or simply a '0' can be put in the value slot
#I have used the 2023 NCAA Men's Basketball Tournament as an example
r1 = {
    "Alabama": 1,
    "Texas A&M CC/SEMO": 16,
    "Maryland": 8,
    "West Virginia": 9,
    "San Diego State": 5,
    "Charleston": 12,
    "Virginia": 4,
    "Furman": 13,
    "Creighton": 6,
    "NC State": 11,
    "Baylor": 3,
    "UCSB": 14,
    "Missouri": 7,
    "Utah State": 10,
    "Arizona": 2,
    "Princeton": 15,
    "Purdue": 1,
    "TX SO/FDU": 16,
    "Memphis": 8,
    "FAU": 9,
    "Duke": 5,
    "Oral Roberts": 12,
    "Tennessee": 4,
    "Louisiana": 13,
    "Kentucky": 6,
    "Providence": 11,
    "Kansas State": 3,
    "Montana State": 14,
    "Michigan State": 7,
    "USC": 10,
    "Marquette": 2,
    "Vermont": 15,
    "Houston": 1,
    "NKU": 16,
    "Iowa": 8,
    "Auburn": 9,
    "Miami": 5,
    "Drake": 12,
    "Indiana": 4,
    "Kent State": 13,
    "Iowa State": 6,
    "MS ST/Pitt": 11,
    "Xavier": 3,
    "Kennesaw State": 14,
    "Texas A&M": 7,
    "Penn State": 10,
    "Texas": 2,
    "Colgate": 15,
    "Kansas": 1,
    "Howard": 16,
    "Arkansas": 8,
    "Illinois": 9,
    "St. Mary": 5,
    "VCU": 12,
    "UConn": 4,
    "Iona": 13,
    "TCU": 6,
    "ASU/Nev": 11,
    "Gonzaga": 3,
    "GCU": 14,
    "Northwestern": 7,
    "Boise State": 10,
    "UCLA": 2,
    "UNCA": 15
}
#This function simulates the progression of the tournament, calling functions one by one to complete the tournament
def generate(round1):
    #Computing a round halves the number of teams, simulating that round and adding the winners to the next round.
    r2 = compute(r1)
    s16 = compute(r2)
    e8 = compute(s16)
    f4 = compute(e8)
    final = compute(f4)
    champ = compute(final)
    #Winners of each round are printed
    print(r2)
    print(s16)
    print(e8)
    print(f4)
    print(final)
    print(champ)
    #Bracket is constructed by plotting the teams on a bracket drawn using long strings
    bracket(list(r1), list(r2), list(s16), list(e8), list(f4), list(final), list(champ))
    #Function returns the champion(s) of the tournament
    return champ;

#This is the all-important function of this tool. The other functions create the bracket and progress through it.
#This one decides who wins each match. Editing this function will change what determines the winner of a given game.
#The default state chooses the winner by seed, randomly choosing an int between 0 and the sum of the two teams's seeds.
#The higher seed team's chance of winning is theoretically the losing team's seed over the sum, and vice versa
#I will explain in the function itself how to reformat this for alternative decision mechanisms
def compute(rd):
    #Create empty dictionary for teams in next round
    nextr = dict()
    #Create list of teams in current round
    teams = list(rd)
    #for the amount of teams in this round, pick every even team: 0,2,4,6,8
    for i in range(0, len(rd), 2):
        #1 Team
        t1 = teams[i]
        #Team they are facing, logically the next team over
        t2 = teams[i+1]
        #Edit code from here--------------------------------------
        #Find seeds of teams(or stats that determine winner)
        t1s = rd[t1]
        t2s = rd[t2]
        #Determine higher seed/lower seed's chance of winning
        adv = min(t1s, t2s)
        #Determine lower seed/higherseed's chance of winning
        und = max(t1s, t2s)
        #Find total of two seeds
        tot = t1s + t2s
        #Pick random integer between 1 and the total
        winner = random.randint(0, tot)
        #If winning number is less than the total minus the lower seed's chance of winning
        if winner < tot-adv:
            #Find out which team had the higher seed and put them into the next round with their seed
            if adv == t1s:
                nextr[t1] = t1s
            else:
                nextr[t2] = t2s
        #If winning number is greater than or equal to the total minus the lower seed's chance of winning
        else:
            #Find out which team had the lower seed and put them into the next round with their seed
            if und == t1s:
                nextr[t1] = t1s
            else:
                nextr[t2] = t2s
        #To here------------------------------------------------
    #After loop has finished iterating, the dict containing the next round's teams and their seeds is done and returned
    return nextr

#This absolute hellscape of a function generates a bracket from carefully built text, resizing for team name length.
#It took ages for me to find specific parts of the bracket when I needed to tweak them, so I came up with a solution
#I have labeled each line with codes referring to the elements in them, so if a line isnt working or needs to be changed
#You can locate the line with the specific element you want to change by CTRL+Fing and using the following code:
#Note: To find the champion section of the bracket, just CTRL+F Match Case "CHAMPION".
#Basic Structure: XXYZE: XX is the quarter of the bracket (NW,NE,SW,SE) being referred to
#Y is a number indicating the round (1-6) that the element is located in
#Z is index of that element within that round of its quarter of the bracket. (in descending order, 1 at the top)
#E is an element desriptor, which describes what element type is located there
#Element Descriptors: T = Team name slot, L = line beneath team name slot, M = Merger, any instance of a '|' symbol
#A round contains the team names, lines below them, and mergers directly ahead
#Examples: NW32T would be the 2nd team slot in the 3rd round of the Upper left part of the bracket
#SE112L would be the horizontal dotted line underneath the 12th team from the top in the 1st round of the bottom left
#NE23M is the third '|' character from the top in the 2nd rd of the northeast part of the bracket,directly next to NE31T
def bracket(rd1, rd2, rd3, rd4, rd5, rd6, rd7):
    #This controls the amount of spaces used for the box containing the champion the name has an odd # of letters
    spaces = math.ceil((18-len(rd7[0]))/2)
    #Top Line
    print('-' * 261)
    #NW11T NE11T
    print(f"{rd1[0]}{' ' * (20 - (len(rd1[0])))}" + (' ' * 221) + (' ' * (20 - (len(rd1[32])))) + rd1[32])
    #NW11L NE11L
    print(('-' * 21) + (' ' * 219) + ('-' * 21))
    #NW11M NW21T NE21T NE11M
    print((' ' * 20) + "| " + f"{rd2[0]}{' ' * (20 - (len(rd2[0])))}" + (' ' * 178) + (' ' * (19 - (len(rd2[16])))) + rd2[16] + " |")
    #NW21L NE21L
    print((' ' * 20) + ('-' * 21) + (' ' * 180) + ('-'*20))
    #NE12T NE12M NE21M NW21M NW12M NW12T
    print(f"{rd1[1]}{' ' * (20 - (len(rd1[1])))}" + "|" + (' ' * 20) + "|" + (' ' * 178) + "|" + (' ' * 19) + "|" + (' ' * (20 - (len(rd1[33])))) + rd1[33])
    print(('-' * 21) + (' ' * 20) + "|" + (' ' * 178) + "|" + (' ' * 19) + ('-' * 21))
    print((' ' * 41) + "| " + f"{rd3[0]}{' ' * (19 - (len(rd3[0])))}" + (' ' * 138) + (' ' * (19 - (len(rd3[8])))) + rd3[8] + " |")
    print((' ' * 41) + ('-' * 20) + (' ' * 140) + ('-' * 20))

    print(f"{rd1[2]}{' ' * (41 - (len(rd1[2])))}" + "|" + (' ' * 19) + "|" + (' ' * 138) + "|" + (' ' * 19) + "|" + (' ' * (40 - (len(rd1[34])))) + rd1[34])
    print(('-' * 21) + (' ' * 20) + "|" + (' ' * 19) + "|" + (' ' * 138) + "|" + (' ' * 19) + "|" + (' ' * 19) + ('-' * 21))
    print((' ' * 20) + "| " + f"{rd2[1]}{' ' * (19 - (len(rd2[1])))}" + "|" + (' ' * 19) + "|" + (' ' * 138) + "|" + (' ' * 19) + "|" + (' ' * (18 - (len(rd2[17])))) + rd2[17] + " |")
    print((' ' * 20) + ('-' * 21) + (' ' * 20) + "|" + (' ' * 138) + "|" + (' ' * 20) + ('-' * 20))
    print(f"{rd1[3]}{' ' * (20 - (len(rd1[3])))}" + "|" + (' ' * 40) + "|" + (' ' * 138) + "|" + (' ' * 39) + "|" + (' ' * (20 - (len(rd1[35])))) + rd1[35])
    print(('-' * 21) + (' ' * 40) + "|" + (' ' * 138) + "|" + (' ' * 39) + ('-' * 21))
    print((' ' * 61) + "| " + f"{rd4[0]}{' ' * (19 - (len(rd4[0])))}" + (' ' * 98) + (' ' * (19 - (len(rd4[4])))) + rd4[4] + " |")
    print((' ' * 61) + ('-' * 20) + (' ' * 100) + ('-' * 20))

    print(f"{rd1[4]}{' ' * (61 - (len(rd1[4])))}" "|" + (' ' * 19) + "|" + (' ' * 98) + "|" + (' ' * 19) + "|" + (' ' * (60 - (len(rd1[36])))) + rd1[36])
    print(('-' * 21) + (' ' * 40) + "|" + (' ' * 19) + "|" + (' ' * 98) + "|" + (' ' * 19) + "|" + (' ' * 39) + ('-' * 21))
    print((' ' * 20) + "| " + f"{rd2[2]}{' ' * (39 - (len(rd2[2])))}" + "|" + (' ' * 19) + "|" + (' ' * 98) + "|" + (' ' * 19) + "|" + (' ' * (38 - (len(rd2[18])))) + rd2[18] + " |")
    print((' ' * 20) + ('-' * 21) + (' ' * 20) + "|" + (' ' * 19) + "|" + (' ' * 98) + "|" + (' ' * 19) + "|" + (' ' * 20) + ('-' * 20))
    print(f"{rd1[5]}{' ' * (20 - (len(rd1[5])))}" + "|" + (' ' * 20) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 98) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * (20 - (len(rd1[37])))) + rd1[37])
    print(('-' * 21) + (' ' * 20) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 98) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 19) + ('-' * 21))
    print((' ' * 41) + "| " + f"{rd3[1]}{' ' * (18 - (len(rd3[1])))}" + "|" + (' ' * 19) + "|" + (' ' * 98) + "|" + (' ' * 19) + "|" + (' ' * (18 - (len(rd3[9])))) + rd3[9]+" |")
    print((' ' * 41) + ('-' * 20) + (' ' * 20) + "|" + (' ' * 98) + "|" + (' ' * 20) + ('-' * 20))
    print(f"{rd1[6]}{' ' * (41 - (len(rd1[6])))}" + "|" + (' ' * 39) + "|" + (' ' * 98) + "|" + (' ' * 19) + " " + (' ' * 19) + "|" + (' ' * (40 - (len(rd1[38])))) + rd1[38])
    print(('-' * 21) + (' ' * 20) + "|" + (' ' * 39) + "|" + (' ' * 98) + "|" + (' ' * 39) + "|" + (' ' * 19) + ('-' * 21))
    print((' ' * 20) + "| " + f"{rd2[3]}{' ' * (19 - (len(rd2[3])))}" + "|" + (' ' * 39) + "|" + (' ' * 98) + "|" + (' ' * 39) + "|" + (' ' * (18 - (len(rd2[19])))) + rd2[19] + " |")
    print((' ' * 20) + ('-' * 21) + (' ' * 40) + "|" + (' ' * 98) + "|" + (' ' * 40) + ('-' * 20)+(' ' * 20))
    print(f"{rd1[7]}{' ' * (20 - (len(rd1[7])))}" + "|" + (' ' * 60) + "|" + (' ' * 98) + "|" + (' ' * 59) + "|" + (' ' * (20 - (len(rd1[39])))) + rd1[39])
    print(('-' * 21) + (' ' * 60) + "|" + (' ' * 98) + "|" + (' ' * 59) + ('-' * 21))
    print((' ' * 81) + "| " + f"{rd5[0]}{' ' * (18 - (len(rd5[0])))}" + (' ' * 60) + (' ' * (18 - (len(rd5[2])))) + rd5[2] + " |")
    print((' ' * 81) + ('-' * 20) + (' ' * 60) + ('-' * 20))

    print(f"{rd1[8]}{' ' * (81- (len(rd1[8])))}" + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 60) + (' ' * (20 - (len(rd1[40])))) + rd1[40])
    print(('-' * 21) + (' ' * 60) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 59) + ('-' * 21))
    print((' ' * 20) + "| " + f"{rd2[4]}{' ' * (20 - (len(rd2[4])))}" + (' ' * 39) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 39) + (' ' * (19 - (len(rd2[20])))) + rd2[20] + " |")
    print((' ' * 20) + ('-' * 21) + (' ' * 40) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 40) + ('-' * 20))
    print(f"{rd1[9]}{' ' * (20 - (len(rd1[9])))}" + "|" + (' ' * 20) + "|" + (' ' * 39) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 39) + "|" + (' ' * 19) + "|" + (' ' * (20 - (len(rd1[41])))) + rd1[41])
    print(('-' * 21) + (' ' * 20) + "|" + (' ' * 39) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 39) + "|" + (' ' * 19) + ('-' * 21))
    print((' ' * 41) + "| " + f"{rd3[2]}{' ' * (38 - (len(rd3[2])))}" + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 19) + (' ' * (19 - (len(rd3[10])))) + rd3[10] + " |")
    print((' ' * 41) + ('-' * 20) + (' ' * 20) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 20) + ('-' * 20))

    print(f"{rd1[10]}{' ' * (41 - (len(rd1[10])))}" + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 19) + (' ' * (21 - (len(rd1[42])))) + rd1[42])
    print(('-' * 21) + (' ' * 20) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 19) + ('-' * 21))
    print((' ' * 20) + "| " + f"{rd2[5]}{' ' * (19 - (len(rd2[5])))}" + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * (18 - (len(rd2[21])))) + rd2[21] + " |")
    print((' ' * 20) + ('-' * 21) + (' ' * 20) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 20) + ('-' * 20))
    print(f"{rd1[11]}{' ' * (20 - (len(rd1[11])))}" + "|" + (' ' * 40) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 39) + "|" + (' ' * (20 - (len(rd1[43])))) + rd1[43])
    print(('-' * 21) + (' ' * 40) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 39) + ('-' * 21))
    print((' ' * 61) + "| " + f"{rd4[1]}{' ' * (18 - (len(rd4[1])))}" + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * (18 - (len(rd4[5])))) + rd4[5] + " |")
    print((' ' * 61) + ('-' * 20) + (' ' * 20) + "|" + (' ' * 58) + "|" + (' ' * 20) + ('-' * 20))

    print(f"{rd1[12]}{' ' * (61 - (len(rd1[12])))}" "|" + (' ' * 39) + "|" + (' ' * 58) + "|" + (' ' * 39) + "|" + (' ' * 39) + (' ' * (21 - (len(rd1[44])))) + rd1[44])
    print(('-' * 21) + (' ' * 40) + "|" + (' ' * 39) + "|" + (' ' * 58) + "|" + (' ' * 39) + "|" + (' ' * 39) + ('-' * 21))
    print((' ' * 20) + "| " + f"{rd2[6]}{' ' * (39 - (len(rd2[6])))}" + "|" + (' ' * 39) + "|" + (' ' * 58) + "|" + (' ' * 39) + "|" + (' ' * 19) + (' ' * (19 - (len(rd2[22])))) + rd2[22] + " |")
    print((' ' * 20) + ('-' * 21) + (' ' * 20) + "|" + (' ' * 39) + "|" + (' ' * 58) + "|" + (' ' * 39) + "|" + (' ' * 20) + ('-' * 20))
    print(f"{rd1[13]}{' ' * (20 - (len(rd1[13])))}" + "|" + (' ' * 20) + "|" + (' ' * 19) + "|" + (' ' * 39) + "|" + (' ' * 58) + "|" + (' ' * 39) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * (20 - (len(rd1[45])))) + rd1[45])
    print(('-' * 21) + (' ' * 20) + "|" + (' ' * 19) + "|" + (' ' * 39) + "|" + (' ' * 58) + "|" + (' ' * 39) + "|" + (' ' * 19) + "|" + (' ' * 19) + ('-' * 21))
    print((' ' * 41) + "| " + f"{rd3[3]}{' ' * (18 - (len(rd3[3])))}" + "|" + (' ' * 39) + "|" + (' ' * 58) + "|" + (' ' * 39) + "|" + (' ' * (18 - (len(rd3[11])))) + rd3[11] + " |")
    print((' ' * 41) + ('-' * 20) + (' ' * 40) + "|" + (' ' * 58) + "|" + (' ' * 40) + ('-' * 20))
    print(f"{rd1[14]}{' ' * (41 - (len(rd1[14])))}" + "|" + (' ' * 59) + "|" + (' ' * 58) + "|" + (' ' * 59) + "|" + (' ' * 20) + (' ' * (20 - (len(rd1[46])))) + rd1[46])
    print(('-' * 21) + (' ' * 20) + "|" + (' ' * 59) + "|" + (' ' * 58) + "|" + (' ' * 59) + "|" + (' ' * 19) + ('-' * 21))
    print((' ' * 20) + "| " + f"{rd2[7]}{' ' * (19 - (len(rd2[7])))}" + "|" + (' ' * 59) + "|" + (' ' * 58) + "|" + (' ' * 59) + "|" + (' ' * (18 - (len(rd2[23])))) + rd2[23] + " |")
    print((' ' * 20) + ('-' * 21) + (' ' * 60) + "|" + (' ' * 58) + "|" + (' ' * 60) + ('-' * 20))
    print(f"{rd1[15]}{' ' * (20 - (len(rd1[15])))}" + "|" + (' ' * 80) + "|" + (' ' * 58) + "|" + (' ' * 79) + "|" + (' ' * (20 - (len(rd1[47])))) + rd1[47])
    print(('-' * 21) + (' ' * 80) + "|" + (' ' * 20) + ('_' * 18) + (' ' * 20) + "|" + (' ' * 79) + ('-' * 21))
    print((' ' * 101) + "| " + f"{rd6[0]}{' ' * (18 - (len(rd6[0])))}" + "|" + (' ' * 5) + "CHAMPION" + (' ' * 5) + "|" + (' ' * (18 - (len(rd6[1])))) + rd6[1] + " |")
    print((' ' * 101) + ('-' * 20) + " " + (' ' * spaces) + rd7[0] + (' ' * spaces) + " " + ('-' * 20))
    print(f"{rd1[16]}{' ' * (110 - (len(rd1[4])))}" + "|" + (' ' * 19) + "|" + ('_' * 18) + "|" + (' ' * 19) + "|" + (' ' * (100 - (len(rd1[48])))) + rd1[48])
    print(('-' * 21) + (' ' * 80) + "|" + (' ' * 58) + "|" + (' ' * 79) + ('-' * 21))
    print((' ' * 20) + "| " + f"{rd2[8]}{' ' * (79 - (len(rd2[8])))}" + "|" + (' ' * 58) + "|" + (' ' * (78 - (len(rd2[24])))) + rd2[24] + " |")
    print((' ' * 20) + ('-' * 21) + (' ' * 60) + "|" + (' ' * 58) + "|" + (' ' * 60) + ('-' * 20))
    print(f"{rd1[17]}{' ' * (20 - (len(rd1[17])))}" + "|" + (' ' * 20) + "|" + (' ' * 59) + "|" + (' ' * 58) + "|" + (' ' * 59) + "|" + (' ' * 19) + "|" + (' ' * (20 - (len(rd1[49])))) + rd1[49])
    print(('-' * 21) + (' ' * 20) + "|" + (' ' * 59) + "|" + (' ' * 58) + "|" + (' ' * 59) + "|" + (' ' * 19) + ('-' * 21))
    print((' ' * 41) + "| " + f"{rd3[4]}{' ' * (18 - (len(rd3[4])))}" + (' ' * 40) + "|" + (' ' * 58) + "|" + (' ' * 40) + (' ' * (18 - (len(rd3[12])))) + rd3[12] + " |")
    print((' ' * 41) + ('-' * 20) + (' ' * 40) + "|" + (' ' * 58) + "|" + (' ' * 40) + ('-' * 20))

    print(f"{rd1[18]}{' ' * (41 - (len(rd1[18])))}" + "|" + (' ' * 19) + "|" + (' ' * 39) + "|" + (' ' * 58) + "|" + (' ' * 39) + "|" + (' ' * 19) + "|" + (' ' * 20) + (' ' * (20 - (len(rd1[50])))) + rd1[50])
    print(('-' * 21) + (' ' * 20) + "|" + (' ' * 19) + "|" + (' ' * 39) + "|" + (' ' * 58) + "|" + (' ' * 39) + "|" + (' ' * 19) + "|" + (' ' * 19) + ('-' * 21))
    print((' ' * 20) + "| " + f"{rd2[9]}{' ' * (19 - (len(rd2[9])))}" + "|" + (' ' * 19) + "|" + (' ' * 39) + "|" + (' ' * 58) + "|" + (' ' * 39) + "|" + (' ' * 19) + "|" + (' ' * (18 - (len(rd2[25])))) + rd2[25] + " |")
    print((' ' * 20) + ('-' * 21) + (' ' * 20) + "|" + (' ' * 39) + "|" + (' ' * 58) + "|" + (' ' * 39) + "|" + (' ' * 20) + ('-' * 20))
    print(f"{rd1[19]}{' ' * (20 - (len(rd1[19])))}" + "|" + (' ' * 40) + "|" + (' ' * 39) + "|" + (' ' * 58) + "|" + (' ' * 39) + "|" + (' ' * 39) + "|" + (' ' * (20 - (len(rd1[51])))) + rd1[51])
    print(('-' * 21) + (' ' * 40) + "|" + (' ' * 39) + "|" + (' ' * 58) + "|" + (' ' * 39) + "|" + (' ' * 39) + ('-' * 21))
    print((' ' * 61) + "| " + f"{rd4[2]}{' ' * (19 - (len(rd4[2])))}" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + (' ' * (19 - (len(rd4[6])))) + rd4[6] + " |")
    print((' ' * 61) + ('-' * 20) + (' ' * 20) + "|" + (' ' * 58) + "|" + (' ' * 20) + ('-' * 20))

    print(f"{rd1[20]}{' ' * (61 - (len(rd1[20])))}" "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 39) + (' ' * (21 - (len(rd1[52])))) + rd1[52])
    print(('-' * 21) + (' ' * 40) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 39) + ('-' * 21))
    print((' ' * 20) + "| " + f"{rd2[10]}{' ' * (39 - (len(rd2[10])))}" + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 19) + (' ' * (19 - (len(rd2[26])))) + rd2[26] + " |")
    print((' ' * 20) + ('-' * 21) + (' ' * 20) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 20) + ('-' * 20))
    print(f"{rd1[21]}{' ' * (20 - (len(rd1[21])))}" + "|" + (' ' * 20) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * (20 - (len(rd1[53])))) + rd1[53])
    print(('-' * 21) + (' ' * 20) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 19) + ('-' * 21))
    print((' ' * 41) + "| " + f"{rd3[5]}{' ' * (18 - (len(rd3[5])))}" + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * (18 - (len(rd3[13])))) + rd3[13] + " |")
    print((' ' * 41) + ('-' * 20) + (' ' * 20) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 20) + ('-' * 20))
    print(f"{rd1[22]}{' ' * (41 - (len(rd1[22])))}" + "|" + (' ' * 39) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 39) + "|" + (' ' * 19 + (' ' * (21 - (len(rd1[54])))) + rd1[54]))
    print(('-' * 21) + (' ' * 20) + "|" + (' ' * 39) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 39) + "|" + (' ' * 19) + ('-' * 21))
    print((' ' * 20) + "| " + f"{rd2[11]}{' ' * (19 - (len(rd2[11])))}" + "|" + (' ' * 39) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 39) + "|" + (' ' * (18 - (len(rd2[27])))) + rd2[27] + " |")
    print((' ' * 20) + ('-' * 21) + (' ' * 40) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 40) + ('-' * 20))
    print(f"{rd1[23]}{' ' * (20 - (len(rd1[23])))}" + "|" + (' ' * 60) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 59) + "|" + (' ' * (20 - (len(rd1[55])))) + rd1[55])
    print(('-' * 21) + (' ' * 60) + "|" + (' ' * 19) + "|" + (' ' * 58) + "|" + (' ' * 19) + "|" + (' ' * 59) + ('-' * 21))
    print((' ' * 81) + "| " + f"{rd5[1]}{' ' * (18 - (len(rd5[1])))}" + "|" + (' ' * 58) + "|" + (' ' * (18 - (len(rd5[3])))) + rd5[3] + " |")
    print((' ' * 81) + ('-' * 20) + (' ' * 60) + ('-' * 20))

    print(f"{rd1[24]}{' ' * (81 - (len(rd1[24])))}" + "|" + (' ' * 98) + "|" + (' ' * 59) + (' ' * (21 - (len(rd1[56])))) + rd1[56])
    print(('-' * 21) + (' ' * 60) + "|" + (' ' * 98) + "|" + (' ' * 59) + ('-' * 21))
    print((' ' * 20) + "| " + f"{rd2[12]}{' ' * (20 - (len(rd2[12])))}" + (' ' * 39) + "|" + (' ' * 98) + "|" + (' ' * 39) + (' ' * (19 - (len(rd2[28])))) + rd2[28] + " |")
    print((' ' * 20) + ('-' * 21) + (' ' * 40) + "|" + (' ' * 98) + "|" + (' ' * 40) + ('-' * 20))
    print(f"{rd1[25]}{' ' * (20 - (len(rd1[25])))}" + "|" + (' ' * 20) + "|" + (' ' * 39) + "|" + (' ' * 98) + "|" + (' ' * 39) + "|" + (' ' * 19) + "|" + (' ' * (20 - (len(rd1[57])))) + rd1[57])
    print(('-' * 21) + (' ' * 20) + "|" + (' ' * 39) + "|" + (' ' * 98) + "|" + (' ' * 39) + "|" + (' ' * 19) + ('-' * 21))
    print((' ' * 41) + "| " + f"{rd3[6]}{' ' * (38 - (len(rd3[6])))}" + "|" + (' ' * 98) + "|" + (' ' * 19) + (' ' * (19 - (len(rd3[14])))) + rd3[14] + " |")
    print((' ' * 41) + ('-' * 20) + (' ' * 20) + "|" + (' ' * 98) + "|" + (' ' * 20) + ('-' * 20))

    print(f"{rd1[26]}{' ' * (41 - (len(rd1[26])))}" + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 98) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 19) + (' ' * (21 - (len(rd1[58])))) + rd1[58])
    print(('-' * 21) + (' ' * 20) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 98) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 19) + ('-' * 21))
    print((' ' * 20) + "| " + f"{rd2[13]}{' ' * (19 - (len(rd2[13])))}" + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * 98) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * (18 - (len(rd2[29])))) + rd2[29] + " |")
    print((' ' * 20) + ('-' * 21) + (' ' * 20) + "|" + (' ' * 19) + "|" + (' ' * 98) + "|" + (' ' * 19) + "|" + (' ' * 20) + ('-' * 20))
    print(f"{rd1[27]}{' ' * (20 - (len(rd1[27])))}" + "|" + (' ' * 40) + "|" + (' ' * 19) + "|" + (' ' * 98) + "|" + (' ' * 19) + "|" + (' ' * 39) + "|" + (' ' * (20 - (len(rd1[59])))) + rd1[59])
    print(('-' * 21) + (' ' * 40) + "|" + (' ' * 19) + "|" + (' ' * 98) + "|" + (' ' * 19) + "|" + (' ' * 39) + ('-' * 21))
    print((' ' * 61) + "| " + f"{rd4[3]}{' ' * (18 - (len(rd4[3])))}" + "|" + (' ' * 98) + "|" + (' ' * (18 - (len(rd4[7])))) + rd4[7] + " |")
    print((' ' * 61) + ('-' * 20) + (' ' * 100) + ('-' * 20))

    print(f"{rd1[28]}{' ' * (61 - (len(rd1[28])))}" "|" + (' ' * 138) + "|" + (' ' * 39) + (' ' * (21 - (len(rd1[60])))) + rd1[60])
    print(('-' * 21) + (' ' * 40) + "|" + (' ' * 138) + "|" + (' ' * 39) + ('-' * 21))
    print((' ' * 20) + "| " + f"{rd2[14]}{' ' * (39 - (len(rd2[14])))}" + "|" + (' ' * 138) + "|" + (' ' * 19) + (' ' * (19 - (len(rd2[30])))) + rd2[30] + " |")
    print((' ' * 20) + ('-' * 21) + (' ' * 20) + "|" + (' ' * 138) + "|" + (' ' * 20) + ('-' * 20))
    print(f"{rd1[29]}{' ' * (20 - (len(rd1[29])))}" + "|" + (' ' * 20) + "|" + (' ' * 19) + "|" + (' ' * 138) + "|" + (' ' * 19) + "|" + (' ' * 19) + "|" + (' ' * (20 - (len(rd1[61])))) + rd1[61])
    print(('-' * 21) + (' ' * 20) + "|" + (' ' * 19) + "|" + (' ' * 138) + "|" + (' ' * 19) + "|" + (' ' * 19) + ('-' * 21))
    print((' ' * 41) + "| " + f"{rd3[7]}{' ' * (18 - (len(rd3[7])))}" + "|" + (' ' * 138) + "|" + (' ' * (18 - (len(rd3[15])))) + rd3[15] + " |")
    print((' ' * 41) + ('-' * 20) + (' ' * 140) + ('-' * 20))
    print(f"{rd1[30]}{' ' * (41 - (len(rd1[30])))}" + "|" + (' ' * 178) + "|" + (' ' * 20) + (' ' * (20 - (len(rd1[62])))) + rd1[62])
    print(('-' * 21) + (' ' * 20) + "|" + (' ' * 178) + "|" + (' ' * 19) + ('-' * 21))
    print((' ' * 20) + "| " + f"{rd2[15]}{' ' * (19 - (len(rd2[15])))}" + "|" + (' ' * 178) + "|" + (' ' * (18 - (len(rd2[31])))) + rd2[31] + " |")
    print((' ' * 20) + ('-' * 21) + (' ' * 180) + ('-' * 20))
    print(f"{rd1[31]}{' ' * (20 - (len(rd1[31])))}" + "|" + (' ' * 219) + "|" + (' ' * (20 - (len(rd1[63])))) + rd1[63])
    print(('-' * 21) + (' ' * 219) + ('-' * 21))
    print('-' * 261)
#This code is for generating multiple brackets at once. If you plan on copying these brackets to a txt file
#I recommend you only create ~25 brackets at a time, some ides cut off the top when there is too much text printed
listchamps =[]
i = 1
while i <= 25:
    #generate returns the champion, so you're appending the champion to listchamps
    listchamps.append(generate(r1))
    i+=1
print("CHAMPIONS")
print(listchamps)



