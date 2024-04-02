# Go to String below and if the length of a word is even print "even!".
# st = 'I love doing python programming in spyder'
st = 'I love doing python programming in spyder'
words = st.split()
for word in words:
    if len(word) % 2 == 0:
        print(f"{word} is even!")

        


