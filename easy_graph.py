import random, os, json, atexit, datetime

easy_graph_path = os.path.expanduser('~/Dropbox/jca/easy_graph/')

class g:
  out_items = []
  registered = False

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

  days = []
  for i in range(10):
    days.append(datetime.date.today() + datetime.timedelta(days=i))
  graph(zip(days, range(len(days))), show_bars=True)
  graph(zip(days, range(len(days))))

  # Make a graph from a bunch of fake objects.

  # class Foo:
  #   def __init__(self):
  #     self.x, self.y = random.random(), random.random()
  #     self.list_ = [random.random() * 100 for _ in range(100)]
  #     self.date = datetime.datetime.now()

  # foos1 = []
  # foos2 = [Foo() for _ in range(10)]
  # foos3 = [Foo() for _ in range(10)]
  # graph(
  #   [[(foo.x, foo.y) for foo in foos] for foos in (foos1, foos2, foos3)],
  #   xaxis='x', yaxis='y', labels=range(len(foos)))
