# Cat, Monkey, and Banana
# Common Attributes:
# - Cats and monkeys are both mammals and are often domesticated or kept as pets.
# - Bananas are a common food source for both animals, especially monkeys.

# Behavioral Similarities:
# - Cats and monkeys exhibit playful behaviors, although the context may differ.
# - Both cats and monkeys have unique communication methods and social structures.

# Laptop, Phone, and TV
# Functional Similarities:
# - All three devices are electronic and serve as communication or entertainment tools.
# - They often share functionalities, such as internet access, media playback, and applications.

# Design Trends:
# - Each device has evolved to become more user-friendly with touchscreens and high-definition displays.

import spacy  # importing spacy

nlp = spacy.load('en_core_web_md')  


complaints = [
    'We bought a house in CA. Our mortgage was handled by a company called ki. Soon after the mortgage was sold to ABC. Shortly after that XYZ took over the mortgage. The other day we got a notice not to send our payment to them but to loi instead. This is all so frustrating and wreaks of the mortgage nightmare.',
    'I got approved for a loan to buy a house I have submitted everything I need to for them I paid for the inspection and paid good faith check after all of that they said I did not get approved for the loan to cancel my contract because they do not want to wait for the down payments assistant said that the Sellers do not want to wait that long I feel like they are getting over on me I feel that they should have told me that I did not get approved before I spent my money and picked out a house Carrington mortgage in Ohio.',
    'As per the correspondence, I received from : The University This is to inform you that I have recently pulled my credit report and noticed that there is a collection listing from The University on my credit report. I WAS never notified of this collection action or that I owed the debt. This letter is to inform you that I would like a verification of the debt and juilo ability to collect this money from me.',
    'I am writing to dispute the follow information in my file.ON BOTH TransUnion & . for {$15000.00}. I have contacted this agency to advise to STOP CALLING ME this case was dismissed in court 2014. Please see the attached document from County State Court. Thanking you in advanced regarding this matter.',
    'I have not had a XXXX phone since early 2007. I have tried to resolve my bill in the past but it keeps reposting an old bill. I have no way to provide financial info from 8 years ago and they know that so they want me to prove it to them but I have no way to do that. Is there anyway to get to find out how old it is.',
    'I posted dated a check and mailed it for 2015 for my mortgage payment as my mortgage company will only take online payments if all the late charges are paid at once (also illegal), and the check was cashed on 2015 which cost me over {$70.00} in over draft fees with my bank.'
]


print("-------------Complaints similarity---------------")
for token in complaints:
    token = nlp(token)
    for token_ in complaints:
        token_ = nlp(token_)
        print(token.similarity(token_))


recipes = [
    'Bake in the preheated oven, stirring every 20 minutes, until sugar mixture has baked and caramelized onto popcorn and cashews, about 1 hour. Spread cashew caramel corn onto a parchment paper-lined baking sheet to cool. If desired, form into balls while still warm.',
    'Combine brown sugar, corn syrup, butter, salt, and cream of tartar in a large saucepan. Bring to a boil, stirring constantly, until a candy thermometer inserted into the middle of the syrup, not touching the bottom, reads 260 degrees F (127 degrees C), 6 to 8 minutes.',
    'Lift marshmallow fudge out of the pan by the edges of the foil and place on a large cutting board. Dip a large knife in the remaining confectioners\' sugar and slice fudge into 1 1/2-inch squares, continually dipping knife in the sugar after each slice.',
    'Melt butter in a medium saucepan over medium heat; stir in condensed milk. Pour in chocolate chips; cook and stir until melted, 5 to 10 minutes.',
    'Lightly grease a cookie sheet. Deflate the dough and turn it out onto a lightly floured surface. Roll the marzipan into a rope and place it in the center of the dough. Fold the dough over to cover it; pinch the seams together to seal. Place the loaf, seam side down, on the prepared baking sheet. Cover with a damp cloth and let rise until doubled in volume, about 40 minutes. Meanwhile, preheat oven to 350 degrees F (175 degrees C)',
    'In a large bowl, cream together the butter, brown sugar, and white sugar. Beat in the instant pudding mix until blended. Stir in the eggs and vanilla. Blend in the flour mixture. Finally, stir in the chocolate chips and nuts. Drop cookies by rounded spoonfuls onto ungreased cookie sheets.'
]


print("-------------Recipes similarity---------------")
for token in recipes:
    token = nlp(token)
    for token_ in recipes:
        token_ = nlp(token_)
        print(token.similarity(token_))


print("-------------Recipes vs Complaints similarity---------------")
for token in recipes:
    token = nlp(token)
    for token_ in complaints:
        token_ = nlp(token_)
        print(token.similarity(token_))

# Because of its broader vocabulary and contextual embeddings, 
# en_core_web_md usually yields higher and more consistent similarity scores 
# when conducting similarity comparisons. In contrast, 
# because en_core_web_sm lacks comprehensive embeddings for a large number of 
# words and phrases, it may produce lower scores or less nuanced comparisons.

