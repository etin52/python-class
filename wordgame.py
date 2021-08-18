print("welcome to word game")
print("""
The rules of the Game:
1.Try to guess a word in our system 
2.Upon getting a word correctly you get 5 points
3.If your word appears n times you get n*5 points 

May the best guess win!

""")

my_random_words="""Today we present you the list of 100 random words in 
English and we’ll also give you their meanings. Keep a count of words to see how many of them you know.

Have you ever thought, what it would be like to know words 
you’ve never thought you would know? Well if not, or if just now, 
then voila! You just turned to a right piece, that’ll help you know
 hundred random words, well why right? However,  you can answer this better,being someone who’s devoting their precious time into learning and growing.
   For the sake of an answer,  I’d say to have a rich vocabulary is a great 
   thing if you’re into an academic course, that requires you to be creative with the choice of your words, or professionally to leave a moving impact on your readers, or maybe to maintain a journal with Galaxy of words, for your own happiness.

Sledging deeper, I would like you and I, to know some words 
we already knew and some we never. So let’s get learning.

""".lower()
user_input=input("Enter a word\n").lower()

print(my_random_words.count(user_input))
word_occurrence=my_random_words.count(user_input)
score=word_occurrence*5
print(F"your score ia {score}")





