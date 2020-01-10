# csv-to-tex-table
Instruction for converting csv-files, produced here by NumPy, to a format required in TeX-tables.

# What to do in Python?
We will start at the point, where all data is calculated.

The line in python should be according to
```
numpy.savetxt('output.csv',
    numpy.column_stack([data1, data2, ...]),
    fmt='%.2f, %.0f, ...',
    header='data1, data2, ...')
```
The option `fmt` let you decide how many decimal places should be written.
In this example 2 for `data1` and 0 for `data2`.

**IMPORTANT:**
- Watch that you set a format for each column!
- Use the `,` between each of the numbers (as shown)

# What next?
If you try to change the format simply from `.csv` to `.tex` it would not work.
I tried to get things done with the end-of-line character option in `numpy-savetxt`
but it did not satisfy me.

Instead we can use the two commands
```
sed '/^#/ d' < output.csv > output-new.csv

cat output-new.csv | sed \
    -e 's:,:\t\&\t:g' \
    -e 's:$:\t\\\\:g' > output.tex
```
With those command we can prepare the `output.csv`-file in a way,
that we only need to import it into LaTeX.

The first `sed` command removes the header-line and writes it into a new file.
(For some reason it does not work for me with the same file;
if you do not use a header, you can remove the line)

Quick rundown of the arguments from second `sed`:
- Replacing the `,` as a delimiter with the `&` used by TeX
  (one could use the `&` already in the `fmt`-option)
- Replacing the end of line, withe the double backslash `\\`

The next part is bigger and needs to be adapted for each table,
but i did not fin a way without it.
```
ed output.tex << END
1i
\begin{tabular}{c c ...}
\toprule
{Data 1} & {Data 2} & ... \\\\
\midrule
.
\$a
\bottomrule
\end{tabular}
.
wq
END
```
These lines put the previous prepared data into the tabular structure.
For each table, change
- the number of columns and the way to display them (`c` or `S`)
- the title of each column

# What to do in TeX?
```
\begin{table}
  \input{output.tex}
\end{table}
```
Of course you should add things as `centering`, `caption` and `label`
as needed.

You may also take a look into the example.
