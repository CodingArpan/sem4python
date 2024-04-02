# Create a program that will print out words that start with 's' from the below given
# statement.
# st='Print only the words that start with s in this sentence'

st = 'Print only the words that start with s in this sentence'
words = st.split()
for word in words:
    if word[0].lower() == 's':
        print(word)