from pyDatalog import pyDatalog

# Limpiar base de conocimiento
pyDatalog.clear()

# Definir términos en PyDatalog
pyDatalog.create_terms('SeUne, Bloqueo, PuedeUnirse, Efectivo, CandidatoFarmaco, Spike, ACE2, Inhibidor, X')

# Definir hechos (datos del problema)
+ SeUne('Spike', 'ACE2')  # La proteína Spike se une a ACE2
+ PuedeUnirse('Inhibidor', 'Spike')  # El inhibidor puede unirse a Spike
+ Bloqueo('Spike', 'ACE2')  # Si se bloquea Spike, se inhibe la infección

# Definir reglas de inferencia
Efectivo(X) <= PuedeUnirse(X, 'Spike') & Bloqueo('Spike', 'ACE2')  # Si el inhibidor se une a Spike y bloquea ACE2, es efectivo
CandidatoFarmaco(X) <= Efectivo(X)  # Si un inhibidor es efectivo, es candidato a fármaco

# Consultas
print("¿La proteína Spike se une a ACE2?", SeUne)  # Consultar relación SeUne
print("¿El inhibidor puede unirse a Spike?", PuedeUnirse)  # Consultar relación PuedeUnirse
print("¿El inhibidor es efectivo?", Efectivo)  # Consultar relación Efectivo
print("¿El inhibidor es candidato a fármaco?", CandidatoFarmaco)  # Consultar relación CandidatoFarmaco
