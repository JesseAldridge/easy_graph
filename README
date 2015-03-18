
`sudo pip install easygraph`

-------------------------------

# Example 1:  Simple bar graph.

days = []
for i in range(10):
  days.append(datetime.date.today() + datetime.timedelta(days=i))
graph(zip(days, range(len(days))), show_bars=True)

# Example 2:  Multiple lists in one graph, with a tooltip for each point.

l1 = [(0,0), (1,1), (2,2), (3,3)]
l2 = [(0,0), (1,1), (2,4), (3,9)]
labels = ['foo', 'bar', 'baz', 'yep']
graph([l1, l2], show_lines=True, xaxis='x', yaxis='y', labels=labels)
