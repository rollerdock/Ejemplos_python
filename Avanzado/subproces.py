import subprocess

a = 0
i = 0
z = i
numcarpetas = int(input("¿Cuántas carpetas quieres crear? "))

for num in range(0, numcarpetas):
    nom = "dir" + str(z)
    subprocess.call(['mkdir', nom])
    print(subprocess.check_output('pwd', shell=True))
    i += 1
    z = i
    a += 1
    nom = "dir"+str(z)
    subprocess.run (['cd',nom])       
    subprocess.call (['mkdir',nom])
    print(subprocess.call('pwd'))
    subprocess.run (['cd',nom])  
    print(subprocess.call('pwd'))
    i+=1
    z=i
    a+=1