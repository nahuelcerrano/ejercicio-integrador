def maxNumberOfWords(str):
  counts = dict()
  words = str.split()

  for word in words:
    if word in counts:
      counts[word] += 1
    else:
      counts[word] = 1

  maxCount = max(counts.values())
  maxWord = max(counts)

  maxCount = (maxWord, maxCount)
  
  return maxCount

print(maxNumberOfWords('Lorem ipsum dolor sit amet sit amet adipiscing amet sem neque sed ipsum'))