from database import *

banco = conexaoBanco()
cursorBD = banco.getCursor()
cursorBD.execute("SHOW TABLES")
for x in cursorBD:
    print(x)


