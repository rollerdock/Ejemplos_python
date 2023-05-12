import subprocess

a = 0
i = 0
z = i
numcarpetas = int(input("¿Cuántas carpetas quieres crear? "))

for num in range(0, numcarpetas):
    nom = "dir" + str(z)
    subprocess.call(['cmd', '/c', 'mkdir', nom])
    print(subprocess.check_output('cd', shell=True))
    i += 1
    z = i
    a += 1
