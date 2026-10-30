"""Convert the '# %%' cell-marked script into a Jupyter notebook (and execute it)."""
import re, nbformat as nbf, os
src = open(os.path.join(os.path.dirname(__file__), "churn_eda_model.py")).read()
cells = []
for chunk in re.split(r"^# %%", src, flags=re.M)[1:]:
    if chunk.startswith(" [markdown]"):
        body = "\n".join(l[2:] if l.startswith("# ") else l.lstrip("#") for l in chunk.split("\n")[1:]).strip()
        cells.append(nbf.v4.new_markdown_cell(body))
    else:
        cells.append(nbf.v4.new_code_cell(chunk.strip()))
nb = nbf.v4.new_notebook(cells=cells)
nbf.write(nb, os.path.join(os.path.dirname(__file__), "..", "notebooks", "churn_eda_model.ipynb"))
