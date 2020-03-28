# Conversor de segundos para horas e minutos

print("Insira os segundos a serem convertidos")

segundos = input()
horas = float(segundos) // 3600

segundos_minutos = float(segundos) % 3600
minutos = segundos_minutos // 60

segundos_restantes = segundos_minutos % 60

print(segundos, "segundo equivalem a :", int(horas), "hora(s),", int(minutos), "minuto(s),", int(segundos_restantes), "segundos")
