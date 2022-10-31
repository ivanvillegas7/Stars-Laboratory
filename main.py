# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 15:04:05 2021

@author: Iván
"""

import matplotlib.pyplot as plt

import numpy as np

from typing import List


#Tarea 1


#Seleccionamos el tipo de estrellas de referencia

esp: List[str] = ['Sun', 'A5', 'F0', 'M0', 'M5']

i: int = 0

#Impirtamos los datos

with  open("MuestraSP.dat", "r") as infile:
    
    lines = infile.readlines()
        
    spectral_type: List[str] = []

    T: List[float] = []

    L: List[float] = []

    M_esp: List[float] = []

    T_esp: List[float] = []

    L_esp: List[float] = []

    for  line in  lines:

        #Nos saltamos las 4 primeras filas del archivo        

        if i==0:
            
            i+=1
            
        elif i==1:
            
            i+=1
            
        elif i==2:
            
            i+=1
            
        elif i==3:
            
            i+=1
            
        else:

            vals = line.split()

            spectral_type.append(str(vals[0]))

            if vals[0] in esp:

                #Guardamos los datos de nuestras estrellas de referencia        
        
                T_esp.append(np.log10(float(vals[1])))

                L_esp.append(np.log10(float(vals[2])))
                
                M_esp.append(float(vals[3]))
                    
            else:

                #Guardamos los datos del resto de estrellas
                
                T.append(np.log10(float(vals[1])))

                L.append(np.log10(float(vals[2])))

#Creamos el diagrama HR

plt.figure()

plt.plot(T, L, color='blue', label='Studied stars')
plt.plot(T_esp, L_esp, 'o', color='red', label='Reference stars')
plt.gca().invert_xaxis()
plt.title('HR diagram')
plt.xlabel(r'Log$_{10}(T_e [K])$')
plt.ylabel(r'Log$_{10}(L [L_\odot])$')
plt.legend()
plt.grid(True)

plt.savefig('Tarea1.pdf')


#%%

#Tarea 2


with  open("summary_z1_sun.txt", "r") as infile:
    
    lines = infile.readlines()
    
    L_z1_s: List[float] = []
    
    T_z1_s: List[float] = []
    
    L_ext_z1_s: List[float] = []
    
    T_ext_z1_s: List[float] = []
    
    for line in lines:
        
        vals = line.split()
        
        if float(vals[1]) == 0.0 or float(vals[1]) == (5e9):
            
            T_ext_z1_s.append(float(vals[5]))
            
            L_ext_z1_s.append(float(vals[3]))
            
        if float(vals[1]) <= (5e9):
            
            T_z1_s.append(float(vals[5]))
            
            L_z1_s.append(float(vals[3]))
            
with  open("summary_z2_sun.txt", "r") as infile:
    
    lines = infile.readlines()
    
    L_z2_s: List[float] = []
    
    T_z2_s: List[float] = []
    
    L_ext_z2_s: List[float] = []
    
    T_ext_z2_s: List[float] = []
    
    L_pp_s: List[float] = []
    
    L_CNO_s: List[float] = []
    
    L_sun: List[float] = []
    
    for line in lines:
        
        vals = line.split()
        
        if float(vals[1]) == 0.0 or float(vals[1]) == (5e9):
            
            T_ext_z2_s.append(float(vals[5]))
            
            L_ext_z2_s.append(float(vals[3]))
            
        if float(vals[1]) <= (5e9):
            
            T_z2_s.append(float(vals[5]))
            
            L_z2_s.append(float(vals[3]))
            
            L_pp_s.append(float(vals[18]))
            
            L_CNO_s.append(float(vals[19]))
            
            L_sun.append(float(vals[3]))
            

plt.figure()

plt.plot(T_z1_s, L_z1_s, color='blue', label='Z=0.001')
plt.plot(T_ext_z1_s, L_ext_z1_s, 'o', color='blue', label='Specified $\\tau$ for Z=0.001')
plt.plot(T_z2_s, L_z2_s, color='red', label='Z=0.02')
plt.plot(T_ext_z2_s, L_ext_z2_s, 'o', color='red', label='Specified $\\tau$ for Z=0.02')
plt.plot(T, L, color='green', label='HR diagram')
plt.plot(T_esp[2], L_esp[2], 'o', color='black', label='Sun')
plt.gca().invert_xaxis()
plt.title(r'HR diagram with $M=M_\odot$')
plt.xlabel(r'Log$_{10}(T_e [K])$')
plt.ylabel(r'Log$_{10}(L [L_\odot])$')
plt.legend()
plt.grid()

plt.savefig('Tarea2_1.pdf')

plt.figure()

plt.plot(T_z1_s, L_z1_s, color='blue', label='Z=0.001')
plt.plot(T_ext_z1_s, L_ext_z1_s, 'o', color='blue', label='Specified $\\tau$ for Z=0.001')
plt.plot(T_z2_s, L_z2_s, color='red', label='Z=0.02')
plt.plot(T_ext_z2_s, L_ext_z2_s, 'o', color='red', label='Specified $\\tau$ for Z=0.02')
plt.plot(T, L, color='green', label='HR diagram')
plt.plot(T_esp[2], L_esp[2], 'o', color='black', label='Sun')
plt.gca().invert_xaxis()
plt.title(r'HR diagram with $M=M_\odot$')
plt.xlabel(r'Log$_{10}(T_e [K])$')
plt.ylabel(r'Log$_{10}(L [L_\odot])$')
plt.legend()
plt.grid()
plt.xlim(3.9, 3.7)
plt.ylim(-0.2, 0.7)

plt.savefig('Tarea2_2.pdf')


#%%

#Tarea 3


#A5

with  open("summary_z1_A5.txt", "r") as infile:
    
    lines = infile.readlines()
    
    L_z1_A5: List[float] = []
    
    T_z1_A5: List[float] = []
    
    L_ext_z1_A5: List[float] = []
    
    T_ext_z1_A5: List[float] = []
    
    for line in lines:
        
        vals = line.split()
        
        if float(vals[1]) == 0.0 or float(vals[1]) == (5.657*5e9):
            
            T_ext_z1_A5.append(float(vals[5]))
            
            L_ext_z1_A5.append(float(vals[3]))
            
        if float(vals[1]) <= (5.657*5e9):
        
            T_z1_A5.append(float(vals[5]))
            
            L_z1_A5.append(float(vals[3]))
            
with  open("summary_z2_A5.txt", "r") as infile:
    
    lines = infile.readlines()
    
    L_z2_A5: List[float] = []
    
    T_z2_A5: List[float] = []
    
    L_ext_z2_A5: List[float] = []
    
    T_ext_z2_A5: List[float] = []
    
    for line in lines:
        
        vals = line.split()
        
        if float(vals[1]) == 0.0 or float(vals[1]) == (6.567*5e9):
            
            T_ext_z2_A5.append(float(vals[5]))
            
            L_ext_z2_A5.append(float(vals[3]))
            
        if float(vals[1]) <= (5.657*5e9):
            
            T_z2_A5.append(float(vals[5]))
            
            L_z2_A5.append(float(vals[3]))

with  open("summary_z3_A5.txt", "r") as infile:
    
    lines = infile.readlines()
    
    L_z3_A5: List[float] = []
    
    T_z3_A5: List[float] = []
    
    L_ext_z3_A5: List[float] = []
    
    T_ext_z3_A5: List[float] = []
    
    L_pp_A5: List[float] = []

    L_CNO_A5: List[float] = []
    
    for line in lines:
        
        vals = line.split()
        
        if float(vals[1]) == 0.0 or float(vals[1]) == (5.657*5e9):
            
            T_ext_z3_A5.append(float(vals[5]))
            
            L_ext_z3_A5.append(float(vals[3]))
            
        if float(vals[1]) <= (5.657*5e9):
            
            T_z3_A5.append(float(vals[5]))
            
            L_z3_A5.append(float(vals[3]))
            
            L_pp_A5.append(float(vals[18]))
            
            L_CNO_A5.append(float(vals[19]))

plt.figure()

plt.plot(T_z1_A5, L_z1_A5, color='blue', label='Z=0.001')
plt.plot(T_ext_z1_A5, L_ext_z1_A5, 'o', color='blue', label='Specified $\\tau$ for Z=0.001')
plt.plot(T_z2_A5, L_z2_A5, color='red', label='Z=0.02')
plt.plot(T_ext_z2_A5, L_ext_z2_A5, 'o', color='red', label='Specified $\\tau$ for Z=0.02')
plt.plot(T_z3_A5, L_z3_A5, color='purple', label='Z=0.03')
plt.plot(T_ext_z3_A5, L_ext_z3_A5, 'o', color='purple', label='Specified $\\tau$ for Z=0.03')
plt.plot(T, L, color='green', label='HR diagram')
plt.plot(T_esp[0], L_esp[0], 'o', color='black', label='A5')
plt.gca().invert_xaxis()
plt.title(r'HR diagram with $M=2M_\odot$')
plt.xlabel(r'Log$_{10}(T_e [K])$')
plt.ylabel(r'Log$_{10}(L [L_\odot])$')
plt.legend()
plt.grid()

plt.savefig('Tarea3_1_A5.pdf')

plt.figure()

plt.plot(T_z1_A5, L_z1_A5, color='blue', label='Z=0.001')
plt.plot(T_ext_z1_A5, L_ext_z1_A5, 'o', color='blue', label='Specified $\\tau$ for Z=0.001')
plt.plot(T_z2_A5, L_z2_A5, color='red', label='Z=0.02')
plt.plot(T_ext_z2_A5, L_ext_z2_A5, 'o', color='red', label='Specified $\\tau$ for Z=0.02')
plt.plot(T_z3_A5, L_z3_A5, color='purple', label='Z=0.03')
plt.plot(T_ext_z3_A5, L_ext_z3_A5, 'o', color='purple', label='Specified $\\tau$ for Z=0.03')
plt.plot(T, L, color='green', label='HR diagram')
plt.plot(T_esp[0], L_esp[0], 'o', color='black', label='A5')
plt.gca().invert_xaxis()
plt.title(r'HR diagram with $M=2M_\odot$')
plt.xlabel(r'Log$_{10}(T_e [K])$')
plt.ylabel(r'Log$_{10}(L [L_\odot])$')
plt.legend()
plt.grid()
plt.xlim(4.2, 3.4)
plt.ylim(0, 5)

plt.savefig('Tarea3_2_A5.pdf')


#F0

with  open("summary_z1_F0.txt", "r") as infile:
    
    lines = infile.readlines()
    
    L_z1_F0: List[float] = []
    
    T_z1_F0: List[float] = []
    
    L_ext_z1_F0: List[float] = []
    
    T_ext_z1_F0: List[float] = []
    
    for line in lines:
        
        vals = line.split()
        
        if float(vals[1]) == 0.0 or float(vals[1]) == (3.238*5e9):
            
            T_ext_z1_F0.append(float(vals[5]))
            
            L_ext_z1_F0.append(float(vals[3]))
            
        if float(vals[1]) <= (3.238*5e9):
            
            T_z1_F0.append(float(vals[5]))
            
            L_z1_F0.append(float(vals[3]))
            
with  open("summary_z2_F0.txt", "r") as infile:
    
    lines = infile.readlines()
    
    L_z2_F0: List[float] = []
    
    T_z2_F0: List[float] = []
    
    L_ext_z2_F0: List[float] = []
    
    T_ext_z2_F0: List[float] = []
    
    for line in lines:
        
        vals = line.split()
        
        if float(vals[1]) == 0.0 or float(vals[1]) == (5.657*5e9):
            
            T_ext_z2_F0.append(float(vals[5]))
            
            L_ext_z2_F0.append(float(vals[3]))
            
        if float(vals[1]) <= (3.238*5e9):
            
            T_z2_F0.append(float(vals[5]))
            
            L_z2_F0.append(float(vals[3]))

with  open("summary_z3_F0.txt", "r") as infile:
    
    lines = infile.readlines()
    
    L_z3_F0: List[float] = []
    
    T_z3_F0: List[float] = []
    
    L_ext_z3_F0: List[float] = []
    
    T_ext_z3_F0: List[float] = []
    
    L_pp_F0: List[float] = []

    L_CNO_F0: List[float] = []
    
    for line in lines:
        
        vals = line.split()
        
        if float(vals[1]) == 0.0 or float(vals[1]) == (5.657*5e9):
            
            T_ext_z3_F0.append(float(vals[5]))
            
            L_ext_z3_F0.append(float(vals[3]))
            
        if float(vals[1]) <= (3.238*5e9):
            
            T_z3_F0.append(float(vals[5]))
            
            L_z3_F0.append(float(vals[3]))
            
            L_pp_F0.append(float(vals[18]))
            
            L_CNO_F0.append(float(vals[19]))

plt.figure()

plt.plot(T_z1_F0, L_z1_F0, color='blue', label='Z=0.001')
plt.plot(T_ext_z1_F0, L_ext_z1_F0, 'o', color='blue', label='Specified $\\tau$ for Z=0.001')
plt.plot(T_z2_F0, L_z2_F0, color='red', label='Z=0.02')
plt.plot(T_ext_z2_F0, L_ext_z2_F0, 'o', color='red', label='Specified $\\tau$ for Z=0.02')
plt.plot(T_z3_F0, L_z3_F0, color='purple', label='Z=0.03')
plt.plot(T_ext_z3_F0, L_ext_z3_F0, 'o', color='purple', label='Specified $\\tau$ for Z=0.03')
plt.plot(T, L, color='green', label='HR diagram')
plt.plot(T_esp[1], L_esp[1], 'o', color='black', label='F0')
plt.gca().invert_xaxis()
plt.title(r'HR diagram with $M=1.6M_\odot$')
plt.xlabel(r'Log$_{10}(T_e [K])$')
plt.ylabel(r'Log$_{10}(L [L_\odot])$')
plt.legend()
plt.grid()

plt.savefig('Tarea3_1_F0.pdf')

plt.figure()

plt.plot(T_z1_F0, L_z1_F0, color='blue', label='Z=0.001')
plt.plot(T_ext_z1_F0, L_ext_z1_F0, 'o', color='blue', label='Specified $\\tau$ for Z=0.001')
plt.plot(T_z2_F0, L_z2_F0, color='red', label='Z=0.02')
plt.plot(T_ext_z2_F0, L_ext_z2_F0, 'o', color='red', label='Specified $\\tau$ for Z=0.02')
plt.plot(T_z3_F0, L_z3_F0, color='purple', label='Z=0.03')
plt.plot(T_ext_z3_F0, L_ext_z3_F0, 'o', color='purple', label='Specified $\\tau$ for Z=0.03')
plt.plot(T, L, color='green', label='HR diagram')
plt.plot(T_esp[1], L_esp[1], 'o', color='black', label='F0')
plt.gca().invert_xaxis()
plt.title(r'HR diagram with $M=1.6M_\odot$')
plt.xlabel(r'Log$_{10}(T_e [K])$')
plt.ylabel(r'Log$_{10}(L [L_\odot])$')
plt.legend()
plt.grid()
plt.xlim(4.1, 3.4)
plt.ylim(0, 5)

plt.savefig('Tarea3_2_F0.pdf')


#M0

with  open("summary_z1_M0.txt", "r") as infile:
    
    lines = infile.readlines()
    
    L_z1_M0: List[float] = []
    
    T_z1_M0: List[float] = []
    
    L_ext_z1_M0: List[float] = []
    
    T_ext_z1_M0: List[float] = []
    
    for line in lines:
        
        vals = line.split()
        
        if float(vals[1]) == 0.0 or float(vals[1]) == (0.186*5e9):
            
            T_ext_z1_M0.append(float(vals[5]))
            
            L_ext_z1_M0.append(float(vals[3]))
            
        T_z1_M0.append(float(vals[5]))
        
        L_z1_M0.append(float(vals[3]))
            
with  open("summary_z2_M0.txt", "r") as infile:
    
    lines = infile.readlines()
    
    L_z2_M0: List[float] = []
    
    T_z2_M0: List[float] = []
    
    L_ext_z2_M0: List[float] = []
    
    T_ext_z2_M0: List[float] = []
    
    for line in lines:
        
        vals = line.split()
        
        if float(vals[1]) == 0.0 or float(vals[1]) == (0.186*5e9):
            
            T_ext_z2_M0.append(float(vals[5]))
            
            L_ext_z2_M0.append(float(vals[3]))
            
        T_z2_M0.append(float(vals[5]))
        
        L_z2_M0.append(float(vals[3]))

with  open("summary_z3_M0.txt", "r") as infile:
    
    lines = infile.readlines()
    
    L_z3_M0: List[float] = []
    
    T_z3_M0: List[float] = []
    
    L_ext_z3_M0: List[float] = []
    
    T_ext_z3_M0: List[float] = []
    
    L_pp_M0: List[float] = []

    L_CNO_M0: List[float] = []
    
    for line in lines:
        
        vals = line.split()
        
        if float(vals[1]) == 0.0 or float(vals[1]) == (0.186*5e9):
            
            T_ext_z3_M0.append(float(vals[5]))
            
            L_ext_z3_M0.append(float(vals[3]))
            
        T_z3_M0.append(float(vals[5]))
        
        L_z3_M0.append(float(vals[3]))
            
        L_pp_M0.append(float(vals[18]))
        
        L_CNO_M0.append(float(vals[19]))

plt.figure()

plt.plot(T_z1_M0, L_z1_M0, color='blue', label='Z=0.001')
plt.plot(T_ext_z1_M0, L_ext_z1_M0, 'o', color='blue', label='Specified $\\tau$ for Z=0.001')
plt.plot(T_z2_M0, L_z2_M0, color='red', label='Z=0.02')
plt.plot(T_ext_z2_M0, L_ext_z2_M0, 'o', color='red', label='Specified $\\tau$ for Z=0.02')
plt.plot(T_z3_M0, L_z3_M0, color='purple', label='Z=0.03')
plt.plot(T_ext_z3_M0, L_ext_z3_M0, 'o', color='purple', label='Specified $\\tau$ for Z=0.03')
plt.plot(T, L, color='green', label='HR diagram')
plt.plot(T_esp[3], L_esp[3], 'o', color='black', label='M0')
plt.gca().invert_xaxis()
plt.title(r'HR diagram with $M=0.51M_\odot$')
plt.xlabel(r'Log$_{10}(T_e [K])$')
plt.ylabel(r'Log$_{10}(L [L_\odot])$')
plt.legend()
plt.grid()

plt.savefig('Tarea3_1_M0.pdf')

plt.figure()

plt.plot(T_z1_M0, L_z1_M0, color='blue', label='Z=0.001')
plt.plot(T_ext_z1_M0, L_ext_z1_M0, 'o', color='blue', label='Specified $\\tau$ for Z=0.001')
plt.plot(T_z2_M0, L_z2_M0, color='red', label='Z=0.02')
plt.plot(T_ext_z2_M0, L_ext_z2_M0, 'o', color='red', label='Specified $\\tau$ for Z=0.02')
plt.plot(T_z3_M0, L_z3_M0, color='purple', label='Z=0.03')
plt.plot(T_ext_z3_M0, L_ext_z3_M0, 'o', color='purple', label='Specified $\\tau$ for Z=0.03')
plt.plot(T, L, color='green', label='HR diagram')
plt.plot(T_esp[3], L_esp[3], 'o', color='black', label='M0')
plt.gca().invert_xaxis()
plt.title(r'HR diagram with $M=0.51M_\odot$')
plt.xlabel(r'Log$_{10}(T_e [K])$')
plt.ylabel(r'Log$_{10}(L [L_\odot])$')
plt.legend()
plt.grid()
plt.xlim(3.7, 3.5)
plt.ylim(-1.5, -1)

plt.savefig('Tarea3_2_M0.pdf')


#M5

with  open("summary_z1_M5.txt", "r") as infile:
    
    lines = infile.readlines()
    
    L_z1_M5: List[float] = []
    
    T_z1_M5: List[float] = []
    
    L_ext_z1_M5: List[float] = []
    
    T_ext_z1_M5: List[float] = []
    
    for line in lines:
        
        vals = line.split()
        
        if float(vals[1]) == 0.0 or float(vals[1]) == (0.02*5e9):
            
            T_ext_z1_M5.append(float(vals[5]))
            
            L_ext_z1_M5.append(float(vals[3]))
            
        T_z1_M5.append(float(vals[5]))
        
        L_z1_M5.append(float(vals[3]))
            
with  open("summary_z2_M5.txt", "r") as infile:
    
    lines = infile.readlines()
    
    M_z2_M5: List[float] = []
    
    L_z2_M5: List[float] = []
    
    T_z2_M5: List[float] = []
    
    L_ext_z2_M5: List[float] = []
    
    T_ext_z2_M5: List[float] = []
    
    M_ext_z2_M5: List[float] = []
    
    for line in lines:
        
        vals = line.split()
        
        if float(vals[1]) == 0.0 or float(vals[1]) == (0.02*5e9):
            
            T_ext_z2_M5.append(float(vals[5]))
            
            L_ext_z2_M5.append(float(vals[3]))
            
            M_ext_z2_M5.append(float(vals[2]))
            
        T_z2_M5.append(float(vals[5]))
        
        L_z2_M5.append(float(vals[3]))
        
        M_z2_M5.append(float(vals[2]))

with  open("summary_z3_M5.txt", "r") as infile:
    
    lines = infile.readlines()
    
    L_z3_M5: List[float] = []
    
    T_z3_M5: List[float] = []
    
    L_ext_z3_M5: List[float] = []
    
    T_ext_z3_M5: List[float] = []
    
    L_pp_M5: List[float] = []

    L_CNO_M5: List[float] = []
    
    for line in lines:
        
        vals = line.split()
        
        if float(vals[1]) == 0.0 or float(vals[1]) == (0.02*5e9):
            
            T_ext_z3_M5.append(float(vals[5]))
            
            L_ext_z3_M5.append(float(vals[3]))
            
        T_z3_M5.append(float(vals[5]))
        
        L_z3_M5.append(float(vals[3]))
            
        L_pp_M5.append(float(vals[18]))
        
        L_CNO_M5.append(float(vals[19]))

plt.figure()

plt.plot(T_z1_M5, L_z1_M5, color='blue', label='Z=0.001')
plt.plot(T_ext_z1_M5, L_ext_z1_M5, 'o', color='blue', label='Specified $\\tau$ for Z=0.001')
plt.plot(T_z2_M5, L_z2_M5, color='red', label='Z=0.02')
plt.plot(T_ext_z2_M5, L_ext_z2_M5, 'o', color='red', label='Specified $\\tau$ for Z=0.02')
plt.plot(T_z3_M5, L_z3_M5, color='purple', label='Z=0.03')
plt.plot(T_ext_z3_M5, L_ext_z3_M5, 'o', color='purple', label='Specified $\\tau$ for Z=0.03')
plt.plot(T, L, color='green', label='HR diagram')
plt.plot(T_esp[4], L_esp[4], 'o', color='black', label='M5')
plt.gca().invert_xaxis()
plt.title(r'HR diagram with $M=0.21M_\odot$')
plt.xlabel(r'Log$_{10}(T_e [K])$')
plt.ylabel(r'Log$_{10}(L [L_\odot])$')
plt.legend()
plt.grid()

plt.savefig('Tarea3_1_M5.pdf')

plt.figure()

plt.plot(T_z1_M5, L_z1_M5, color='blue', label='Z=0.001')
plt.plot(T_ext_z1_M5, L_ext_z1_M5, 'o', color='blue', label='Specified $\\tau$ for Z=0.001')
plt.plot(T_z2_M5, L_z2_M5, color='red', label='Z=0.02')
plt.plot(T_ext_z2_M5, L_ext_z2_M5, 'o', color='red', label='Specified $\\tau$ for Z=0.02')
plt.plot(T_z3_M5, L_z3_M5, color='purple', label='Z=0.03')
plt.plot(T_ext_z3_M5, L_ext_z3_M5, 'o', color='purple', label='Specified $\\tau$ for Z=0.03')
plt.plot(T, L, color='green', label='HR diagram')
plt.plot(T_esp[4], L_esp[4], 'o', color='black', label='M5')
plt.gca().invert_xaxis()
plt.title(r'HR diagram with $M=0.21M_\odot$')
plt.xlabel(r'Log$_{10}(T_e [K])$')
plt.ylabel(r'Log$_{10}(L [L_\odot])$')
plt.legend()
plt.grid()
plt.xlim(3.6, 3.475)
plt.ylim(-3, -1)

plt.savefig('Tarea3_2_M5.pdf')


#%%

#Tarea 4

delta_M0: List[float] = []

for i in range(0, len(T_z3_M0)):
    
    delta_M0.append(np.sqrt((T_z3_M0[i]-T_esp[3])**2+(L_z3_M0[i]-L_esp[3])**2))
    
min_M0: int = np.argmin(np.array(delta_M0))

delta_M5: List[float] = []

for i in range(0, len(T_z3_M5)):
    
    delta_M5.append(np.sqrt((T_z3_M5[i]-T_esp[4])**2+(L_z3_M5[i]-L_esp[4])**2))

min_M5: int = np.argmin(np.array(delta_M5))

L_pp: List[float] = [float((L_pp_A5[0])/10**(L_z3_A5[0])),\
                     float((L_pp_F0[0])/10**(L_z3_F0[0])),\
                     float((L_pp_s[-1])/10**(L_sun[-1])), \
                     float((L_pp_M0[int(min_M0)])/10**(L_z3_M0[int(min_M0)])),\
                     float((L_pp_M5[int(min_M5)])/10**(L_z3_M5[int(min_M5)]))]

L_CNO: List[float] = [float((L_CNO_A5[0])/10**(L_z3_A5[0])),\
                      float((L_CNO_F0[0])/10**(L_z3_F0[0])),\
                      float((L_CNO_s[-1])/10**(L_sun[-1])),\
                      float((L_CNO_M0[int(min_M0)])/10**(L_z3_M0[int(min_M0)])),\
                      float((L_CNO_M5[int(min_M5)])/10**(L_z3_M5[int(min_M5)]))]


plt.figure()

plt.plot(M_esp, L_pp, marker= 'o', color='red', label='pp chain')
plt.plot(M_esp, L_CNO, marker= 'o', color='blue', label='CNO cycle')
plt.title(r'Percentage of the soruce of luminosity')
plt.xlabel(r'$M [M_\odot]$')
plt.ylabel(r'$L_i/L$')
plt.legend()
plt.grid()

plt.savefig('Tarea4.pdf')
