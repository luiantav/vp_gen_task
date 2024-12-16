import numpy as np
from numpy import random
import seaborn as sns
import os
import pandas as pd
import numpy.matlib

output_file = "sequences_gen"
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
gen_blocks = 2
gen_trials_p_block = 18
n_gen = 9 
gen_code = 4
gen_columns = ["trial_n", "gen","condition", "task","ITI","ISI","block"]
gen_trial_dimension = 7



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



# GENERALISATION: Sample = gen_C1_1_ID1
trial_n =  list(range(1, gen_trials_p_block+1))
gen_unique = list(range(0,n_gen))
gen = np.repeat(gen_unique, (gen_trials_p_block/n_gen))


for ID in range(1,ID_total):
    for j in range(1,(gen_blocks +1)):
        globals()['Gen_C1_%s' % j] = np.full([gen_trials_p_block,gen_trial_dimension], None) 
        control_gen(gen)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, gen_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, gen_trials_p_block))

        for i in range(gen_trials_p_block):
            globals()['Gen_C1_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Gen_C1_%s' % j][[i],[1]] = gen[(i)]
            globals()['Gen_C1_%s' % j][[i],[2]] = 0
            globals()['Gen_C1_%s' % j][[i],[3]] = 4 #task
            globals()['Gen_C1_%s' % j][[i],[4]] = ITI[(i)]
            globals()['Gen_C1_%s' % j][[i],[5]] = SOI[(i)]
            globals()['Gen_C1_%s' % j][[i],[6]] = j #block

#save copy to then save to csv

        globals()['SGen_C1_%s' % j] = np.copy(globals()['Gen_C1_%s' % j]) 


#make it pretty and compatible with jsPsych input format needed
        globals()['Gen_C1_%s' % j] = str(globals()['Gen_C1_%s' % j]).replace('.0 ', ',')
        globals()['Gen_C1_%s' % j] = str(globals()['Gen_C1_%s' % j]).replace(',]',']')
        globals()['Gen_C1_%s' % j] = str(globals()['Gen_C1_%s' % j]).replace('\n',',')
        globals()['Gen_C1_%s' % j] = str(globals()['Gen_C1_%s' % j]).replace('],]',']]')
        globals()['Gen_C1_%s' % j] = str(globals()['Gen_C1_%s' % j]).replace(', ',',')
        globals()['Gen_C1_%s' % j] = str(globals()['Gen_C1_%s' % j]).replace(']]',']],')
        globals()['Gen_C1_%s' % j] = str(globals()['Gen_C1_%s' % j]).replace(' ',',')
        globals()['Gen_C1_%s' % j] = str(globals()['Gen_C1_%s' % j]).replace('.0]', ']')


        for x in range(gen_trials_p_block):
            globals()['Gen_C1_%s' % j] = str(globals()['Gen_C1_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')

    for j in range(1,(gen_blocks +1)):
        globals()['Gen_C2_%s' % j] = np.full([gen_trials_p_block,gen_trial_dimension], None) 
        control_gen(gen)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, gen_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, gen_trials_p_block))

        for i in range(gen_trials_p_block):
            globals()['Gen_C2_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Gen_C2_%s' % j][[i],[1]] = gen[(i)]
            globals()['Gen_C2_%s' % j][[i],[2]] = 1
            globals()['Gen_C2_%s' % j][[i],[3]] = 4 #task
            globals()['Gen_C2_%s' % j][[i],[4]] = ITI[(i)]
            globals()['Gen_C2_%s' % j][[i],[5]] = SOI[(i)]
            globals()['Gen_C2_%s' % j][[i],[6]] = j #block

#save copy to then save to csv

        globals()['SGen_C2_%s' % j] = np.copy(globals()['Gen_C2_%s' % j]) 


#make it pretty and compatible with jsPsych input format needed
        globals()['Gen_C2_%s' % j] = str(globals()['Gen_C2_%s' % j]).replace('.0 ', ',')
        globals()['Gen_C2_%s' % j] = str(globals()['Gen_C2_%s' % j]).replace(',]',']')
        globals()['Gen_C2_%s' % j] = str(globals()['Gen_C2_%s' % j]).replace('\n',',')
        globals()['Gen_C2_%s' % j] = str(globals()['Gen_C2_%s' % j]).replace('],]',']]')
        globals()['Gen_C2_%s' % j] = str(globals()['Gen_C2_%s' % j]).replace(', ',',')
        globals()['Gen_C2_%s' % j] = str(globals()['Gen_C2_%s' % j]).replace(']]',']],')
        globals()['Gen_C2_%s' % j] = str(globals()['Gen_C2_%s' % j]).replace(' ',',')
        globals()['Gen_C2_%s' % j] = str(globals()['Gen_C2_%s' % j]).replace('.0]', ']')


        for x in range(gen_trials_p_block):
            globals()['Gen_C2_%s' % j] = str(globals()['Gen_C2_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')

    for j in range(1,(gen_blocks +1)):
        globals()['Gen_C3_%s' % j] = np.full([gen_trials_p_block,gen_trial_dimension], None) 
        control_gen(gen)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, gen_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, gen_trials_p_block))

        for i in range(gen_trials_p_block):
            globals()['Gen_C3_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Gen_C3_%s' % j][[i],[1]] = gen[(i)]
            globals()['Gen_C3_%s' % j][[i],[2]] = 2
            globals()['Gen_C3_%s' % j][[i],[3]] = 4 #task
            globals()['Gen_C3_%s' % j][[i],[4]] = ITI[(i)]
            globals()['Gen_C3_%s' % j][[i],[5]] = SOI[(i)]
            globals()['Gen_C3_%s' % j][[i],[6]] = j #block

#save copy to then save to csv

        globals()['SGen_C3_%s' % j] = np.copy(globals()['Gen_C3_%s' % j]) 


#make it pretty and compatible with jsPsych input format needed
        globals()['Gen_C3_%s' % j] = str(globals()['Gen_C3_%s' % j]).replace('.0 ', ',')
        globals()['Gen_C3_%s' % j] = str(globals()['Gen_C3_%s' % j]).replace(',]',']')
        globals()['Gen_C3_%s' % j] = str(globals()['Gen_C3_%s' % j]).replace('\n',',')
        globals()['Gen_C3_%s' % j] = str(globals()['Gen_C3_%s' % j]).replace('],]',']]')
        globals()['Gen_C3_%s' % j] = str(globals()['Gen_C3_%s' % j]).replace(', ',',')
        globals()['Gen_C3_%s' % j] = str(globals()['Gen_C3_%s' % j]).replace(']]',']],')
        globals()['Gen_C3_%s' % j] = str(globals()['Gen_C3_%s' % j]).replace(' ',',')
        globals()['Gen_C3_%s' % j] = str(globals()['Gen_C3_%s' % j]).replace('.0]', ']')


        for x in range(gen_trials_p_block):
            globals()['Gen_C3_%s' % j] = str(globals()['Gen_C3_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')

    for j in range(1,(gen_blocks +1)):
        globals()['Gen_C4_%s' % j] = np.full([gen_trials_p_block,gen_trial_dimension], None) 
        control_gen(gen)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, gen_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, gen_trials_p_block))

        for i in range(gen_trials_p_block):
            globals()['Gen_C4_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Gen_C4_%s' % j][[i],[1]] = gen[(i)]
            globals()['Gen_C4_%s' % j][[i],[2]] = 3
            globals()['Gen_C4_%s' % j][[i],[3]] = 4 #task
            globals()['Gen_C4_%s' % j][[i],[4]] = ITI[(i)]
            globals()['Gen_C4_%s' % j][[i],[5]] = SOI[(i)]
            globals()['Gen_C4_%s' % j][[i],[6]] = j #block

#save copy to then save to csv

        globals()['SGen_C4_%s' % j] = np.copy(globals()['Gen_C4_%s' % j]) 


#make it pretty and compatible with jsPsych input format needed
        globals()['Gen_C4_%s' % j] = str(globals()['Gen_C4_%s' % j]).replace('.0 ', ',')
        globals()['Gen_C4_%s' % j] = str(globals()['Gen_C4_%s' % j]).replace(',]',']')
        globals()['Gen_C4_%s' % j] = str(globals()['Gen_C4_%s' % j]).replace('\n',',')
        globals()['Gen_C4_%s' % j] = str(globals()['Gen_C4_%s' % j]).replace('],]',']]')
        globals()['Gen_C4_%s' % j] = str(globals()['Gen_C4_%s' % j]).replace(', ',',')
        globals()['Gen_C4_%s' % j] = str(globals()['Gen_C4_%s' % j]).replace(']]',']],')
        globals()['Gen_C4_%s' % j] = str(globals()['Gen_C4_%s' % j]).replace(' ',',')
        globals()['Gen_C4_%s' % j] = str(globals()['Gen_C4_%s' % j]).replace('.0]', ']')


        for x in range(gen_trials_p_block):
            globals()['Gen_C4_%s' % j] = str(globals()['Gen_C4_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')

    for j in range(1,(gen_blocks +1)):
        globals()['Gen_C5_%s' % j] = np.full([gen_trials_p_block,gen_trial_dimension], None) 
        control_gen(gen)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, gen_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, gen_trials_p_block))

        for i in range(gen_trials_p_block):
            globals()['Gen_C5_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Gen_C5_%s' % j][[i],[1]] = gen[(i)]
            globals()['Gen_C5_%s' % j][[i],[2]] = 4
            globals()['Gen_C5_%s' % j][[i],[3]] = 4 #task
            globals()['Gen_C5_%s' % j][[i],[4]] = ITI[(i)]
            globals()['Gen_C5_%s' % j][[i],[5]] = SOI[(i)]
            globals()['Gen_C5_%s' % j][[i],[6]] = j #block

#save copy to then save to csv

        globals()['SGen_C5_%s' % j] = np.copy(globals()['Gen_C5_%s' % j]) 


#make it pretty and compatible with jsPsych input format needed
        globals()['Gen_C5_%s' % j] = str(globals()['Gen_C5_%s' % j]).replace('.0 ', ',')
        globals()['Gen_C5_%s' % j] = str(globals()['Gen_C5_%s' % j]).replace(',]',']')
        globals()['Gen_C5_%s' % j] = str(globals()['Gen_C5_%s' % j]).replace('\n',',')
        globals()['Gen_C5_%s' % j] = str(globals()['Gen_C5_%s' % j]).replace('],]',']]')
        globals()['Gen_C5_%s' % j] = str(globals()['Gen_C5_%s' % j]).replace(', ',',')
        globals()['Gen_C5_%s' % j] = str(globals()['Gen_C5_%s' % j]).replace(']]',']],')
        globals()['Gen_C5_%s' % j] = str(globals()['Gen_C5_%s' % j]).replace(' ',',')
        globals()['Gen_C5_%s' % j] = str(globals()['Gen_C5_%s' % j]).replace('.0]', ']')


        for x in range(gen_trials_p_block):
            globals()['Gen_C5_%s' % j] = str(globals()['Gen_C5_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')


    for j in range(1,(gen_blocks +1)):
        globals()['Gen_C6_%s' % j] = np.full([gen_trials_p_block,gen_trial_dimension], None) 
        control_gen(gen)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, gen_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, gen_trials_p_block))

        for i in range(gen_trials_p_block):
            globals()['Gen_C6_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Gen_C6_%s' % j][[i],[1]] = gen[(i)]
            globals()['Gen_C6_%s' % j][[i],[2]] = 5
            globals()['Gen_C6_%s' % j][[i],[3]] = 4 #task
            globals()['Gen_C6_%s' % j][[i],[4]] = ITI[(i)]
            globals()['Gen_C6_%s' % j][[i],[5]] = SOI[(i)]
            globals()['Gen_C6_%s' % j][[i],[6]] = j #block

#save copy to then save to csv

        globals()['SGen_C6_%s' % j] = np.copy(globals()['Gen_C6_%s' % j]) 


#make it pretty and compatible with jsPsych input format needed
        globals()['Gen_C6_%s' % j] = str(globals()['Gen_C6_%s' % j]).replace('.0 ', ',')
        globals()['Gen_C6_%s' % j] = str(globals()['Gen_C6_%s' % j]).replace(',]',']')
        globals()['Gen_C6_%s' % j] = str(globals()['Gen_C6_%s' % j]).replace('\n',',')
        globals()['Gen_C6_%s' % j] = str(globals()['Gen_C6_%s' % j]).replace('],]',']]')
        globals()['Gen_C6_%s' % j] = str(globals()['Gen_C6_%s' % j]).replace(', ',',')
        globals()['Gen_C6_%s' % j] = str(globals()['Gen_C6_%s' % j]).replace(']]',']],')
        globals()['Gen_C6_%s' % j] = str(globals()['Gen_C6_%s' % j]).replace(' ',',')
        globals()['Gen_C6_%s' % j] = str(globals()['Gen_C6_%s' % j]).replace('.0]', ']')


        for x in range(gen_trials_p_block):
            globals()['Gen_C6_%s' % j] = str(globals()['Gen_C6_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')


    if (ID == 1):
        f.write("var vars = { ")

# write to .js file, block for block
    for j in range(1,(gen_blocks+1)):
        f.write("\n")
        f.write("'Gen_C1_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Gen_C1_%s' % j])) #write to file
        f.write("'Gen_C2_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Gen_C2_%s' % j])) #write to file
        f.write("'Gen_C3_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Gen_C3_%s' % j])) #write to file
        f.write("'Gen_C4_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Gen_C4_%s' % j])) #write to file
        f.write("'Gen_C5_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Gen_C5_%s' % j])) #write to file
        f.write("'Gen_C6_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Gen_C6_%s' % j])) #write to file


# write to csv
    
    sgen = np.concatenate((SGen_C1_1, SGen_C2_1))
    sgen = np.concatenate((sgen, SGen_C3_1))
    sgen = np.concatenate((sgen, SGen_C4_1))
    sgen = np.concatenate((sgen, SGen_C5_1))
    sgen = np.concatenate((sgen, SGen_C6_1))

    for j in range(2,gen_blocks+1):
        sgen = np.append(sgen, globals()['SGen_C1_%s' % j])
        sgen = np.append(sgen, globals()['SGen_C2_%s' % j])
        sgen = np.append(sgen, globals()['SGen_C3_%s' % j])
        sgen = np.append(sgen, globals()['SGen_C4_%s' % j])
        sgen = np.append(sgen, globals()['SGen_C5_%s' % j])
        sgen = np.append(sgen, globals()['SGen_C6_%s' % j])


    sgen = sgen.reshape(((gen_blocks*gen_trials_p_block)*6), gen_trial_dimension)
    sgen_df = pd.DataFrame(sgen, columns=[gen_columns])
    sgen_df = sgen_df.astype(str)
    sgen_df= sgen_df.replace(to_replace = "\.0+$",value = "", regex = True)
    sgen_df.to_csv("ID_"+str(ID)+"/Gen_ID" + str(ID)+".csv", index=False)

