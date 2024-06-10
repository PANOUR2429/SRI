from .models import *

#user selection

# possible building types: Residential, Non - Residential
selected_building_type = 'Residential'

# possible zones : North Europe, West Europe, North-East Europe, South Europe, South-East Europe
selected_zone = 'West Europe'

# user selection for H (Heating)
H1a_level = 3   #max 4
H1b_level = 2   #max 3
H1c_level = 2   #max 2
H1d_level = 3   #max 4
H1f_level = 0   #max 3
H2a_level = 0   #max 2
H2b_level = 2   #max 3
H2d_level = 0   #max 4
H3_level = 4    #max 4
H4_level = 1    #max 4

# user selection for DHW (Domestic Hot Water)
DHW1a_level = 2   #max 3
DHW1b_level = 1   #max 3
DHW1d_level = 0   #max 3
DHW2b_level = 2   #max 4
DHW3_level = 4    #max 4

# user selection for C (Cooling)
C1a_level = 0   #max 4
C1b_level = 3   #max 3
C1c_level = 2   #max 2
C1d_level = 0   #max 4
C1f_level = 0   #max 2
C1g_level = 0   #max 3
C2a_level = 3   #max 3
C2b_level = 0   #max 4
C3_level = 4   #max 4
C4_level = 2    #max 4

# user selection for V (Ventilation)
V1a_level = 0   #max 4
V1c_level = 2   #max 4
V2c_level = 2   #max 2
V2d_level = 0   #max 3
V3_level = 2   #max 3
V6_level = 0    #max 3

# user selection for L (Lighting)
L1a_level = 1   #max 3
L2_level = 2   #max 4

# user selection for DE (Dynamic Building Envelope)
DE1_level = 1   #max 4
DE2_level = 2   #max 3
DE4_level = 4   #max 4

# user selection for E (Electricity)
E2_level = 2   #max 4
E3_level = 2   #max 4
E4_level = 1   #max 3
E5_level = 1   #max 2
E8_level = 2   #max 3
E11_level = 4   #max 4
E12_level = 1   #max 4

# user selection for EV (Electrical Vehicle Charging)
EV15_level = 2   #max 4
EV16_level = 2   #max 2
EV17_level = 2   #max 2

# user selection for MC (Monitoring and Control)
MC3_level = 2   #max 3
MC4_level = 3   #max 3
MC9_level = 1   #max 2
MC13_level = 2   #max 3
MC25_level = 1   #max 2
MC28_level = 0   #max 2
MC29_level = 2   #max 4
MC30_level = 0   #max 3

print("User selected : ")
print(" Building type :" + str(selected_building_type))
print(" zone :" + str(selected_zone))


#-----------------------------------------------------------------------------------------------------
#SUM OF SERVICES' PERFORMANCES AGAINST EACH CRITERION TO CALCULATE PERFORMANCE OF EACH DOMAIN

print("#SUM OF SERVICES PERFORMANCES")

#-------H calculation-------------
i = 0
H = [0,0,0,0,0,0,0]
H_level_list = [H1a_level, H1b_level, H1c_level, H1d_level, H1f_level, H2a_level, H2b_level, H2d_level, H3_level, H4_level]
H1a = list(Levels.objects.filter(code = 'H-1a', level = H_level_list[0]).values())
H1b = list(Levels.objects.filter(code = 'H-1b', level = H_level_list[1]).values())
H1c = list(Levels.objects.filter(code = 'H-1c', level = H_level_list[2]).values())
H1d = list(Levels.objects.filter(code = 'H-1d', level = H_level_list[3]).values())
H1f = list(Levels.objects.filter(code = 'H-1f', level = H_level_list[4]).values())
H2a = list(Levels.objects.filter(code= 'H-2a', level = H_level_list[5]).values())
H2b = list(Levels.objects.filter(code = 'H-2b', level = H_level_list[6]).values())
H2d = list(Levels.objects.filter(code = 'H-2d', level = H_level_list[7]).values())
H3 = list(Levels.objects.filter(code = 'H-3', level = H_level_list[8]).values())
H4 = list(Levels.objects.filter(code = 'H-4', level = H_level_list[9]).values())

while i < len(H):
  H[i] = H1a[0]["score_cr"+str(i+1)] + H1b[0]["score_cr"+str(i+1)] + H1c[0]["score_cr"+str(i+1)] + H1d[0]["score_cr"+str(i+1)] + H1f[0]["score_cr"+str(i+1)] + H2a[0]["score_cr"+str(i+1)] + H2b[0]["score_cr"+str(i+1)] + H2d[0]["score_cr"+str(i+1)] + H3[0]["score_cr"+str(i+1)] + H4[0]["score_cr"+str(i+1)]
  i += 1

print("H = " + str(H))

#-------DHW calculation-------------
j = 0
DHW = [0,0,0,0,0,0,0]
DHW_level_list = [DHW1a_level, DHW1b_level,DHW1d_level, DHW2b_level, DHW3_level]
DHW1a = list(Levels.objects.filter(code = 'DHW-1a', level = DHW_level_list[0]).values())
DHW1b = list(Levels.objects.filter(code = 'DHW-1b', level = DHW_level_list[1]).values())
DHW1d = list(Levels.objects.filter(code = 'DHW-1d', level = DHW_level_list[2]).values())
DHW2b = list(Levels.objects.filter(code = 'DHW-2b', level = DHW_level_list[3]).values())
DHW3 = list(Levels.objects.filter(code = 'DHW-3', level = DHW_level_list[4]).values())

while j < len(DHW):
  DHW[j] = DHW1a[0]["score_cr"+str(j+1)] + DHW1b[0]["score_cr"+str(j+1)] + DHW1d[0]["score_cr"+str(j+1)] + DHW2b[0]["score_cr"+str(j+1)] + DHW3[0]["score_cr"+str(j+1)]
  j += 1

print("DHW = " + str(DHW))

#-------C calculation-------------
k = 0
C = [0,0,0,0,0,0,0]
C_level_list = [C1a_level,C1b_level,C1c_level, C1d_level,C1f_level,C1g_level,C2a_level,C2b_level,C3_level,C4_level]
C1a = list(Levels.objects.filter(code = 'C-1a', level = C_level_list[0]).values())
C1b = list(Levels.objects.filter(code = 'C-1b', level = C_level_list[1]).values())
C1c = list(Levels.objects.filter(code = 'C-1c', level = C_level_list[2]).values())
C1d = list(Levels.objects.filter(code = 'C-1d', level = C_level_list[3]).values())
C1f = list(Levels.objects.filter(code = 'C-1f', level = C_level_list[4]).values())
C1g = list(Levels.objects.filter(code = 'C-1g', level = C_level_list[5]).values())
C2a = list(Levels.objects.filter(code = 'C-2a', level = C_level_list[6]).values())
C2b = list(Levels.objects.filter(code = 'C-2b', level = C_level_list[7]).values())
C3 = list(Levels.objects.filter(code = 'C-3', level = C_level_list[8]).values())
C4 = list(Levels.objects.filter(code = 'C-4', level = C_level_list[9]).values())

while k < len(C):
  C[k] = C1a[0]["score_cr"+str(k+1)] + C1b[0]["score_cr"+str(k+1)] + C1c[0]["score_cr"+str(k+1)]+ C1d[0]["score_cr"+str(k+1)] + C1f[0]["score_cr"+str(k+1)] + C1g[0]["score_cr"+str(k+1)] + C2a[0]["score_cr"+str(k+1)] + C2b[0]["score_cr"+str(k+1)] + C3[0]["score_cr"+str(k+1)] + C4[0]["score_cr"+str(k+1)]
  k += 1

print("C = " + str(C))

#-------V calculation-------------
k = 0
V = [0,0,0,0,0,0,0]
V_level_list = [V1a_level,V1c_level,V2c_level,V2d_level,V3_level,V6_level]
V1a = list(Levels.objects.filter(code = 'V-1a', level = V_level_list[0]).values())
V1c = list(Levels.objects.filter(code = 'V-1c', level = C_level_list[1]).values())
V2c = list(Levels.objects.filter(code = 'V-2c', level = V_level_list[2]).values())
V2d = list(Levels.objects.filter(code = 'V-2d', level = V_level_list[3]).values())
V3 = list(Levels.objects.filter(code = 'V-3', level = V_level_list[4]).values())
V6 = list(Levels.objects.filter(code = 'V-6', level = V_level_list[5]).values())

while k < len(V):
  V[k] = V1a[0]["score_cr"+str(k+1)] + V1c[0]["score_cr"+str(k+1)]+ V2c[0]["score_cr"+str(k+1)] + V2d[0]["score_cr"+str(k+1)] + V3[0]["score_cr"+str(k+1)] + V6[0]["score_cr"+str(k+1)]
  k += 1

print("V = " + str(V))

#-------L calculation-------------
k = 0
L = [0,0,0,0,0,0,0]
L_level_list = [L1a_level, L2_level]
L1a = list(Levels.objects.filter(code = 'L-1a', level = L_level_list[0]).values())
L2 = list(Levels.objects.filter(code = 'L-2', level = L_level_list[1]).values())

while k < len(L):
  L[k] = L1a[0]["score_cr"+str(k+1)] + L2[0]["score_cr"+str(k+1)]
  k += 1

print("L = " + str(L))

#-------DE calculation-------------
k = 0
DE = [0,0,0,0,0,0,0]
DE_level_list = [DE1_level,DE2_level,DE4_level]
DE1 = list(Levels.objects.filter(code = 'DE-1', level = DE_level_list[0]).values())
DE2 = list(Levels.objects.filter(code = 'DE-2', level = DE_level_list[1]).values())
DE4 = list(Levels.objects.filter(code = 'DE-4', level = DE_level_list[2]).values())

while k < len(DE):
  DE[k] = DE1[0]["score_cr"+str(k+1)] + DE2[0]["score_cr"+str(k+1)] + DE4[0]["score_cr"+str(k+1)]
  k += 1

print("DE = " + str(DE))

#-------E calculation-------------
k = 0
E = [0,0,0,0,0,0,0]
E_level_list = [E2_level, E3_level, E4_level,E5_level,E8_level,E11_level,E12_level]
E2 = list(Levels.objects.filter(code = 'E-2', level = E_level_list[0]).values())
E3 = list(Levels.objects.filter(code = 'E-3', level = E_level_list[1]).values())
E4 = list(Levels.objects.filter(code = 'E-4', level = E_level_list[2]).values())
E5 = list(Levels.objects.filter(code = 'E-5', level = E_level_list[3]).values())
E8 = list(Levels.objects.filter(code = 'E-8', level = E_level_list[4]).values())
E11 = list(Levels.objects.filter(code = 'E-11', level = E_level_list[5]).values())
E12 = list(Levels.objects.filter(code = 'E-12', level = E_level_list[6]).values())

while k < len(E):
  E[k] = E2[0]["score_cr"+str(k+1)] + E3[0]["score_cr"+str(k+1)] + E4[0]["score_cr"+str(k+1)] + E5[0]["score_cr"+str(k+1)] + E8[0]["score_cr"+str(k+1)] + E11[0]["score_cr"+str(k+1)] + E12[0]["score_cr"+str(k+1)]
  k += 1

print("E = " + str(E))

#-------EV calculation-------------
k = 0
EV = [0,0,0,0,0,0,0]
EV_level_list = [EV15_level, EV16_level, EV17_level]
EV15 = list(Levels.objects.filter(code = 'EV-15', level = EV_level_list[0]).values())
EV16 = list(Levels.objects.filter(code = 'EV-16', level = EV_level_list[1]).values())
EV17 = list(Levels.objects.filter(code = 'EV-17', level = EV_level_list[2]).values())

while k < len(EV):
  EV[k] = EV15[0]["score_cr"+str(k+1)] + EV16[0]["score_cr"+str(k+1)] + EV17[0]["score_cr"+str(k+1)]
  k += 1

print("EV = " + str(EV))

#-------MC calculation-------------
k = 0
MC = [0,0,0,0,0,0,0]
MC_level_list = [MC3_level,MC4_level,MC9_level,MC13_level,MC25_level,MC28_level,MC29_level,MC30_level]
MC3 = list(Levels.objects.filter(code = 'MC-3', level = MC_level_list[0]).values())
MC4 = list(Levels.objects.filter(code = 'MC-4', level = MC_level_list[1]).values())
MC9 = list(Levels.objects.filter(code = 'MC-9', level = MC_level_list[2]).values())
MC13 = list(Levels.objects.filter(code = 'MC-13', level = MC_level_list[3]).values())
MC25 = list(Levels.objects.filter(code = 'MC-25', level = MC_level_list[4]).values())
MC28 = list(Levels.objects.filter(code = 'MC-28', level = MC_level_list[5]).values())
MC29 = list(Levels.objects.filter(code = 'MC-29', level = MC_level_list[6]).values())
MC30 = list(Levels.objects.filter(code = 'MC-30', level = MC_level_list[7]).values())

while k < len(MC):
  MC[k] = MC3[0]["score_cr"+str(k+1)] + MC4[0]["score_cr"+str(k+1)] + MC9[0]["score_cr"+str(k+1)] + MC13[0]["score_cr"+str(k+1)] + MC25[0]["score_cr"+str(k+1)] + MC28[0]["score_cr"+str(k+1)] + MC29[0]["score_cr"+str(k+1)] + MC30[0]["score_cr"+str(k+1)]
  k += 1

print("MC = " + str(MC))


#-----------------------------------------------------------------------------------------------------
# SUM OF SERVICES' MAX PERFORMANCES AGAINST EACH CRITERION TO CALCULATE MAX PERFORMANCE OF EACH DOMAIN
print("")
print("#SUM OF SERVICES MAX PERFORMANCES ")

#-------Hmax calculation-------------
i = 0
Hmax = [0,0,0,0,0,0,0]
Hmax_level_list = [4, 3, 2, 4, 3, 2, 3, 4, 4, 4]
H1amax = list(Levels.objects.filter(code = 'H-1a', level = Hmax_level_list[0]).values())
H1bmax = list(Levels.objects.filter(code = 'H-1b', level = Hmax_level_list[1]).values())
H1cmax = list(Levels.objects.filter(code = 'H-1c', level = Hmax_level_list[2]).values())
H1dmax = list(Levels.objects.filter(code = 'H-1d', level = Hmax_level_list[3]).values())
H1fmax = list(Levels.objects.filter(code = 'H-1f', level = Hmax_level_list[4]).values())
H2amax = list(Levels.objects.filter(code= 'H-2a', level = Hmax_level_list[5]).values())
H2bmax = list(Levels.objects.filter(code = 'H-2b', level = Hmax_level_list[6]).values())
H2dmax = list(Levels.objects.filter(code = 'H-2d', level = Hmax_level_list[7]).values())
H3max = list(Levels.objects.filter(code = 'H-3', level = Hmax_level_list[8]).values())
H4max = list(Levels.objects.filter(code = 'H-4', level = Hmax_level_list[9]).values())

while i < len(Hmax):
  Hmax[i] = H1amax[0]["score_cr"+str(i+1)] + H1bmax[0]["score_cr"+str(i+1)] + H1cmax[0]["score_cr"+str(i+1)] + H1dmax[0]["score_cr"+str(i+1)] + H1fmax[0]["score_cr"+str(i+1)] + H2amax[0]["score_cr"+str(i+1)] + H2bmax[0]["score_cr"+str(i+1)] + H2dmax[0]["score_cr"+str(i+1)] + H3max[0]["score_cr"+str(i+1)] + H4max[0]["score_cr"+str(i+1)]
  i += 1

print("Hmax = " + str(Hmax))

#-------DHWmax calculation-------------
j = 0
DHWmax = [0,0,0,0,0,0,0]
DHWmax_level_list = [3, 3,3, 4, 4]
DHW1amax = list(Levels.objects.filter(code = 'DHW-1a', level = DHWmax_level_list[0]).values())
DHW1bmax = list(Levels.objects.filter(code = 'DHW-1b', level = DHWmax_level_list[1]).values())
DHW1dmax = list(Levels.objects.filter(code = 'DHW-1d', level = DHWmax_level_list[2]).values())
DHW2bmax = list(Levels.objects.filter(code = 'DHW-2b', level = DHWmax_level_list[3]).values())
DHW3max = list(Levels.objects.filter(code = 'DHW-3', level = DHWmax_level_list[4]).values())

while j < len(DHWmax):
  DHWmax[j] = DHW1amax[0]["score_cr"+str(j+1)] + DHW1bmax[0]["score_cr"+str(j+1)] + DHW1dmax[0]["score_cr"+str(j+1)] + DHW2bmax[0]["score_cr"+str(j+1)] + DHW3max[0]["score_cr"+str(j+1)]
  j += 1

print("DHWmax = " + str(DHWmax))

#-------Cmax calculation-------------
k = 0
Cmax = [0,0,0,0,0,0,0]
Cmax_level_list = [4,3,2, 4,2,3,3,4,4,4]
C1amax = list(Levels.objects.filter(code = 'C-1a', level = Cmax_level_list[0]).values())
C1bmax = list(Levels.objects.filter(code = 'C-1b', level = Cmax_level_list[1]).values())
C1cmax = list(Levels.objects.filter(code = 'C-1c', level = Cmax_level_list[2]).values())
C1dmax = list(Levels.objects.filter(code = 'C-1d', level = Cmax_level_list[3]).values())
C1fmax = list(Levels.objects.filter(code = 'C-1f', level = Cmax_level_list[4]).values())
C1gmax = list(Levels.objects.filter(code = 'C-1g', level = Cmax_level_list[5]).values())
C2amax = list(Levels.objects.filter(code = 'C-2a', level = Cmax_level_list[6]).values())
C2bmax = list(Levels.objects.filter(code = 'C-2b', level = Cmax_level_list[7]).values())
C3max = list(Levels.objects.filter(code = 'C-3', level = Cmax_level_list[8]).values())
C4max = list(Levels.objects.filter(code = 'C-4', level = Cmax_level_list[9]).values())

while k < len(Cmax):
  Cmax[k] = C1amax[0]["score_cr"+str(k+1)] + C1bmax[0]["score_cr"+str(k+1)] + C1cmax[0]["score_cr"+str(k+1)]+ C1dmax[0]["score_cr"+str(k+1)] + C1fmax[0]["score_cr"+str(k+1)] + C1gmax[0]["score_cr"+str(k+1)] + C2amax[0]["score_cr"+str(k+1)] + C2bmax[0]["score_cr"+str(k+1)] + C3max[0]["score_cr"+str(k+1)] + C4max[0]["score_cr"+str(k+1)]
  k += 1

print("Cmax = " + str(Cmax))

#-------Vmax calculation-------------
k = 0
Vmax = [0,0,0,0,0,0,0]
Vmax_level_list = [4,4,2,3,3,3]
V1amax = list(Levels.objects.filter(code = 'V-1a', level = Vmax_level_list[0]).values())
V1cmax = list(Levels.objects.filter(code = 'V-1c', level = Cmax_level_list[1]).values())
V2cmax = list(Levels.objects.filter(code = 'V-2c', level = Vmax_level_list[2]).values())
V2dmax = list(Levels.objects.filter(code = 'V-2d', level = Vmax_level_list[3]).values())
V3max = list(Levels.objects.filter(code = 'V-3', level = Vmax_level_list[4]).values())
V6max = list(Levels.objects.filter(code = 'V-6', level = Vmax_level_list[5]).values())

while k < len(Vmax):
  Vmax[k] = V1amax[0]["score_cr"+str(k+1)] + V1cmax[0]["score_cr"+str(k+1)]+ V2cmax[0]["score_cr"+str(k+1)] + V2dmax[0]["score_cr"+str(k+1)] + V3max[0]["score_cr"+str(k+1)] + V6max[0]["score_cr"+str(k+1)]
  k += 1

print("Vmax = " + str(Vmax))

#-------Lmax calculation-------------
k = 0
Lmax = [0,0,0,0,0,0,0]
Lmax_level_list = [3, 4]
L1amax = list(Levels.objects.filter(code = 'L-1a', level = Lmax_level_list[0]).values())
L2max = list(Levels.objects.filter(code = 'L-2', level = Lmax_level_list[1]).values())

while k < len(Lmax):
  Lmax[k] = L1amax[0]["score_cr"+str(k+1)] + L2max[0]["score_cr"+str(k+1)]
  k += 1

print("Lmax = " + str(Lmax))

#-------DEmax calculation-------------
k = 0
DEmax = [0,0,0,0,0,0,0]
DEmax_level_list = [4,3,4]
DE1max = list(Levels.objects.filter(code = 'DE-1', level = DEmax_level_list[0]).values())
DE2max = list(Levels.objects.filter(code = 'DE-2', level = DEmax_level_list[1]).values())
DE4max = list(Levels.objects.filter(code = 'DE-4', level = DEmax_level_list[2]).values())

while k < len(DEmax):
  DEmax[k] = DE1max[0]["score_cr"+str(k+1)] + DE2max[0]["score_cr"+str(k+1)] + DE4max[0]["score_cr"+str(k+1)]
  k += 1

print("DEmax = " + str(DEmax))

#-------Emax calculation-------------
k = 0
Emax = [0,0,0,0,0,0,0]
Emax_level_list = [4, 4, 3,2,3,4,4]
E2max = list(Levels.objects.filter(code = 'E-2', level = Emax_level_list[0]).values())
E3max = list(Levels.objects.filter(code = 'E-3', level = Emax_level_list[1]).values())
E4max = list(Levels.objects.filter(code = 'E-4', level = Emax_level_list[2]).values())
E5max = list(Levels.objects.filter(code = 'E-5', level = Emax_level_list[3]).values())
E8max = list(Levels.objects.filter(code = 'E-8', level = Emax_level_list[4]).values())
E11max = list(Levels.objects.filter(code = 'E-11', level = Emax_level_list[5]).values())
E12max = list(Levels.objects.filter(code = 'E-12', level = Emax_level_list[6]).values())

while k < len(Emax):
  Emax[k] = E2max[0]["score_cr"+str(k+1)] + E3max[0]["score_cr"+str(k+1)] + E4max[0]["score_cr"+str(k+1)] + E5max[0]["score_cr"+str(k+1)] + E8max[0]["score_cr"+str(k+1)] + E11max[0]["score_cr"+str(k+1)] + E12max[0]["score_cr"+str(k+1)]
  k += 1

print("Emax = " + str(Emax))

#-------EVmax calculation-------------
k = 0
EVmax = [0,0,0,0,0,0,0]
EVmax_level_list = [4, 2, 2]
EV15max = list(Levels.objects.filter(code = 'EV-15', level = EVmax_level_list[0]).values())
EV16max = list(Levels.objects.filter(code = 'EV-16', level = EVmax_level_list[1]).values())
EV17max = list(Levels.objects.filter(code = 'EV-17', level = EVmax_level_list[2]).values())

while k < len(EVmax):
  EVmax[k] = EV15max[0]["score_cr"+str(k+1)] + EV16max[0]["score_cr"+str(k+1)] + EV17max[0]["score_cr"+str(k+1)]
  k += 1

print("EVmax = " + str(EVmax))

#-------MCmax calculation-------------
k = 0
MCmax = [0,0,0,0,0,0,0]
MCmax_level_list = [3,3,2,3,2,2,4,3]
MC3max = list(Levels.objects.filter(code = 'MC-3', level = MCmax_level_list[0]).values())
MC4max = list(Levels.objects.filter(code = 'MC-4', level = MCmax_level_list[1]).values())
MC9max = list(Levels.objects.filter(code = 'MC-9', level = MCmax_level_list[2]).values())
MC13max = list(Levels.objects.filter(code = 'MC-13', level = MCmax_level_list[3]).values())
MC25max = list(Levels.objects.filter(code = 'MC-25', level = MCmax_level_list[4]).values())
MC28max = list(Levels.objects.filter(code = 'MC-28', level = MCmax_level_list[5]).values())
MC29max = list(Levels.objects.filter(code = 'MC-29', level = MCmax_level_list[6]).values())
MC30max = list(Levels.objects.filter(code = 'MC-30', level = MCmax_level_list[7]).values())

while k < len(MCmax):
  MCmax[k] = MC3max[0]["score_cr"+str(k+1)] + MC4max[0]["score_cr"+str(k+1)] + MC9max[0]["score_cr"+str(k+1)] + MC13max[0]["score_cr"+str(k+1)] + MC25max[0]["score_cr"+str(k+1)] + MC28max[0]["score_cr"+str(k+1)] + MC29max[0]["score_cr"+str(k+1)] + MC30max[0]["score_cr"+str(k+1)]
  k += 1

print("MCmax = " + str(MCmax))

#-----------------------------------------------------------------------------------------------------
# NORMALISED VALUES CALCULATIONS
print("")
print("NORMALISED VALUES BAZED ON USER SELECTION FOR BUILDING TYPE AND ZONE")

g = 0
N_H = [0,0,0,0,0,0,0]
N_DHW = [0,0,0,0,0,0,0]
N_C = [0,0,0,0,0,0,0]
N_V = [0,0,0,0,0,0,0]
N_L = [0,0,0,0,0,0,0]
N_DE = [0,0,0,0,0,0,0]
N_E = [0,0,0,0,0,0,0]
N_EV = [0,0,0,0,0,0,0]
N_MC = [0,0,0,0,0,0,0]

N_Hmax = [0,0,0,0,0,0,0]
N_DHWmax = [0,0,0,0,0,0,0]
N_Cmax = [0,0,0,0,0,0,0]
N_Vmax = [0,0,0,0,0,0,0]
N_Lmax = [0,0,0,0,0,0,0]
N_DEmax = [0,0,0,0,0,0,0]
N_Emax = [0,0,0,0,0,0,0]
N_EVmax = [0,0,0,0,0,0,0]
N_MCmax = [0,0,0,0,0,0,0]

W_H = list(DomainWeight.objects.filter(domain = 'Heating', building_type = selected_building_type, zone = selected_zone).values())
W_DHW = list(DomainWeight.objects.filter(domain = 'Domestic hot water', building_type = selected_building_type, zone = selected_zone).values())
W_C = list(DomainWeight.objects.filter(domain = 'Cooling', building_type = selected_building_type, zone = selected_zone).values())
W_V = list(DomainWeight.objects.filter(domain = 'Ventilation', building_type = selected_building_type, zone = selected_zone).values())
W_L = list(DomainWeight.objects.filter(domain = 'Lighting', building_type = selected_building_type, zone = selected_zone).values())
W_DE = list(DomainWeight.objects.filter(domain = 'Dynamic building envelope', building_type = selected_building_type, zone = selected_zone).values())
W_E = list(DomainWeight.objects.filter(domain = 'Electricity', building_type = selected_building_type, zone = selected_zone).values())
W_EV = list(DomainWeight.objects.filter(domain = 'Electric vehicle charging', building_type = selected_building_type, zone = selected_zone).values())
W_MC = list(DomainWeight.objects.filter(domain = 'Monitoring and control', building_type = selected_building_type, zone = selected_zone).values())

while g < len(N_H):
  N_H[g] = H[g] * W_H[0]["dw_cr"+str(g+1)]
  N_DHW[g] = DHW[g] * W_DHW[0]["dw_cr" + str(g + 1)]
  N_C[g] = C[g] * W_C[0]["dw_cr" + str(g + 1)]
  N_V[g] = V[g] * W_V[0]["dw_cr" + str(g + 1)]
  N_L[g] = L[g] * W_L[0]["dw_cr" + str(g + 1)]
  N_DE[g] = DE[g] * W_DE[0]["dw_cr" + str(g + 1)]
  N_E[g] = E[g] * W_E[0]["dw_cr" + str(g + 1)]
  N_EV[g] = EV[g] * W_EV[0]["dw_cr" + str(g + 1)]
  N_MC[g] = MC[g] * W_MC[0]["dw_cr" + str(g + 1)]
  N_Hmax[g] = Hmax[g] * W_H[0]["dw_cr"+str(g+1)]
  N_DHWmax[g] = DHWmax[g] * W_DHW[0]["dw_cr" + str(g + 1)]
  N_Cmax[g] = Cmax[g] * W_C[0]["dw_cr" + str(g + 1)]
  N_Vmax[g] = Vmax[g] * W_V[0]["dw_cr" + str(g + 1)]
  N_Lmax[g] = Lmax[g] * W_L[0]["dw_cr" + str(g + 1)]
  N_DEmax[g] = DEmax[g] * W_DE[0]["dw_cr" + str(g + 1)]
  N_Emax[g] = Emax[g] * W_E[0]["dw_cr" + str(g + 1)]
  N_EVmax[g] = EVmax[g] * W_EV[0]["dw_cr" + str(g + 1)]
  N_MCmax[g] = MCmax[g] * W_MC[0]["dw_cr" + str(g + 1)]
  g += 1


print("N_H = " + str(N_H))
print("N_DHW = " + str(N_DHW))
print("N_C = " + str(N_C))
print("N_V = " + str(N_V))
print("N_L = " + str(N_L))
print("N_DE = " + str(N_DE))
print("N_E = " + str(N_E))
print("N_EV = " + str(N_EV))
print("N_MC = " + str(N_MC))
print("")
print("N_Hmax = " + str(N_Hmax))
print("N_DHWmax = " + str(N_DHWmax))
print("N_Cmax = " + str(N_Cmax))
print("N_Vmax = " + str(N_Vmax))
print("N_Lmax = " + str(N_Lmax))
print("N_DEmax = " + str(N_DEmax))
print("N_Emax = " + str(N_Emax))
print("N_EVmax = " + str(N_EVmax))
print("N_MCmax = " + str(N_MCmax))

#------------------------------
#SMARTNESS OF EACH CRITERION
print("")
print("SMARTNESS & NORMALISED SMARTNESS OF EACH CRITERION BAZED ON USER SELECTION FOR BUILDING TYPE AND ZONE")


i = 0
Smartness = [0,0,0,0,0,0,0]
Sum_N = [0,0,0,0,0,0,0]
Sum_N_Max = [0,0,0,0,0,0,0]

W = list(ImpactWeight.objects.filter(building_type = selected_building_type, zone = selected_zone).values())
N_Smartness = [0,0,0,0,0,0,0]

while i < len(Smartness):
  Sum_N[i] = N_H[i]+N_DHW[i]+N_C[i]+N_V[i]+N_L[i]+N_DE[i]+N_E[i]+N_EV[i]+N_MC[i]
  Sum_N_Max[i] = N_Hmax[i] + N_DHWmax[i] + N_Cmax[i] + N_Vmax[i] + N_Lmax[i] + N_DEmax[i] + N_Emax[i] + N_EVmax[i] + N_MCmax[i]
  Smartness[i] = Sum_N[i] / Sum_N_Max[i]
  N_Smartness[i] = Smartness[i] * W[0]["imp_cr"+str(i+1)]
  i += 1

print ("Smartness = " + str(Smartness))
print ("Normalized Smartness = " + str(N_Smartness))


#------------------------------
# SMARTNESS VALUES OF EACH KEY FUNCTIONALITY
print("")
print("SMARTNESS VALUES OF EACH KEY FUNCTIONALITY")

w_kf1 = 1/3
w_kf2 = 1/3
w_kf3 = 1/3

kf1 = w_kf1 * ( N_Smartness[0] + N_Smartness[6] )
kf2 = w_kf2 * sum(N_Smartness[2:5])
kf3 = w_kf3 * ( N_Smartness[1] )

SRI = kf1 + kf2 + kf3

print ("kf1 = " + str(kf1))
print ("kf2 = " + str(kf2))
print ("kf3 = " + str(kf3))
print("-------------------")
print("TOTAL SRI:  ")
print ("SRI = " + str(SRI) )
print("-------------------")
print("User selected : ")
print(" Building type : " + str(selected_building_type))
print(" zone : " + str(selected_zone))
print(" H Levels   : " + str(H_level_list))
print(" DHW Levels : " + str(DHW_level_list))
print(" C Levels   : " + str(C_level_list))
print(" V Levels   : " + str(V_level_list))
print(" L Levels   : " + str(L_level_list))
print(" DE Levels  : " + str(DE_level_list))
print(" E Levels   : " + str(E_level_list))
print(" EV Levels  : " + str(EV_level_list))
print(" MC Levels  : " + str(MC_level_list))
print("--------------------")
print ("SRI = " + str( round(SRI,4) * 100) + "%")




# test code bellow
#l_H1a = Levels.objects.filter(id=1, code = 'H-1a', level = i).values()
#print(list(l_H1a))

#=list(l_H1a)[0]["desc"]
#print(x)

#y = list(Levels.objects.values())
#print(y[0]["desc"])


#x = Levels.objects.filter(code = 'H-1a', level = 4).values()
#y=list(x)

#print(y)
#print(y[0]["score_cr"+str(6)])
#print(y[0]["score_cr"+str(1)])




