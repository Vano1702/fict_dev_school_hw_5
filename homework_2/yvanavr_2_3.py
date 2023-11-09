# A function to group the words in anagrams
def groupAnagrams(words):
    grouped = [[words.pop(0)]]
    for word in words:
        flag = 1
        for group in grouped:
            if sorted(word)==sorted(group[0]):
                group.append(word)
                flag = 0
                break
        if flag:
            grouped.append([word])
    return grouped

a = ["tsar", "rat", "tar", "star", "tars", "cheese"]
print(groupAnagrams(a))
