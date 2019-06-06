def main():
    answer_list = ["A", "C", "A", "A", "D", "B",
                     "C", "A", "C", "B", "A", "D",
                     "C", "A", "D", "C", "B", "B",
                     "D", "A"]
    user_ans_list = []
    corr_count = 0
    incorr_count = 0
    questions = 20

    infile = open('Untitled.txt', 'r')

    user_ans_list = infile.readlines()

    infile.close()

    index = 0

    print("Q\tocrr\tYour\tStatus")
    print("#\tAnswer\tAnswer\n--------------------------")

    while index < 20:
        print(str(index+1) + "\t" + answer_list[index] + "\t" + user_ans_list[index], end="\t")
        if user_ans_list[index] == corr_ans_list[index]:
            corr_count += 1
            print("Correct")
        else:
            incorr_count += 1
            index += 1
            print("Wrong")

    percent_corr = (corr_count/num_questions) * 100
    percent_corr_fmt = format(percent_corr, ".1f")
    print("Grade : ", corr_count , "/", num_questions, " = ",
          percent_corr_fmt, sep="")

    if percent_corr >= 75:
        print("Congratulations!! You passed the exam")
    else:
        print("Sorry, you did not pass the exam")


main()
