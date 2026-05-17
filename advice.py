def advcie_generator(score):

    if score >= 0 and score <=100:

        if score >= 85:
            return"* Advice: try advanced exercises to challenge yourself and improve further"
        
        if score >= 70 and score <= 84:
            return "* Advice: review your small mistakes and practice more to improve your score"
        
        if score >= 50 and score <= 69:
            return "* Advice: you passed, but you need more practice to improve"

        if score < 50:
            return "* Advice: you need support and should review the basics"
