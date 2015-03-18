
`sudo pip install easygraph`

-------------------------------

    import easygraph

    # Example 1:  Simple bar graph.

    easygraph.graph([(0,0), (1,1), (2,4)], show_bars=True)

    # Example 2:  Works with dates.  Can label axes and draw linear regression.

    import datetime, random

    days = [datetime.date.today() + datetime.timedelta(days=i) for i in range(10)]
    values = [i + 2 - random.random() * 4 for i in range(10)]
    easygraph.graph(
      zip(days, values), show_bars=True, xaxis='Day', yaxis='Values',
      draw_regression=True)

    # Example 2:  Multiple lists in one graph, with a tooltip for each point.

    l1 = [(0,0), (1,1), (2,2), (3,3)]
    l2 = [(0,0), (1,1), (2,4), (3,9)]
    labels = ['foo', 'bar', 'baz', 'yep']
    easygraph.graph([l1, l2], labels=labels, show_lines=True)
