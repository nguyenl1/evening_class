# ari = (4.71) * (characters/words) + (0.5) * (words/sentences) - 21.43

# round(ari)
# use regular expressions

read it in
strip out punc and spaces
count number of chars 
remove punc
count number of words 
count sentence (maybe count periods)


get number of characters
get number of words
get number of sentences 

try:
    f = open("./lab22.txt")
    contents = f.read()
    print(contents)
except (IOError, OSError) as e:
    print(e)
finally:
    f.close()

ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}


print(f"The ARI for gettysburg-affress.txt is {12} 'n\ This corresponds to a {11th Grade} level of difficulty 'n\ that is suitable for an average person {16-17} years old")