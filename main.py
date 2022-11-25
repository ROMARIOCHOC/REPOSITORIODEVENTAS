print("BIENVENIDOS AL PROGRAMA DE VENDEDORES: ");
nombre=str(input("INGRESE SU NOMBRE: "));
año_nacim=int(input("INGRESE LA FECHA DE NACIMIENTO: "));
edad=2022-año_nacim;

if(edad>=18):
    print("Bienvenido al programa");
    semestre1=int(input("ingrese el primer semestre: "));
    semestre2=int(input("ingrese el segundo semestre: "));
    ventas=semestre1+semestre2;
    if semestre1 > semestre2:
     mensaje = ("semestre mayor ES 1ERO");
    elif semestre1 == semestre2:
     mensaje = ("son iguales");
    else:
     mensaje = ("semestre mayor es 2do");

    if (ventas >= 100000):
       medalla = "la medalla BRONCE";
       premio = "premio es DIA LIBRE";
    elif(ventas >= 100001 and ventas < 500000):
      medalla = "la medalla plata";
      premio = "UN   dia libre el bono es Q250";
    elif (ventas >= 500001 and ventas >= 1000000):
      medalla = "la medalla ORO";
      premio = "un dia libre el bono es Q500";
    else:
      medalla = "la medalla es de DIAMANTE";
      premio = "dos dias libres bono es Q1000";
    print("VENDEDOR",nombre);
    print("VENTAS", ventas);
    print("MEDALLA", medalla);
    print("PREMIO", premio);



















