# prtp
Is a python module which enables you to choose from available printers and not just the default one if you were using Tkinter as the graphical user interface. I was using Tkinter to build graphical user interface but there was no tutorial of some sort to be able to print a file to another printer and not just the default one.

## Getting Started

### Prerequisites

Before you install prtp, make sure you have install pywin32.
* [Homepage](http://sf.net/projects/pywin32)
* [Download](https://sourceforge.net/projects/pywin32/files/pywin32/)

### Installing
```
C:\Users\jessie> pip install prtp
```
### Uninstall
```
C:\Users\jessie> pip uninstall prtp
```

### Usage
```
import Tkinter as tk
from prtp import prtp

file_name = 'test.pdf'

root = tk.Tk()
win = prtp.PrintToPrinter(root, filename=file_name)
root.mainloop()

```

## Authors

* **Jesus Vedasto Olazo** - [jestoy0514](https://github.com/jestoy0514)

## License

This project is licensed under the GNU General Public License Version 3 - see the [LICENSE.md](LICENSE.md) file for details
