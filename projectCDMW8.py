#CDM in class project
import numpy as np
import pandas as pd
import random
import string

#making nonsense list for abbas
abbas_expression = []
for x in range(500):
    output_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
    abbas_expression.append(output_string)


#create variables for dataframe
df = pd.DataFrame()                                                                                                                                                                     
N = 500                                                                                                                                                                                
df["ID"] = range(1,501)   
df["M4rk"] = [0]*N
df["Ch4d3au"] = [0]*N
df["S4br1na"] = np.random.uniform(700,9000, size = N)
df["R0dr1gu3s"] = np.random.uniform(700,9000, size = N)
df["Ab4s"] = np.random.choice(abbas_expression, size = N)
df["D3ng4n"] = np.random.choice(abbas_expression, size = N)
df["f111pos"] = np.random.uniform(700,2000, size = N)
df["f111p1d1s"] = np.random.uniform(700,2000, size = N)
df["J3ffr"] = np.random.uniform(700,2000, size = N)
df["34t0n"] = np.random.uniform(700,2000, size = N)

new_df = df.assign(case_status = df['S4br1na'] + df['R0dr1gu3s'] > 9000)
#jokes to hit:
#1 mark chadeau gene never expressed: we've never seen it.
#2 abas dengan gene expession is all gobbldegook: we're sure it's interesting but we couldn't understand it.
#4 name of the disease: crazy difficult masters, or CDM for short. 
#5 sufficent cause model for predicting CDM. When the sum of sabrina and rodrigues genes go over 9000, we predict a case. 

new_df.to_csv("C:/Users/username/Documents/0_Imperial/CDM/CDM_Coursework2/CDM_Coursework2/genex_and_case.csv")

