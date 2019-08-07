from collections import Counter

colors = ['red', 'blue', 'yellow', 'blue', 'red', 'blue']
counter = Counter(colors)
print(counter)

sorted_counter = counter.most_common()
print("most word:",sorted_counter[0])