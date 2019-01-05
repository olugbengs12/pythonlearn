name = input("Enter file:")
fhandle = open(name)
words = list()

for line in fhandle:
    if not line.startswith("From:") :
         continue
    line = line.split()
    words.append(line[1])

counts = dict()
for word in words:
     counts[word] = counts.get(word, 0) + 1


maxval = None
maxkey = None
for word in counts:
    value = counts[word]
    if maxval == None or value > maxval:
          maxval = value
          maxkey = word

print (maxkey, maxval)
