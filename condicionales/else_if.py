 
ingreso_mensual = 72000
gasto_mensual = 3000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual > 3000:
        print("estas bien en cualquier parte del mundo")
    else:
        print ("te pasas cabron")
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")
elif ingreso_mensual > 500:
    print("estas bien en angola")
else :
    print("eres pobre")