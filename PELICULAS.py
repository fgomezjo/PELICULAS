import pandas as pd

leerpelis = pd.read_csv("peliculas.csv")
tiGeCa = leerpelis[["titulo","genero","calificacion"]]
leerpelis["Clasica"] = leerpelis["anio"] < 1995
def evaluarApreciacion(calificacion):
    if calificacion > 10 or calificacion < 0:
        return "No Valido"
    elif calificacion > 8.5:
        return "Excelente"
    elif calificacion >= 7:
        return "Buena"
    elif calificacion >= 5:
        return "Regular"
    elif calificacion >= 3:
        return "Mala"
    else:
        return "Pesima"
leerpelis["Apreciacion"] = leerpelis["calificacion"].apply(evaluarApreciacion)
columnas = ["titulo","genero","calificacion","Clasica","Apreciacion"]
leerpelis[columnas].to_csv("archivo.csv", index=False)
promCalifGen = leerpelis.groupby("genero")["calificacion"].mean().reset_index()
promCalifGen = promCalifGen.rename(columns={"calificacion":"Promedio"})
cantGen = leerpelis.groupby("genero").size().reset_index(name="Cantidad")
analisisFinal = pd.merge(promCalifGen, cantGen, on="genero")
analisisFinal.to_excel("peliculasSalida.xlsx", index = False)
