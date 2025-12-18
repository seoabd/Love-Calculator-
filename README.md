# Love-Calculator-

Love Calculator
💪 This is a difficult challenge! 💪 
You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 
1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
2. Then check for the number of times the letters in the word LOVE occurs.   
3. Then combine these numbers to make a 2 digit number and print it out. 
e.g.
name1 = "Sead Abduli" name2 = "Tatjana Mirkovska"
T occurs 2 times 
R occurs 1 time 
U occurs 1 times 
E occurs 1 times 
Total = 5 
L occurs 1 time 
O occurs 1 times 
V occurs 1 times 
E occurs 1 times 
Total = 4 

Love Score = 54


Example Input 
calculate_love_score("Kanye West", "Kim Kardashian")
Example Output
42


How to test your code and see your output?

Udemy coding exercises do not have a console, so you cannot use the input() function. You will need to call your function with hard-coded values like so:

def calculate_love_score(name1, name2):
  # your code here
 
# Call your function with hard coded values
calculate_love_score("Kanye West", "Kim Kardashian")
