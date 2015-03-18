import random, os, json, atexit, datetime, urllib2

# Download static site files if necessary.

easy_graph_path = os.path.expanduser('~/easygraph')
if not os.path.exists(easy_graph_path):
  os.mkdir(easy_graph_path)

for filename in ('jquery.flot.axislabels.js', 'render_output.html'):
  path = os.path.join(easy_graph_path, filename)
  if os.path.exists(path):
    continue

  response = urllib2.urlopen(
    'https://raw.githubusercontent.com/JesseAldridge/easy_graph/master/easygraph/' +
    filename)
  with open(path, 'w') as f:
    print 'downloading:', path
    f.write(response.read())

# Accumulate output items in global list.

class g:
  out_items = []
  registered = False

# Can write raw html between graphs.

def html(html):
  g.out_items.append({'html':html})

# Graph a list of (x,y) points -- either a single series or a list of series.

def graph(points, **kw):
  if not g.registered:
    atexit.register(dump_output)
  g.registered = True
  multi_series = False
  for list_ in points:
    if list_ and any(isinstance(list_[0], type_) for type_ in (list, tuple)):
      multi_series = True
      break

  if not multi_series:
    points = [points]
  kw['points'] = points
  g.out_items.append(kw)

# At exit, dump all the data items into a single json file and open render_output.html.

def path(rel_path):
  return os.path.join(easy_graph_path, rel_path)

def dump_output():
  def dt_handler(obj):
      return obj.isoformat() if hasattr(obj, 'isoformat') else None

  json_str = json.dumps(g.out_items[::-1], indent=2, default=dt_handler)
  with open(path('out_data.js'), 'w') as f:
    f.write('var out_data = ' + json_str)
  os.system('open -g {}'.format(path('render_output.html')))


if __name__ == '__main__':

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
