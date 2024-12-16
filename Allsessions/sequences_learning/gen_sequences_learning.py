import numpy as np
from numpy import random
import seaborn as sns
import os
import pandas as pd
import numpy.matlib

output_file = "sequences_learning"
f = open(output_file+".js", "a") # create/open output file #a

# Set parameters
ID = 1 #how many sequence files +1 do we want
ID_total = 25 #how many ID's in total

if (ID == 1):
    for i in range(1,ID_total+1):
        os.makedirs("ID_"+str(i))


# parameters for ITI/SOI
bounds = [0.75, 1.5] #[0.250,1.0] #[0.750,3]
target_lam = 0.5 #is lambda, not mean

#parameters for learning task 
learn_blocks = 2
learn_trials_p_block = 12
learn_code = 3
learn_columns = ["trial_n", "rho","condition", "task","ITI","ISI","block","ouA","ouB","ouC"]
learn_trial_dimension = 10



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
def preserve_uncertainty(arr):
    arr = np.take(arr,np.random.permutation(arr.shape[0]),axis=0,out=arr);
    while 'try_again':
        if (any(i==j==k==l for i,j,k,l in zip(arr, arr[1:], arr[2:], arr[3:]))):
            arr = np.take(arr,np.random.permutation(arr.shape[0]),axis=0,out=arr);
            print('try_again')
        else:
            print('yey')
            break



# LEARNING: Sample = demo_C1_1_ID1
trial_n =  list(range(1, learn_trials_p_block+1))
condition = np.ones(learn_trials_p_block)
ratio = int(learn_trials_p_block/2)
quarter = int(learn_trials_p_block/4)
condition[:ratio] = 0


# for OU we need to somehow shuffle here to assign OU level to condition?
ou1 = np.zeros(learn_trials_p_block)
ou1[:quarter] = 1
ou2 = np.ones(learn_trials_p_block)
ou2[:ratio] = 0
ou3 = np.ones(learn_trials_p_block)
ou3[:quarter] = 0


for ID in range(1,ID_total):
    for j in range(1,(learn_blocks +1)):
        globals()['Learn_C1_%s' % j] = np.full([learn_trials_p_block,learn_trial_dimension], None) 
        preserve_uncertainty(ou1)
        preserve_uncertainty(ou2)
        preserve_uncertainty(ou3)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, learn_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, learn_trials_p_block))

        for i in range(learn_trials_p_block):
            globals()['Learn_C1_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Learn_C1_%s' % j][[i],[1]] = 100 #rho
            globals()['Learn_C1_%s' % j][[i],[2]] = 0
            globals()['Learn_C1_%s' % j][[i],[3]] = 3 #task
            globals()['Learn_C1_%s' % j][[i],[4]] = ITI[(i)]
            globals()['Learn_C1_%s' % j][[i],[5]] = SOI[(i)]
            globals()['Learn_C1_%s' % j][[i],[6]] = j #block
            globals()['Learn_C1_%s' % j][[i],[7]] = ou1[(i)]
            globals()['Learn_C1_%s' % j][[i],[8]] = ou2[(i)]
            globals()['Learn_C1_%s' % j][[i],[9]] = ou3[(i)]



# some shuffling to make sure local uncertainty is constant

#save copy to then save to csv

        globals()['SLearn_C1_%s' % j] = np.copy(globals()['Learn_C1_%s' % j]) 



#make it pretty and compatible with jsPsych input format needed
        globals()['Learn_C1_%s' % j] = str(globals()['Learn_C1_%s' % j]).replace('.0 ', ',')
        globals()['Learn_C1_%s' % j] = str(globals()['Learn_C1_%s' % j]).replace(',]',']')
        globals()['Learn_C1_%s' % j] = str(globals()['Learn_C1_%s' % j]).replace('\n',',')
        globals()['Learn_C1_%s' % j] = str(globals()['Learn_C1_%s' % j]).replace('],]',']]')
        globals()['Learn_C1_%s' % j] = str(globals()['Learn_C1_%s' % j]).replace(', ',',')
        globals()['Learn_C1_%s' % j] = str(globals()['Learn_C1_%s' % j]).replace(']]',']],')
        globals()['Learn_C1_%s' % j] = str(globals()['Learn_C1_%s' % j]).replace(' ',',')
        globals()['Learn_C1_%s' % j] = str(globals()['Learn_C1_%s' % j]).replace('.0]', ']')


        for x in range(learn_trials_p_block):
            globals()['Learn_C1_%s' % j] = str(globals()['Learn_C1_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')


    for j in range(1,(learn_blocks +1)):
        globals()['Learn_C2_%s' % j] = np.full([learn_trials_p_block,learn_trial_dimension], None) 
        preserve_uncertainty(ou1)
        preserve_uncertainty(ou2)
        preserve_uncertainty(ou3)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, learn_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, learn_trials_p_block))

        for i in range(learn_trials_p_block):
            globals()['Learn_C2_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Learn_C2_%s' % j][[i],[1]] = 100 #rho
            globals()['Learn_C2_%s' % j][[i],[2]] = 1
            globals()['Learn_C2_%s' % j][[i],[3]] = 3 #task
            globals()['Learn_C2_%s' % j][[i],[4]] = ITI[(i)]
            globals()['Learn_C2_%s' % j][[i],[5]] = SOI[(i)]
            globals()['Learn_C2_%s' % j][[i],[6]] = j #block
            globals()['Learn_C2_%s' % j][[i],[7]] = ou1[(i)]
            globals()['Learn_C2_%s' % j][[i],[8]] = ou2[(i)]
            globals()['Learn_C2_%s' % j][[i],[9]] = ou3[(i)]


#save copy to then save to csv

        globals()['SLearn_C2_%s' % j] = np.copy(globals()['Learn_C2_%s' % j]) 



#make it pretty and compatible with jsPsych input format needed
        globals()['Learn_C2_%s' % j] = str(globals()['Learn_C2_%s' % j]).replace('.0 ', ',')
        globals()['Learn_C2_%s' % j] = str(globals()['Learn_C2_%s' % j]).replace(',]',']')
        globals()['Learn_C2_%s' % j] = str(globals()['Learn_C2_%s' % j]).replace('\n',',')
        globals()['Learn_C2_%s' % j] = str(globals()['Learn_C2_%s' % j]).replace('],]',']]')
        globals()['Learn_C2_%s' % j] = str(globals()['Learn_C2_%s' % j]).replace(', ',',')
        globals()['Learn_C2_%s' % j] = str(globals()['Learn_C2_%s' % j]).replace(']]',']],')
        globals()['Learn_C2_%s' % j] = str(globals()['Learn_C2_%s' % j]).replace(' ',',')
        globals()['Learn_C2_%s' % j] = str(globals()['Learn_C2_%s' % j]).replace('.0]', ']')


        for x in range(learn_trials_p_block):
            globals()['Learn_C2_%s' % j] = str(globals()['Learn_C2_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')


    for j in range(1,(learn_blocks +1)):
        globals()['Learn_C3_%s' % j] = np.full([learn_trials_p_block,learn_trial_dimension], None) 
        preserve_uncertainty(ou1)
        preserve_uncertainty(ou2)
        preserve_uncertainty(ou3)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, learn_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, learn_trials_p_block))

        for i in range(learn_trials_p_block):
            globals()['Learn_C3_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Learn_C3_%s' % j][[i],[1]] = 100 #rho
            globals()['Learn_C3_%s' % j][[i],[2]] = 2
            globals()['Learn_C3_%s' % j][[i],[3]] = 3 #task
            globals()['Learn_C3_%s' % j][[i],[4]] = ITI[(i)]
            globals()['Learn_C3_%s' % j][[i],[5]] = SOI[(i)]
            globals()['Learn_C3_%s' % j][[i],[6]] = j #block
            globals()['Learn_C3_%s' % j][[i],[7]] = ou1[(i)]
            globals()['Learn_C3_%s' % j][[i],[8]] = ou2[(i)]
            globals()['Learn_C3_%s' % j][[i],[9]] = ou3[(i)]


#save copy to then save to csv

        globals()['SLearn_C3_%s' % j] = np.copy(globals()['Learn_C3_%s' % j]) 



#make it pretty and compatible with jsPsych input format needed
        globals()['Learn_C3_%s' % j] = str(globals()['Learn_C3_%s' % j]).replace('.0 ', ',')
        globals()['Learn_C3_%s' % j] = str(globals()['Learn_C3_%s' % j]).replace(',]',']')
        globals()['Learn_C3_%s' % j] = str(globals()['Learn_C3_%s' % j]).replace('\n',',')
        globals()['Learn_C3_%s' % j] = str(globals()['Learn_C3_%s' % j]).replace('],]',']]')
        globals()['Learn_C3_%s' % j] = str(globals()['Learn_C3_%s' % j]).replace(', ',',')
        globals()['Learn_C3_%s' % j] = str(globals()['Learn_C3_%s' % j]).replace(']]',']],')
        globals()['Learn_C3_%s' % j] = str(globals()['Learn_C3_%s' % j]).replace(' ',',')
        globals()['Learn_C3_%s' % j] = str(globals()['Learn_C3_%s' % j]).replace('.0]', ']')


        for x in range(learn_trials_p_block):
            globals()['Learn_C3_%s' % j] = str(globals()['Learn_C3_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')

    for j in range(1,(learn_blocks +1)):
        globals()['Learn_C4_%s' % j] = np.full([learn_trials_p_block,learn_trial_dimension], None) 
        preserve_uncertainty(ou1)
        preserve_uncertainty(ou2)
        preserve_uncertainty(ou3)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, learn_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, learn_trials_p_block))

        for i in range(learn_trials_p_block):
            globals()['Learn_C4_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Learn_C4_%s' % j][[i],[1]] = 100 #rho
            globals()['Learn_C4_%s' % j][[i],[2]] = 3
            globals()['Learn_C4_%s' % j][[i],[3]] = 3 #task
            globals()['Learn_C4_%s' % j][[i],[4]] = ITI[(i)]
            globals()['Learn_C4_%s' % j][[i],[5]] = SOI[(i)]
            globals()['Learn_C4_%s' % j][[i],[6]] = j #block
            globals()['Learn_C4_%s' % j][[i],[7]] = ou1[(i)]
            globals()['Learn_C4_%s' % j][[i],[8]] = ou2[(i)]
            globals()['Learn_C4_%s' % j][[i],[9]] = ou3[(i)]


#save copy to then save to csv

        globals()['SLearn_C4_%s' % j] = np.copy(globals()['Learn_C4_%s' % j]) 



#make it pretty and compatible with jsPsych input format needed
        globals()['Learn_C4_%s' % j] = str(globals()['Learn_C4_%s' % j]).replace('.0 ', ',')
        globals()['Learn_C4_%s' % j] = str(globals()['Learn_C4_%s' % j]).replace(',]',']')
        globals()['Learn_C4_%s' % j] = str(globals()['Learn_C4_%s' % j]).replace('\n',',')
        globals()['Learn_C4_%s' % j] = str(globals()['Learn_C4_%s' % j]).replace('],]',']]')
        globals()['Learn_C4_%s' % j] = str(globals()['Learn_C4_%s' % j]).replace(', ',',')
        globals()['Learn_C4_%s' % j] = str(globals()['Learn_C4_%s' % j]).replace(']]',']],')
        globals()['Learn_C4_%s' % j] = str(globals()['Learn_C4_%s' % j]).replace(' ',',')
        globals()['Learn_C4_%s' % j] = str(globals()['Learn_C4_%s' % j]).replace('.0]', ']')


        for x in range(learn_trials_p_block):
            globals()['Learn_C4_%s' % j] = str(globals()['Learn_C4_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')


    for j in range(1,(learn_blocks +1)):
        globals()['Learn_C5_%s' % j] = np.full([learn_trials_p_block,learn_trial_dimension], None) 
        preserve_uncertainty(ou1)
        preserve_uncertainty(ou2)
        preserve_uncertainty(ou3)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, learn_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, learn_trials_p_block))

        for i in range(learn_trials_p_block):
            globals()['Learn_C5_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Learn_C5_%s' % j][[i],[1]] = 100 #rho
            globals()['Learn_C5_%s' % j][[i],[2]] = 4
            globals()['Learn_C5_%s' % j][[i],[3]] = 3 #task
            globals()['Learn_C5_%s' % j][[i],[4]] = ITI[(i)]
            globals()['Learn_C5_%s' % j][[i],[5]] = SOI[(i)]
            globals()['Learn_C5_%s' % j][[i],[6]] = j #block
            globals()['Learn_C5_%s' % j][[i],[7]] = ou1[(i)]
            globals()['Learn_C5_%s' % j][[i],[8]] = ou2[(i)]
            globals()['Learn_C5_%s' % j][[i],[9]] = ou3[(i)]


#save copy to then save to csv

        globals()['SLearn_C5_%s' % j] = np.copy(globals()['Learn_C5_%s' % j]) 



#make it pretty and compatible with jsPsych input format needed
        globals()['Learn_C5_%s' % j] = str(globals()['Learn_C5_%s' % j]).replace('.0 ', ',')
        globals()['Learn_C5_%s' % j] = str(globals()['Learn_C5_%s' % j]).replace(',]',']')
        globals()['Learn_C5_%s' % j] = str(globals()['Learn_C5_%s' % j]).replace('\n',',')
        globals()['Learn_C5_%s' % j] = str(globals()['Learn_C5_%s' % j]).replace('],]',']]')
        globals()['Learn_C5_%s' % j] = str(globals()['Learn_C5_%s' % j]).replace(', ',',')
        globals()['Learn_C5_%s' % j] = str(globals()['Learn_C5_%s' % j]).replace(']]',']],')
        globals()['Learn_C5_%s' % j] = str(globals()['Learn_C5_%s' % j]).replace(' ',',')
        globals()['Learn_C5_%s' % j] = str(globals()['Learn_C5_%s' % j]).replace('.0]', ']')


        for x in range(learn_trials_p_block):
            globals()['Learn_C5_%s' % j] = str(globals()['Learn_C5_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')


    for j in range(1,(learn_blocks +1)):
        globals()['Learn_C6_%s' % j] = np.full([learn_trials_p_block,learn_trial_dimension], None) 
        preserve_uncertainty(ou1)
        preserve_uncertainty(ou2)
        preserve_uncertainty(ou3)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, learn_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, learn_trials_p_block))

        for i in range(learn_trials_p_block):
            globals()['Learn_C6_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Learn_C6_%s' % j][[i],[1]] = 100 #rho
            globals()['Learn_C6_%s' % j][[i],[2]] = 5
            globals()['Learn_C6_%s' % j][[i],[3]] = 3 #task
            globals()['Learn_C6_%s' % j][[i],[4]] = ITI[(i)]
            globals()['Learn_C6_%s' % j][[i],[5]] = SOI[(i)]
            globals()['Learn_C6_%s' % j][[i],[6]] = j #block
            globals()['Learn_C6_%s' % j][[i],[7]] = ou1[(i)]
            globals()['Learn_C6_%s' % j][[i],[8]] = ou2[(i)]
            globals()['Learn_C6_%s' % j][[i],[9]] = ou3[(i)]


#save copy to then save to csv

        globals()['SLearn_C6_%s' % j] = np.copy(globals()['Learn_C6_%s' % j]) 



#make it pretty and compatible with jsPsych input format needed
        globals()['Learn_C6_%s' % j] = str(globals()['Learn_C6_%s' % j]).replace('.0 ', ',')
        globals()['Learn_C6_%s' % j] = str(globals()['Learn_C6_%s' % j]).replace(',]',']')
        globals()['Learn_C6_%s' % j] = str(globals()['Learn_C6_%s' % j]).replace('\n',',')
        globals()['Learn_C6_%s' % j] = str(globals()['Learn_C6_%s' % j]).replace('],]',']]')
        globals()['Learn_C6_%s' % j] = str(globals()['Learn_C6_%s' % j]).replace(', ',',')
        globals()['Learn_C6_%s' % j] = str(globals()['Learn_C6_%s' % j]).replace(']]',']],')
        globals()['Learn_C6_%s' % j] = str(globals()['Learn_C6_%s' % j]).replace(' ',',')
        globals()['Learn_C6_%s' % j] = str(globals()['Learn_C6_%s' % j]).replace('.0]', ']')


        for x in range(learn_trials_p_block):
            globals()['Learn_C6_%s' % j] = str(globals()['Learn_C6_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')

    

   
# add trials that stay the same across participants
    if (ID == 1):
        f.write("var vars = { ")

# write to .js file, block for block
    for j in range(1,(learn_blocks+1)):
        f.write("\n")
        f.write("'Learn_C1_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Learn_C1_%s' % j])) #write to file
        f.write("'Learn_C2_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Learn_C2_%s' % j])) #write to file
        f.write("'Learn_C3_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Learn_C3_%s' % j])) #write to file
        f.write("'Learn_C4_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Learn_C4_%s' % j])) #write to file
        f.write("'Learn_C5_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Learn_C5_%s' % j])) #write to file
        f.write("'Learn_C6_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Learn_C6_%s' % j])) #write to file


# write to csv
    
    slearn = np.concatenate((SLearn_C1_1, SLearn_C2_1))
    slearn= np.concatenate((slearn, SLearn_C3_1))
    slearn= np.concatenate((slearn, SLearn_C4_1))
    slearn= np.concatenate((slearn, SLearn_C5_1))
    slearn= np.concatenate((slearn, SLearn_C6_1))
    for j in range(2,learn_blocks+1):
        slearn = np.append(slearn, globals()['SLearn_C1_%s' % j])
        slearn = np.append(slearn, globals()['SLearn_C2_%s' % j])
        slearn = np.append(slearn, globals()['SLearn_C3_%s' % j])
        slearn = np.append(slearn, globals()['SLearn_C4_%s' % j])
        slearn = np.append(slearn, globals()['SLearn_C5_%s' % j])
        slearn = np.append(slearn, globals()['SLearn_C6_%s' % j])

    slearn = slearn.reshape(((learn_blocks*learn_trials_p_block)*6), learn_trial_dimension)
    slearn_df = pd.DataFrame(slearn, columns=[learn_columns])
    slearn_df = slearn_df.astype(str)
    slearn_df= slearn_df.replace(to_replace = "\.0+$",value = "", regex = True)
    slearn_df.to_csv("ID_"+str(ID)+"/Learn_ID" + str(ID)+".csv", index=False)

