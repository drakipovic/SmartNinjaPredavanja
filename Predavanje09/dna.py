f = open('dna.txt', 'r')
dna = f.read()

black_hair = "CCAGCAATCGC"
brown_hair = "GCCAGTGCCG"
blonde_hair = "TTAGCTATCGC"

has_black_hair = black_hair in dna
has_brown_hair = brown_hair in dna
has_blonde_hair = blonde_hair in dna

square_face = "GCCACGG"
round_face = "ACCACAA"
oval_face = "AGGCCTCA"

has_square_face = square_face in dna
has_round_face = round_face in dna
has_oval_face = oval_face in dna

blue_eyes = "TTGTGGTGGC"
green_eyes = "GGGAGGTGGC"
brown_eyes = "AAGTAGTGAC"

has_blue_eyes = blue_eyes in dna
has_green_eyes = green_eyes in dna
has_brown_eyes = brown_eyes in dna

female = "TGAAGGACCTTC"
male = "TGCAGGAACTTC"

is_female = female in dna
is_male = male in dna

white_race = "AAAACCTCA"
black_race = "CGACTACAG"
yellow_race = "CGCGGGCCG"

is_white = white_race in dna
is_black = black_race in dna
is_yellow = yellow_race in dna


#eva
if is_female and is_white and has_blonde_hair and has_blue_eyes and has_oval_face:
    print "Eva ate ice-cream"

#larisa
if is_female and is_white and has_brown_hair and has_brown_eyes and has_oval_face:
    print "Larisa ate ice-cream"

#matej
if is_male and is_white and has_black_hair and has_blue_eyes and has_oval_face:
    print "Matej ate ice-cream"

#miha
if is_male and is_white and has_brown_hair and has_green_eyes and has_square_face:
    print "Miha ate ice-cream"