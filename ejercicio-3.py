def countEachWord(str):
  counts = dict()
  words = str.split()

  for word in words:
    if word in counts:
      counts[word] += 1
    else:
      counts[word] = 1
  return counts

print(countEachWord('Lorem ipsum dolor sit amet sit amet adipiscing amet sem neque sed ipsum'))