message = input("> ")
words =message.split(" ")
print(words)
emojis ={
    #" :)" : "\U0001F600",
     #":(": "\U0001F603",
    ":)" : " 😊 🤣 ",
    ":(" : "❤"
}
output =""
for word in words:
    output += emojis.get(word ,word)+ " "

print(output)