import os

os.getcwd()

os.listdir("c:\\Users\\janur\\OneDrive\\z_dev\\Python")

atualDir = os.getcwd()
os.chdir("..")
outroDir = os.getcwd()
os.chdir(atualDir)

os.mkdir("pasta2")
os.rmdir("pasta2")

os.rename("teste.txt", "pasta2/teste2.txt")
os.rename("pasta2/teste2.txt", "teste.txt")

os.system("cls")
