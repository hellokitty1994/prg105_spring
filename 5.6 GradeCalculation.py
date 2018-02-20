# write a program that ask users to enter five test scores. You will need to create five variable to hold
# these scores.
def calc_avarage(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score) / 5
    return average
   def determine_grade(user_score):
       if(user_score < 60):
           return "F"
       elif ( user_score < 70):
           return  "D"
       elif (user_score < 80):
           return "C"
       elif (user_score < 90):
           return "B"
       elif (user_score  <100):
           return "A"
def asking_scores():
    score1 = float (input("Enter score 1 "))
    score2 = float (input("Enter score 2 "))
    score3 = float (input("Enter score 3 "))
    score4 = float (input("Enter score 4 "))
    score5 = float (input("Enter score 5 "))
    return  score1, score2, score3, score4, score5
def print_table_of_results (score1, score2, score3, score4, score5):
    print("score\tletter grade")
    print( str (score1) + "\t\t" + determine_grade(score1), \
           str (score2) + "\t\t" + determine_grade(score2), \
           str (score3) + "\t\t" + determine_grade(score3), \
           str (score4) + "\t\t" + determine_grade(score4), \
           str (score5) + "\t\t" + determine_grade(score5),  sep= "\n"")
def main ():
    score1, score2, score3, score4, score5 = asking_scores()
    print_table_of_results( score1, score2, score3, score4, score5)
main()

