import numpy as np
from numpy import random
import seaborn as sns
import os
import pandas as pd
import numpy.matlib

output_file = "sequences_snap"
f = open(output_file+".js", "a") # create/open output file #a

# Set parameters
ID = 1 #how many sequence files +1 do we want
ID_total = 25 #how many ID's in total

if (ID == 1):
    for i in range(1,ID_total+1):
        os.makedirs("ID_"+str(i))


# parameters for ITI/SOI
bounds = [0.250,1.0] #[0.750,3]
target_lam = 0.5 #is lambda, not mean

#parameters for generalisation task 
snap_blocks = 2
snap_trials_p_block = 16
gen_comp = 8
n_gen = 9 
snap_code = 9
snap_columns = ["trial_n", "gen1","gen2","choice","order","condition", "task","ITI","ISI","block"]
snap_trial_dimension = 10



# functions

#iti and isi
def generate_trunc_exp_distrLAM(bounds, lam, n, perc=0.05, lim=0.35):
    samples_upper = n*perc # how many should be in upper segment
    upper = samples_upper-1
    upper_limit = bounds[1] - (bounds[1]-bounds[0])*lim #upper boundary
    i = 1
    while (i < 30) & (upper < samples_upper): #if rule is not met, repeat
        vals = bounds[0] + np.random.exponential(lam, n*2)
        vals = vals[vals<bounds[1]]
        vals = np.random.choice(vals, n, replace=False)
        upper = len(vals[vals>upper_limit]) #check if it's the case
        i = i+1
    vals = vals*1000
    return vals



# shuffle function to prevent that more then 2 consecutive choices are the same
def shuffle(arr):
    arr = np.take(arr,np.random.permutation(arr.shape[0]),axis=0,out=arr);
    

# function to check that unc. is balanced
def control_gen(arr):
    arr = np.take(arr,np.random.permutation(arr.shape[0]),axis=0,out=arr);
    while 'try_again':
        if (any(i==j==k for i,j,k in zip(arr, arr[1:], arr[2:]))):
            arr = np.take(arr,np.random.permutation(arr.shape[0]),axis=0,out=arr);
            print('try_again')
        else:
            print('yey')
            break



# GENERALISATION: Sample = snap_C1_1_ID1
trial_n =  list(range(1, snap_trials_p_block+1))
gen_unique = list(range(0,gen_comp))

gen = np.tile(gen_unique, 2)
sameness = np.ones(snap_trials_p_block)
ratio = int(snap_trials_p_block/2)
sameness[:ratio] = 0

order = np.ones(snap_trials_p_block)
order[:ratio] = 0
order = np.take(order,np.random.permutation(order.shape[0]),axis=0,out=order);
gen2 = gen + 1

temp_arr = pd.DataFrame({'GS1': gen, 'GS2': gen2, 'sameness': sameness,'order': order})
temp2 = temp_arr.sample(frac=1).reset_index(drop=True)
gen1 = temp2["GS1"].values
gen2 = temp2["GS2"].values
sameness = temp2["sameness"].values
order = temp2["order"].values




for ID in range(1,ID_total):
    for j in range(1,(snap_blocks +1)):
        globals()['Snap_C1_%s' % j] = np.full([snap_trials_p_block,snap_trial_dimension], None) 
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, snap_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, snap_trials_p_block))
        #control_gen(gen)
        #control_gen(sameness)
        #control_gen(order)
        for i in range(snap_trials_p_block):
            globals()['Snap_C1_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Snap_C1_%s' % j][[i],[1]] = gen1[(i)]
            globals()['Snap_C1_%s' % j][[i],[2]] = gen2[(i)]
            globals()['Snap_C1_%s' % j][[i],[3]] = sameness[(i)]
            globals()['Snap_C1_%s' % j][[i],[4]] = order[(i)]
            globals()['Snap_C1_%s' % j][[i],[5]] = 0
            globals()['Snap_C1_%s' % j][[i],[6]] = 9
            globals()['Snap_C1_%s' % j][[i],[7]] = ITI[(i)]
            globals()['Snap_C1_%s' % j][[i],[8]] = SOI[(i)]
            globals()['Snap_C1_%s' % j][[i],[9]] = j #block

#save copy to then save to csv

        globals()['SSnap_C1_%s' % j] = np.copy(globals()['Snap_C1_%s' % j]) 


#make it pretty and compatible with jsPsych input format needed
        globals()['Snap_C1_%s' % j] = str(globals()['Snap_C1_%s' % j]).replace('.0 ', ',')
        globals()['Snap_C1_%s' % j] = str(globals()['Snap_C1_%s' % j]).replace(',]',']')
        globals()['Snap_C1_%s' % j] = str(globals()['Snap_C1_%s' % j]).replace('\n',',')
        globals()['Snap_C1_%s' % j] = str(globals()['Snap_C1_%s' % j]).replace('],]',']]')
        globals()['Snap_C1_%s' % j] = str(globals()['Snap_C1_%s' % j]).replace(', ',',')
        globals()['Snap_C1_%s' % j] = str(globals()['Snap_C1_%s' % j]).replace(']]',']],')
        globals()['Snap_C1_%s' % j] = str(globals()['Snap_C1_%s' % j]).replace(' ',',')
        globals()['Snap_C1_%s' % j] = str(globals()['Snap_C1_%s' % j]).replace('.0]', ']')


        for x in range(snap_trials_p_block):
            globals()['Snap_C1_%s' % j] = str(globals()['Snap_C1_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')

    
    for j in range(1,(snap_blocks +1)):
        globals()['Snap_C2_%s' % j] = np.full([snap_trials_p_block,snap_trial_dimension], None) 
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, snap_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, snap_trials_p_block))
        for i in range(snap_trials_p_block):
            globals()['Snap_C2_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Snap_C2_%s' % j][[i],[1]] = gen1[(i)]
            globals()['Snap_C2_%s' % j][[i],[2]] = gen2[(i)]
            globals()['Snap_C2_%s' % j][[i],[3]] = sameness[(i)]
            globals()['Snap_C2_%s' % j][[i],[4]] = order[(i)]
            globals()['Snap_C2_%s' % j][[i],[5]] = 1
            globals()['Snap_C2_%s' % j][[i],[6]] = 9
            globals()['Snap_C2_%s' % j][[i],[7]] = ITI[(i)]
            globals()['Snap_C2_%s' % j][[i],[8]] = SOI[(i)]
            globals()['Snap_C2_%s' % j][[i],[9]] = j #block

#save copy to then save to csv

        globals()['SSnap_C2_%s' % j] = np.copy(globals()['Snap_C2_%s' % j]) 


#make it pretty and compatible with jsPsych input format needed
        globals()['Snap_C2_%s' % j] = str(globals()['Snap_C2_%s' % j]).replace('.0 ', ',')
        globals()['Snap_C2_%s' % j] = str(globals()['Snap_C2_%s' % j]).replace(',]',']')
        globals()['Snap_C2_%s' % j] = str(globals()['Snap_C2_%s' % j]).replace('\n',',')
        globals()['Snap_C2_%s' % j] = str(globals()['Snap_C2_%s' % j]).replace('],]',']]')
        globals()['Snap_C2_%s' % j] = str(globals()['Snap_C2_%s' % j]).replace(', ',',')
        globals()['Snap_C2_%s' % j] = str(globals()['Snap_C2_%s' % j]).replace(']]',']],')
        globals()['Snap_C2_%s' % j] = str(globals()['Snap_C2_%s' % j]).replace(' ',',')
        globals()['Snap_C2_%s' % j] = str(globals()['Snap_C2_%s' % j]).replace('.0]', ']')


        for x in range(snap_trials_p_block):
            globals()['Snap_C2_%s' % j] = str(globals()['Snap_C2_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')


    for j in range(1,(snap_blocks +1)):
        globals()['Snap_C3_%s' % j] = np.full([snap_trials_p_block,snap_trial_dimension], None) 
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, snap_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, snap_trials_p_block))

        for i in range(snap_trials_p_block):
            globals()['Snap_C3_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Snap_C3_%s' % j][[i],[1]] = gen1[(i)]
            globals()['Snap_C3_%s' % j][[i],[2]] = gen2[(i)]
            globals()['Snap_C3_%s' % j][[i],[3]] = sameness[(i)]
            globals()['Snap_C3_%s' % j][[i],[4]] = order[(i)]
            globals()['Snap_C3_%s' % j][[i],[5]] = 2
            globals()['Snap_C3_%s' % j][[i],[6]] = 9
            globals()['Snap_C3_%s' % j][[i],[7]] = ITI[(i)]
            globals()['Snap_C3_%s' % j][[i],[8]] = SOI[(i)]
            globals()['Snap_C3_%s' % j][[i],[9]] = j #block

#save copy to then save to csv

        globals()['SSnap_C3_%s' % j] = np.copy(globals()['Snap_C3_%s' % j]) 


#make it pretty and compatible with jsPsych input format needed
        globals()['Snap_C3_%s' % j] = str(globals()['Snap_C3_%s' % j]).replace('.0 ', ',')
        globals()['Snap_C3_%s' % j] = str(globals()['Snap_C3_%s' % j]).replace(',]',']')
        globals()['Snap_C3_%s' % j] = str(globals()['Snap_C3_%s' % j]).replace('\n',',')
        globals()['Snap_C3_%s' % j] = str(globals()['Snap_C3_%s' % j]).replace('],]',']]')
        globals()['Snap_C3_%s' % j] = str(globals()['Snap_C3_%s' % j]).replace(', ',',')
        globals()['Snap_C3_%s' % j] = str(globals()['Snap_C3_%s' % j]).replace(']]',']],')
        globals()['Snap_C3_%s' % j] = str(globals()['Snap_C3_%s' % j]).replace(' ',',')
        globals()['Snap_C3_%s' % j] = str(globals()['Snap_C3_%s' % j]).replace('.0]', ']')


        for x in range(snap_trials_p_block):
            globals()['Snap_C3_%s' % j] = str(globals()['Snap_C3_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')


    for j in range(1,(snap_blocks +1)):
        globals()['Snap_C4_%s' % j] = np.full([snap_trials_p_block,snap_trial_dimension], None) 
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, snap_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, snap_trials_p_block))

        for i in range(snap_trials_p_block):
            globals()['Snap_C4_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Snap_C4_%s' % j][[i],[1]] = gen1[(i)]
            globals()['Snap_C4_%s' % j][[i],[2]] = gen2[(i)]
            globals()['Snap_C4_%s' % j][[i],[3]] = sameness[(i)]
            globals()['Snap_C4_%s' % j][[i],[4]] = order[(i)]
            globals()['Snap_C4_%s' % j][[i],[5]] = 3
            globals()['Snap_C4_%s' % j][[i],[6]] = 9
            globals()['Snap_C4_%s' % j][[i],[7]] = ITI[(i)]
            globals()['Snap_C4_%s' % j][[i],[8]] = SOI[(i)]
            globals()['Snap_C4_%s' % j][[i],[9]] = j #block

#save copy to then save to csv

        globals()['SSnap_C4_%s' % j] = np.copy(globals()['Snap_C4_%s' % j]) 


#make it pretty and compatible with jsPsych input format needed
        globals()['Snap_C4_%s' % j] = str(globals()['Snap_C4_%s' % j]).replace('.0 ', ',')
        globals()['Snap_C4_%s' % j] = str(globals()['Snap_C4_%s' % j]).replace(',]',']')
        globals()['Snap_C4_%s' % j] = str(globals()['Snap_C4_%s' % j]).replace('\n',',')
        globals()['Snap_C4_%s' % j] = str(globals()['Snap_C4_%s' % j]).replace('],]',']]')
        globals()['Snap_C4_%s' % j] = str(globals()['Snap_C4_%s' % j]).replace(', ',',')
        globals()['Snap_C4_%s' % j] = str(globals()['Snap_C4_%s' % j]).replace(']]',']],')
        globals()['Snap_C4_%s' % j] = str(globals()['Snap_C4_%s' % j]).replace(' ',',')
        globals()['Snap_C4_%s' % j] = str(globals()['Snap_C4_%s' % j]).replace('.0]', ']')


        for x in range(snap_trials_p_block):
            globals()['Snap_C4_%s' % j] = str(globals()['Snap_C4_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')



    for j in range(1,(snap_blocks +1)):
        globals()['Snap_C5_%s' % j] = np.full([snap_trials_p_block,snap_trial_dimension], None) 
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, snap_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, snap_trials_p_block))
        for i in range(snap_trials_p_block):
            globals()['Snap_C5_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Snap_C5_%s' % j][[i],[1]] = gen1[(i)]
            globals()['Snap_C5_%s' % j][[i],[2]] = gen2[(i)]
            globals()['Snap_C5_%s' % j][[i],[3]] = sameness[(i)]
            globals()['Snap_C5_%s' % j][[i],[4]] = order[(i)]
            globals()['Snap_C5_%s' % j][[i],[5]] = 4
            globals()['Snap_C5_%s' % j][[i],[6]] = 9
            globals()['Snap_C5_%s' % j][[i],[7]] = ITI[(i)]
            globals()['Snap_C5_%s' % j][[i],[8]] = SOI[(i)]
            globals()['Snap_C5_%s' % j][[i],[9]] = j #block

#save copy to then save to csv

        globals()['SSnap_C5_%s' % j] = np.copy(globals()['Snap_C5_%s' % j]) 


#make it pretty and compatible with jsPsych input format needed
        globals()['Snap_C5_%s' % j] = str(globals()['Snap_C5_%s' % j]).replace('.0 ', ',')
        globals()['Snap_C5_%s' % j] = str(globals()['Snap_C5_%s' % j]).replace(',]',']')
        globals()['Snap_C5_%s' % j] = str(globals()['Snap_C5_%s' % j]).replace('\n',',')
        globals()['Snap_C5_%s' % j] = str(globals()['Snap_C5_%s' % j]).replace('],]',']]')
        globals()['Snap_C5_%s' % j] = str(globals()['Snap_C5_%s' % j]).replace(', ',',')
        globals()['Snap_C5_%s' % j] = str(globals()['Snap_C5_%s' % j]).replace(']]',']],')
        globals()['Snap_C5_%s' % j] = str(globals()['Snap_C5_%s' % j]).replace(' ',',')
        globals()['Snap_C5_%s' % j] = str(globals()['Snap_C5_%s' % j]).replace('.0]', ']')


        for x in range(snap_trials_p_block):
            globals()['Snap_C5_%s' % j] = str(globals()['Snap_C5_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')


    for j in range(1,(snap_blocks +1)):
        globals()['Snap_C6_%s' % j] = np.full([snap_trials_p_block,snap_trial_dimension], None) 
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, snap_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, snap_trials_p_block))

        for i in range(snap_trials_p_block):
            globals()['Snap_C6_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Snap_C6_%s' % j][[i],[1]] = gen1[(i)]
            globals()['Snap_C6_%s' % j][[i],[2]] = gen2[(i)]
            globals()['Snap_C6_%s' % j][[i],[3]] = sameness[(i)]
            globals()['Snap_C6_%s' % j][[i],[4]] = order[(i)]
            globals()['Snap_C6_%s' % j][[i],[5]] = 5
            globals()['Snap_C6_%s' % j][[i],[6]] = 9
            globals()['Snap_C6_%s' % j][[i],[7]] = ITI[(i)]
            globals()['Snap_C6_%s' % j][[i],[8]] = SOI[(i)]
            globals()['Snap_C6_%s' % j][[i],[9]] = j #block

#save copy to then save to csv

        globals()['SSnap_C6_%s' % j] = np.copy(globals()['Snap_C6_%s' % j]) 


#make it pretty and compatible with jsPsych input format needed
        globals()['Snap_C6_%s' % j] = str(globals()['Snap_C6_%s' % j]).replace('.0 ', ',')
        globals()['Snap_C6_%s' % j] = str(globals()['Snap_C6_%s' % j]).replace(',]',']')
        globals()['Snap_C6_%s' % j] = str(globals()['Snap_C6_%s' % j]).replace('\n',',')
        globals()['Snap_C6_%s' % j] = str(globals()['Snap_C6_%s' % j]).replace('],]',']]')
        globals()['Snap_C6_%s' % j] = str(globals()['Snap_C6_%s' % j]).replace(', ',',')
        globals()['Snap_C6_%s' % j] = str(globals()['Snap_C6_%s' % j]).replace(']]',']],')
        globals()['Snap_C6_%s' % j] = str(globals()['Snap_C6_%s' % j]).replace(' ',',')
        globals()['Snap_C6_%s' % j] = str(globals()['Snap_C6_%s' % j]).replace('.0]', ']')


        for x in range(snap_trials_p_block):
            globals()['Snap_C6_%s' % j] = str(globals()['Snap_C6_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')



    if (ID == 1):
        f.write("var vars = { ")

# write to .js file, block for block
    for j in range(1,(snap_blocks+1)):
        f.write("\n")
        f.write("'Snap_C1_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Snap_C1_%s' % j])) #write to file
        f.write("'Snap_C2_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Snap_C2_%s' % j])) #write to file
        f.write("'Snap_C3_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Snap_C3_%s' % j])) #write to file
        f.write("'Snap_C4_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Snap_C4_%s' % j])) #write to file
        f.write("'Snap_C5_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Snap_C5_%s' % j])) #write to file
        f.write("'Snap_C6_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Snap_C6_%s' % j])) #write to file


# write to csv
    
    ssnap = np.concatenate((SSnap_C1_1, SSnap_C2_1))
    ssnap = np.concatenate((ssnap, SSnap_C3_1))
    ssnap = np.concatenate((ssnap, SSnap_C4_1))
    ssnap = np.concatenate((ssnap, SSnap_C5_1))
    ssnap = np.concatenate((ssnap, SSnap_C6_1))

    for j in range(2,snap_blocks+1):
        ssnap = np.append(ssnap, globals()['SSnap_C1_%s' % j])
        ssnap = np.append(ssnap, globals()['SSnap_C2_%s' % j])
        ssnap = np.append(ssnap, globals()['SSnap_C3_%s' % j])
        ssnap = np.append(ssnap, globals()['SSnap_C4_%s' % j])
        ssnap = np.append(ssnap, globals()['SSnap_C5_%s' % j])
        ssnap = np.append(ssnap, globals()['SSnap_C6_%s' % j])


    ssnap = ssnap.reshape(((snap_blocks*snap_trials_p_block)*6), snap_trial_dimension)
    ssnap_df = pd.DataFrame(ssnap, columns=[snap_columns])
    ssnap_df = ssnap_df.astype(str)
    ssnap_df= ssnap_df.replace(to_replace = "\.0+$",value = "", regex = True)
    ssnap_df.to_csv("ID_"+str(ID)+"/Snap_ID" + str(ID)+".csv", index=False)

