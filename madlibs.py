# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to_________"
# youtuber = "krishna panjiyar" # some string variable


# a few days to do this
# print("subscribe to " + youtuber)
# print("subsribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjectives: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)