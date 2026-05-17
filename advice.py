def advcie_generator(score):

    if score >= 0 and score <=100:

        if score >= 85:
            print("* Advice: try advanced exercises to challenge yourself and improve further")
        
        if score >= 70 and score <= 84:
            print("* Advice: review your small mistakes and practice more to improve your score")
        
        if score >= 50 and score <= 69:
            print("* Advice: you passed, but you need more practice to improve")

        if score < 50:
            print("* Advice: you need support and should review the basics")
