import os
import graphviz


d = graphviz.Digraph()
for current_dir, dirs, files in os.walk(r"C:\Users\Denis\Desktop\MLCourse\MLCourse\MLCA"): #передаем в качестве аргумента текущую директорию
    head = current_dir.split("\\")[-1]
    d.node(head)
    for _ in dirs:
      d.edge(head, _)

    for _ in files:
      d.edge(head, _)
d.render("123", view=True)