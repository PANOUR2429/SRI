from .models import *

# user selection for H (Heating)
H1a_level = 3   #max 4
H1b_level = 2   #max 3
H1c_level = 0   #max 2
H1d_level = 0   #max 4
H1f_level = 0   #max 3
H2a_level = 0   #max 2
H2b_level = 0   #max 3
H2d_level = 0   #max 4
H3_level = 0    #max 4
H4_level = 0    #max 4

# user selection for DHW (Domestic Hot Water)
DHW1a_level = 0   #max 3
DHW1b_level = 0   #max 3
DHW1d_level = 0   #max 3
DHW2b_level = 0   #max 4
DHW3_level = 0    #max 4

DHW_level_list = [DHW1a_level, DHW1b_level,DHW1d_level, DHW2b_level, DHW3_level]

# user selection for C (Cooling)
C1a_level = 0   #max 4
C1b_level = 0   #max 3
C1c_level = 0   #max 2
C1d_level = 0   #max 4
C1f_level = 0   #max 2
C1g_level = 0   #max 3
C2a_level = 0   #max 3
C2b_level = 0   #max 4
C3_level = 0    #max 4
C4_level = 0    #max 4

C_level_list = [C1a_level,C1b_level,C1d_level,C1f_level,C1g_level,C2a_level,C2b_level,C3_level,C4_level]

# user selection for V (Ventilation)
V1a_level = 0   #max 4
V1c_level = 0   #max 4
V2c_level = 0   #max 2
V2d_level = 0   #max 3
V3_level = 0    #max 3
V6_level = 0    #max 3

V_level_list = [V1a_level,V1c_level,V2c_level,V2d_level,V3_level,V6_level]

# user selection for L (Lighting)
L1a_level = 0   #max 3
L2_level = 0   #max 4

L_level_list = [L1a_level, L2_level]

# user selection for DE (Dynamic Building Envelope)
DE1_level = 0   #max 4
DE2_level = 0   #max 3
DE4_level = 0   #max 4

DE_level_list = [DE1_level,DE2_level,DE4_level]

# user selection for E (Electricity)
E2_level = 0   #max 4
E3_level = 0   #max 4
E4_level = 0   #max 3
E5_level = 0   #max 2
E8_level = 0   #max 3
E11_level = 0   #max 4
E12_level = 0   #max 4

E_level_list = [E3_level, E4_level,E5_level,E8_level,E11_level,E12_level]

# user selection for EV (Electrical Vehicle Charging)
EV15_level = 0   #max 4
EV16_level = 0   #max 2
EV17_level = 0   #max 2

Ev_level_list = [EV15_level, EV16_level, EV17_level]

# user selection for MC (Monitoring and Control)
MC3_level = 0   #max 3
MC4_level = 0   #max 3
MC9_level = 0   #max 2
MC13_level = 0   #max 3
MC25_level = 0   #max 2
MC28_level = 0   #max 2
MC29_level = 0   #max 4
MC30_level = 0   #max 3

MC_level_list = [MC3_level,MC4_level,MC9_level,MC13_level,MC25_level,MC28_level,MC29_level,MC30_level]

#SUM OF SERVICES' PERFORMANCES AGAINST EACH CRITERION TO CALCULATE PERFORMANCE OF EACH DOMAIN

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




