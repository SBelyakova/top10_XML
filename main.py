def count_top10_xml():
  import xml.etree.ElementTree as ET
  parser = ET.XMLParser(encoding="utf-8")
  tree = ET.parse("files/newsafr.xml", parser)
  root = tree.getroot()

  news_list = []
  unique_word =[]
  counts = []

  items = root.findall("channel/item")
  for item in items:
    news_list.append(item.find("description").text)


  for string in news_list:
    uniques = string.split(' ')
    for word in uniques:
      if len(word) > 6:
        unique_word.append(word)      
    
  for words in unique_word:
    count = 0
    for word in unique_word:
      if word == words:
        count += 1
    if (count, words) not in counts:
        counts.append((count, words))

    counts.sort()
    counts.reverse()

  for i in range (0, 10):
    count, word = counts[i]
    print(f'на {i+1} месте: слово \"{word}\", встречается {count} раз(а)')
  return

count_top10_xml()  