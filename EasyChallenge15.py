f = open(r'\\blm\dfs\or\egis\workspace\mpirkl.BLM\textexample.txt', 'w')
t = "This is a new string"
t_new = t.rjust(100)
f.write(t_new)
f.close()