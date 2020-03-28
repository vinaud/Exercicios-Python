# Conversor de segundos para dias,horas e minutos

print("Por favor, entre com o número de segundos que deseja converter:")

segundos = input()
dias = float(segundos) // 86400

segundos_horas = float(segundos) % 86400
horas = segundos_horas // 3600

segundos_minutos = float(segundos) % 3600
minutos = segundos_minutos // 60

segundos_restantes = segundos_minutos % 60

print(int(dias),"dias,",int(horas),"horas,",int(minutos),"minutos e",int(segundos_restantes),"segundos.")
#a dias, b horas, c minutos e d segundos.
