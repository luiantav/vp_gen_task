import random
import numpy as np
from numpy import random
import seaborn as sns
import os
import pandas as pd
import numpy.matlib


output_file = "sequences"
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

# parameters for demo
demo_blocks = 2
demo_trials_p_block = 6
demo_code = 1
demo_columns = ["trial_n", "rho", "choice","condition", "task","ITI","ISI","block","first"]
demo_trial_dimension = 9

#parameters for kaern (quest)
kaern_blocks = 2 #3 titration blocks and one fixed
kaern_trials_p_block = 20
kaern_code = 2
kaern_columns = ["trial_n", "rho", "choice","condition", "task","ITI","ISI","block","first"]
kaern_trial_dimension = 9

rho_lower = 25
rho_upper = 175

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
        vals = np.random.choice(vals, n, replace=True)
        upper = len(vals[vals>upper_limit]) #check if it's the case
        i = i+1
    vals = vals*1000
    return vals



# shuffle function to prevent that more then 2 consecutive choices are the same
def shuffle(arr):
    arr = np.take(arr,np.random.permutation(arr.shape[0]),axis=0,out=arr);
    while 'try_again':
        if (any(i==j==k for i,j,k in zip(arr, arr[1:], arr[2:]))):
            arr = np.take(arr,np.random.permutation(arr.shape[0]),axis=0,out=arr);
            print('try_again')
        else:
            print('yey')
            break




# DEMO: Sample = demo_C1_1_ID1
trial_n =  list(range(1, demo_trials_p_block+1))
choice = np.ones(demo_trials_p_block)
task = [demo_code] * demo_trials_p_block
condition = ()
ratio = int(demo_trials_p_block/2)
choice[:ratio] = 0
first = np.zeros(demo_trials_p_block)

for ID in range(1,ID_total):
    for j in range(1,(demo_blocks +1)):
        globals()['Demo_C1_%s' % j] = np.full([demo_trials_p_block,demo_trial_dimension], None) 
        rho = np.random.randint(rho_lower,rho_upper, size= demo_trials_p_block) #check how to improve sampling 
        shuffle(choice)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, demo_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, demo_trials_p_block))

        for i in range(demo_trials_p_block):
            globals()['Demo_C1_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Demo_C1_%s' % j][[i],[1]] = rho[(i)] 
            globals()['Demo_C1_%s' % j][[i],[2]] = choice[(i)]
            globals()['Demo_C1_%s' % j][[i],[3]] = 0
            globals()['Demo_C1_%s' % j][[i],[4]] = task[(i)]
            globals()['Demo_C1_%s' % j][[i],[5]] = ITI[(i)]
            globals()['Demo_C1_%s' % j][[i],[6]] = SOI[(i)]
            globals()['Demo_C1_%s' % j][[i],[7]] = j
            globals()['Demo_C1_%s' % j][[i],[8]] = first[(i)]


#save copy to then save to csv

        globals()['SDemo_C1_%s' % j] = np.copy(globals()['Demo_C1_%s' % j]) 



#make it pretty and compatible with jsPsych input format needed
        globals()['Demo_C1_%s' % j] = str(globals()['Demo_C1_%s' % j]).replace('.0 ', ',')
        globals()['Demo_C1_%s' % j] = str(globals()['Demo_C1_%s' % j]).replace(',]',']')
        globals()['Demo_C1_%s' % j] = str(globals()['Demo_C1_%s' % j]).replace('\n',',')
        globals()['Demo_C1_%s' % j] = str(globals()['Demo_C1_%s' % j]).replace('],]',']]')
        globals()['Demo_C1_%s' % j] = str(globals()['Demo_C1_%s' % j]).replace(', ',',')
        globals()['Demo_C1_%s' % j] = str(globals()['Demo_C1_%s' % j]).replace(']]',']],')
        globals()['Demo_C1_%s' % j] = str(globals()['Demo_C1_%s' % j]).replace(' ',',')
        globals()['Demo_C1_%s' % j] = str(globals()['Demo_C1_%s' % j]).replace('.0]', ']')


        for x in range(demo_trials_p_block):
            globals()['Demo_C1_%s' % j] = str(globals()['Demo_C1_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')


    for j in range(1,demo_blocks +1):
        globals()['Demo_C2_%s' % j] = np.full([demo_trials_p_block,demo_trial_dimension], None) 
        rho = np.random.randint(rho_lower,rho_upper, size= demo_trials_p_block) #check how to improve sampling 
        shuffle(choice)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, demo_trials_p_block))
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, demo_trials_p_block))

        for i in range(demo_trials_p_block):
            globals()['Demo_C2_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Demo_C2_%s' % j][[i],[1]] = rho[(i)] 
            globals()['Demo_C2_%s' % j][[i],[2]] = choice[(i)]
            globals()['Demo_C2_%s' % j][[i],[3]] = 1
            globals()['Demo_C2_%s' % j][[i],[4]] = task[(i)]
            globals()['Demo_C2_%s' % j][[i],[5]] = ITI[(i)]
            globals()['Demo_C2_%s' % j][[i],[6]] = SOI[(i)]
            globals()['Demo_C2_%s' % j][[i],[7]] = j
            globals()['Demo_C2_%s' % j][[i],[8]] = first[(i)]
            

#save copy to then save to csv

        globals()['SDemo_C2_%s' % j] = np.copy(globals()['Demo_C2_%s' % j])


#make it pretty and compatible with jsPsych input format needed

        globals()['Demo_C2_%s' % j] = str(globals()['Demo_C2_%s' % j]).replace('.0 ', ',')
        globals()['Demo_C2_%s' % j] = str(globals()['Demo_C2_%s' % j]).replace(',]',']')
        globals()['Demo_C2_%s' % j] = str(globals()['Demo_C2_%s' % j]).replace('\n',',')
        globals()['Demo_C2_%s' % j] = str(globals()['Demo_C2_%s' % j]).replace('],]',']]')
        globals()['Demo_C2_%s' % j] = str(globals()['Demo_C2_%s' % j]).replace(', ',',')
        globals()['Demo_C2_%s' % j] = str(globals()['Demo_C2_%s' % j]).replace(']]',']],')
        globals()['Demo_C2_%s' % j] = str(globals()['Demo_C2_%s' % j]).replace(' ',',')
        globals()['Demo_C2_%s' % j] = str(globals()['Demo_C2_%s' % j]).replace('.0]', ']')

        for x in range(demo_trials_p_block):
            globals()['Demo_C2_%s' % j] = str(globals()['Demo_C2_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')




# TITRATION - Quest

    trial_n =  list(range(1, kaern_trials_p_block+1))
    choice = np.ones(kaern_trials_p_block)
    task = [kaern_code] * kaern_trials_p_block
    condition = ()
    ratio = int(kaern_trials_p_block/2)
    choice[:ratio] = 0
    first = np.zeros(kaern_trials_p_block)



    # Condition 1
    for j in range(1,(kaern_blocks +1)):
        globals()['Kaern_C1_%s' % j] = np.full([kaern_trials_p_block,kaern_trial_dimension], None) 
        rho = np.random.randint(rho_lower,rho_upper, size= kaern_trials_p_block) #check how to improve sampling 
        shuffle(choice)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, kaern_trials_p_block)) 
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, kaern_trials_p_block))

        for i in range(kaern_trials_p_block):
            globals()['Kaern_C1_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Kaern_C1_%s' % j][[i],[1]] = rho[(i)] 
            globals()['Kaern_C1_%s' % j][[i],[2]] = choice[(i)]
            globals()['Kaern_C1_%s' % j][[i],[3]] = 0
            globals()['Kaern_C1_%s' % j][[i],[4]] = task[(i)]
            globals()['Kaern_C1_%s' % j][[i],[5]] = ITI[(i)]
            globals()['Kaern_C1_%s' % j][[i],[6]] = SOI[(i)]
            globals()['Kaern_C1_%s' % j][[i],[7]] = j
            globals()['Kaern_C1_%s' % j][[i],[8]] = first[(i)]

        if (j == 1):
            find_first_different = np.where((globals()['Kaern_C1_%s' % j][:,2]) == 1)[0][0] #find first different and mark with 2
            globals()['Kaern_C1_%s' % j][[find_first_different],[8]] = 2

        globals()['SKaern_C1_%s' % j] = np.copy(globals()['Kaern_C1_%s' % j]) #save copy to then save to csv

        #make it pretty and compatible with jsPsych input format needed
        globals()['Kaern_C1_%s' % j] = str(globals()['Kaern_C1_%s' % j]).replace('.0 ', ',')
        globals()['Kaern_C1_%s' % j] = str(globals()['Kaern_C1_%s' % j]).replace(',]',']')
        globals()['Kaern_C1_%s' % j] = str(globals()['Kaern_C1_%s' % j]).replace('\n',',')
        globals()['Kaern_C1_%s' % j] = str(globals()['Kaern_C1_%s' % j]).replace('],]',']]')
        globals()['Kaern_C1_%s' % j] = str(globals()['Kaern_C1_%s' % j]).replace(', ',',')
        globals()['Kaern_C1_%s' % j] = str(globals()['Kaern_C1_%s' % j]).replace(']]',']],')
        globals()['Kaern_C1_%s' % j] = str(globals()['Kaern_C1_%s' % j]).replace(' ',',')
        globals()['Kaern_C1_%s' % j] = str(globals()['Kaern_C1_%s' % j]).replace('.0]', ']')

        for x in range(kaern_trials_p_block):
            globals()['Kaern_C1_%s' % j] = str(globals()['Kaern_C1_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')


    for j in range(1,kaern_blocks+1):
        globals()['Kaern_C2_%s' % j] = np.full([kaern_trials_p_block,kaern_trial_dimension], None) 
        rho = np.random.randint(rho_lower,rho_upper, size= kaern_trials_p_block) #check how to improve sampling 
        shuffle(choice)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, kaern_trials_p_block))
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, kaern_trials_p_block))
       
        for i in range(kaern_trials_p_block):
            globals()['Kaern_C2_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Kaern_C2_%s' % j][[i],[1]] = rho[(i)] 
            globals()['Kaern_C2_%s' % j][[i],[2]] = choice[(i)]
            globals()['Kaern_C2_%s' % j][[i],[3]] = 1
            globals()['Kaern_C2_%s' % j][[i],[4]] = task[(i)]
            globals()['Kaern_C2_%s' % j][[i],[5]] = ITI[(i)]
            globals()['Kaern_C2_%s' % j][[i],[6]] = SOI[(i)]
            globals()['Kaern_C2_%s' % j][[i],[7]] = j
            globals()['Kaern_C2_%s' % j][[i],[8]] = first[(i)]

        if (j == 1):
            find_first_different = np.where((globals()['Kaern_C2_%s' % j][:,2]) == 1)[0][0] #find first different and mark with 2
            globals()['Kaern_C2_%s' % j][[find_first_different],[8]] = 2

        globals()['SKaern_C2_%s' % j] = np.copy(globals()['Kaern_C2_%s' % j]) #save copy to then save to csv

        #make it pretty and compatible with jsPsych input format needed
        globals()['Kaern_C2_%s' % j] = str(globals()['Kaern_C2_%s' % j]).replace('.0 ', ',')
        globals()['Kaern_C2_%s' % j] = str(globals()['Kaern_C2_%s' % j]).replace(',]',']')
        globals()['Kaern_C2_%s' % j] = str(globals()['Kaern_C2_%s' % j]).replace('\n',',')
        globals()['Kaern_C2_%s' % j] = str(globals()['Kaern_C2_%s' % j]).replace('],]',']]')
        globals()['Kaern_C2_%s' % j] = str(globals()['Kaern_C2_%s' % j]).replace(', ',',')
        globals()['Kaern_C2_%s' % j] = str(globals()['Kaern_C2_%s' % j]).replace(']]',']],')
        globals()['Kaern_C2_%s' % j] = str(globals()['Kaern_C2_%s' % j]).replace(' ',',')
        globals()['Kaern_C2_%s' % j] = str(globals()['Kaern_C2_%s' % j]).replace('.0]', ']')
        

        for x in range(kaern_trials_p_block):
            globals()['Kaern_C2_%s' % j] = str(globals()['Kaern_C2_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')


    for j in range(1,kaern_blocks+1):
        globals()['Kaern_C3_%s' % j] = np.full([kaern_trials_p_block,kaern_trial_dimension], None) 
        rho = np.random.randint(rho_lower,rho_upper, size= kaern_trials_p_block) #check how to improve sampling 
        shuffle(choice)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, kaern_trials_p_block))
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, kaern_trials_p_block))


        for i in range(kaern_trials_p_block):
            globals()['Kaern_C3_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Kaern_C3_%s' % j][[i],[1]] = rho[(i)] 
            globals()['Kaern_C3_%s' % j][[i],[2]] = choice[(i)]
            globals()['Kaern_C3_%s' % j][[i],[3]] = 2
            globals()['Kaern_C3_%s' % j][[i],[4]] = task[(i)]
            globals()['Kaern_C3_%s' % j][[i],[5]] = ITI[(i)]
            globals()['Kaern_C3_%s' % j][[i],[6]] = SOI[(i)]
            globals()['Kaern_C3_%s' % j][[i],[7]] = j
            globals()['Kaern_C3_%s' % j][[i],[8]] = first[(i)]

        if (j == 1):
            find_first_different = np.where((globals()['Kaern_C3_%s' % j][:,2]) == 1)[0][0] #find first different and mark with 2
            globals()['Kaern_C3_%s' % j][[find_first_different],[8]] = 2

        globals()['SKaern_C3_%s' % j] = np.copy(globals()['Kaern_C3_%s' % j]) #save copy to then save to csv

        #make it pretty and compatible with jsPsych input format needed
        globals()['Kaern_C3_%s' % j] = str(globals()['Kaern_C3_%s' % j]).replace('.0 ', ',')
        globals()['Kaern_C3_%s' % j] = str(globals()['Kaern_C3_%s' % j]).replace(',]',']')
        globals()['Kaern_C3_%s' % j] = str(globals()['Kaern_C3_%s' % j]).replace('\n',',')
        globals()['Kaern_C3_%s' % j] = str(globals()['Kaern_C3_%s' % j]).replace('],]',']]')
        globals()['Kaern_C3_%s' % j] = str(globals()['Kaern_C3_%s' % j]).replace(', ',',')
        globals()['Kaern_C3_%s' % j] = str(globals()['Kaern_C3_%s' % j]).replace(']]',']],')
        globals()['Kaern_C3_%s' % j] = str(globals()['Kaern_C3_%s' % j]).replace(' ',',')
        globals()['Kaern_C3_%s' % j] = str(globals()['Kaern_C3_%s' % j]).replace('.0]', ']')

        for x in range(kaern_trials_p_block):
            globals()['Kaern_C3_%s' % j] = str(globals()['Kaern_C3_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')


    for j in range(1,kaern_blocks+1):
        globals()['Kaern_C4_%s' % j] = np.full([kaern_trials_p_block,kaern_trial_dimension], None) 
        rho = np.random.randint(rho_lower,rho_upper, size= kaern_trials_p_block) #check how to improve sampling 
        shuffle(choice)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, kaern_trials_p_block))
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, kaern_trials_p_block))

        for i in range(kaern_trials_p_block):
            globals()['Kaern_C4_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Kaern_C4_%s' % j][[i],[1]] = rho[(i)] 
            globals()['Kaern_C4_%s' % j][[i],[2]] = choice[(i)]
            globals()['Kaern_C4_%s' % j][[i],[3]] = 3
            globals()['Kaern_C4_%s' % j][[i],[4]] = task[(i)]
            globals()['Kaern_C4_%s' % j][[i],[5]] = ITI[(i)]
            globals()['Kaern_C4_%s' % j][[i],[6]] = SOI[(i)]
            globals()['Kaern_C4_%s' % j][[i],[7]] = j
            globals()['Kaern_C4_%s' % j][[i],[8]] = first[(i)]

        if (j == 1):
            find_first_different = np.where((globals()['Kaern_C4_%s' % j][:,2]) == 1)[0][0] #find first different and mark with 2
            globals()['Kaern_C4_%s' % j][[find_first_different],[8]] = 2

        globals()['SKaern_C4_%s' % j] = np.copy(globals()['Kaern_C4_%s' % j]) #save copy to then save to csv

        #make it pretty and compatible with jsPsych input format needed
        globals()['Kaern_C4_%s' % j] = str(globals()['Kaern_C4_%s' % j]).replace('.0 ', ',')
        globals()['Kaern_C4_%s' % j] = str(globals()['Kaern_C4_%s' % j]).replace(',]',']')
        globals()['Kaern_C4_%s' % j] = str(globals()['Kaern_C4_%s' % j]).replace('\n',',')
        globals()['Kaern_C4_%s' % j] = str(globals()['Kaern_C4_%s' % j]).replace('],]',']]')
        globals()['Kaern_C4_%s' % j] = str(globals()['Kaern_C4_%s' % j]).replace(', ',',')
        globals()['Kaern_C4_%s' % j] = str(globals()['Kaern_C4_%s' % j]).replace(']]',']],')
        globals()['Kaern_C4_%s' % j] = str(globals()['Kaern_C4_%s' % j]).replace(' ',',')
        globals()['Kaern_C4_%s' % j] = str(globals()['Kaern_C4_%s' % j]).replace('.0]', ']')

        for x in range(kaern_trials_p_block):
            globals()['Kaern_C4_%s' % j] = str(globals()['Kaern_C4_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')


    for j in range(1,kaern_blocks+1):
        globals()['Kaern_C5_%s' % j] = np.full([kaern_trials_p_block,kaern_trial_dimension], None) 
        rho = np.random.randint(rho_lower,rho_upper, size= kaern_trials_p_block) #check how to improve sampling 
        shuffle(choice)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, kaern_trials_p_block))
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, kaern_trials_p_block))

        for i in range(kaern_trials_p_block):
            globals()['Kaern_C5_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Kaern_C5_%s' % j][[i],[1]] = rho[(i)] 
            globals()['Kaern_C5_%s' % j][[i],[2]] = choice[(i)]
            globals()['Kaern_C5_%s' % j][[i],[3]] = 4
            globals()['Kaern_C5_%s' % j][[i],[4]] = task[(i)]
            globals()['Kaern_C5_%s' % j][[i],[5]] = ITI[(i)]
            globals()['Kaern_C5_%s' % j][[i],[6]] = SOI[(i)]
            globals()['Kaern_C5_%s' % j][[i],[7]] = j
            globals()['Kaern_C5_%s' % j][[i],[8]] = first[(i)]

        if (j == 1):
            find_first_different = np.where((globals()['Kaern_C5_%s' % j][:,2]) == 1)[0][0] #find first different and mark with 2
            globals()['Kaern_C5_%s' % j][[find_first_different],[8]] = 2

        globals()['SKaern_C5_%s' % j] = np.copy(globals()['Kaern_C5_%s' % j]) #save copy to then save to csv

        #make it pretty and compatible with jsPsych input format needed
        globals()['Kaern_C5_%s' % j] = str(globals()['Kaern_C5_%s' % j]).replace('.0 ', ',')
        globals()['Kaern_C5_%s' % j] = str(globals()['Kaern_C5_%s' % j]).replace(',]',']')
        globals()['Kaern_C5_%s' % j] = str(globals()['Kaern_C5_%s' % j]).replace('\n',',')
        globals()['Kaern_C5_%s' % j] = str(globals()['Kaern_C5_%s' % j]).replace('],]',']]')
        globals()['Kaern_C5_%s' % j] = str(globals()['Kaern_C5_%s' % j]).replace(', ',',')
        globals()['Kaern_C5_%s' % j] = str(globals()['Kaern_C5_%s' % j]).replace(']]',']],')
        globals()['Kaern_C5_%s' % j] = str(globals()['Kaern_C5_%s' % j]).replace(' ',',')
        globals()['Kaern_C5_%s' % j] = str(globals()['Kaern_C5_%s' % j]).replace('.0]', ']')

        for x in range(kaern_trials_p_block):
            globals()['Kaern_C5_%s' % j] = str(globals()['Kaern_C5_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')

    for j in range(1,kaern_blocks+1):
        globals()['Kaern_C6_%s' % j] = np.full([kaern_trials_p_block,kaern_trial_dimension], None) 
        rho = np.random.randint(rho_lower,rho_upper, size= kaern_trials_p_block) #check how to improve sampling 
        shuffle(choice)
        ITI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, kaern_trials_p_block))
        SOI = np.rint(generate_trunc_exp_distrLAM(bounds, target_lam, kaern_trials_p_block))

        for i in range(kaern_trials_p_block):
            globals()['Kaern_C6_%s' % j][[i],[0]] = trial_n[(i)] 
            globals()['Kaern_C6_%s' % j][[i],[1]] = rho[(i)] 
            globals()['Kaern_C6_%s' % j][[i],[2]] = choice[(i)]
            globals()['Kaern_C6_%s' % j][[i],[3]] = 5
            globals()['Kaern_C6_%s' % j][[i],[4]] = task[(i)]
            globals()['Kaern_C6_%s' % j][[i],[5]] = ITI[(i)]
            globals()['Kaern_C6_%s' % j][[i],[6]] = SOI[(i)]
            globals()['Kaern_C6_%s' % j][[i],[7]] = j
            globals()['Kaern_C6_%s' % j][[i],[8]] = first[(i)]


        if (j == 1):
            find_first_different = np.where((globals()['Kaern_C6_%s' % j][:,2]) == 1)[0][0] #find first different and mark with 2
            globals()['Kaern_C6_%s' % j][[find_first_different],[8]] = 2

        globals()['SKaern_C6_%s' % j] = np.copy(globals()['Kaern_C6_%s' % j]) #save copy to then save to csv

        #make it pretty and compatible with jsPsych input format needed
        globals()['Kaern_C6_%s' % j] = str(globals()['Kaern_C6_%s' % j]).replace('.0 ', ',')
        globals()['Kaern_C6_%s' % j] = str(globals()['Kaern_C6_%s' % j]).replace(',]',']')
        globals()['Kaern_C6_%s' % j] = str(globals()['Kaern_C6_%s' % j]).replace('\n',',')
        globals()['Kaern_C6_%s' % j] = str(globals()['Kaern_C6_%s' % j]).replace('],]',']]')
        globals()['Kaern_C6_%s' % j] = str(globals()['Kaern_C6_%s' % j]).replace(', ',',')
        globals()['Kaern_C6_%s' % j] = str(globals()['Kaern_C6_%s' % j]).replace(']]',']],')
        globals()['Kaern_C6_%s' % j] = str(globals()['Kaern_C6_%s' % j]).replace(' ',',')
        globals()['Kaern_C6_%s' % j] = str(globals()['Kaern_C6_%s' % j]).replace('.0]', ']')

        for x in range(kaern_trials_p_block):
            globals()['Kaern_C6_%s' % j] = str(globals()['Kaern_C6_%s' % j]).replace('['+str(x)+' ', '['+str(x)+',')



# add trials that stay the same across participants
    if (ID == 1):
        f.write("var vars = { ")

# write to .js file, block for block
    for j in range(1,(demo_blocks+1)):
        f.write("\n")
        f.write("'Demo_C1_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Demo_C1_%s' % j])) #write to file
        f.write("'Demo_C2_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Demo_C2_%s' % j])) #write to file

    for j in range(1,(kaern_blocks+1)):
        f.write("\n")
        f.write("'Kaern_C1_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Kaern_C1_%s' % j])) #write to file
        f.write("'Kaern_C2_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Kaern_C2_%s' % j])) #write to file
        f.write("'Kaern_C3_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Kaern_C3_%s' % j])) #write to file
        f.write("'Kaern_C4_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Kaern_C4_%s' % j])) #write to file
        f.write("'Kaern_C5_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Kaern_C5_%s' % j])) #write to file
        f.write("'Kaern_C6_" + str(j)+"_ID"+str(ID)+"':")
        f.write("%s %s\n" %("", globals()['Kaern_C6_%s' % j])) #write to file


# write to csv
    
    sdemo = np.concatenate((SDemo_C1_1, SDemo_C2_1))
    for j in range(2,demo_blocks+1):
        sdemo = np.append(sdemo, globals()['SDemo_C1_%s' % j])
        sdemo = np.append(sdemo, globals()['SDemo_C2_%s' % j])

    sdemo = sdemo.reshape(((demo_blocks*demo_trials_p_block)*2), demo_trial_dimension)
    sdemo_df = pd.DataFrame(sdemo, columns=[demo_columns])
    sdemo_df = sdemo_df.astype(str)
    sdemo_df= sdemo_df.replace(to_replace = "\.0+$",value = "", regex = True)
    sdemo_df.to_csv("ID_"+str(ID)+"/Demo_ID" + str(ID)+".csv", index=False)


    skaern= np.concatenate((SKaern_C1_1, SKaern_C2_1))
    skaern= np.concatenate((skaern, SKaern_C3_1))
    skaern= np.concatenate((skaern, SKaern_C4_1))
    skaern= np.concatenate((skaern, SKaern_C5_1))
    skaern= np.concatenate((skaern, SKaern_C6_1))
    for j in range(2,kaern_blocks+1):
        skaern= np.append(skaern, globals()['SKaern_C1_%s' % j])
        skaern= np.append(skaern, globals()['SKaern_C2_%s' % j])
        skaern= np.append(skaern, globals()['SKaern_C3_%s' % j])
        skaern= np.append(skaern, globals()['SKaern_C4_%s' % j])
        skaern= np.append(skaern, globals()['SKaern_C5_%s' % j])
        skaern= np.append(skaern, globals()['SKaern_C6_%s' % j])

    skaern= skaern.reshape(((kaern_blocks*kaern_trials_p_block)*6), kaern_trial_dimension)
    skaern_df = pd.DataFrame(skaern, columns=[kaern_columns])
    skaern_df = skaern_df.astype(str)
    skaern_df= skaern_df.replace(to_replace = "\.0+$",value = "", regex = True)
    skaern_df.to_csv("ID_"+str(ID)+"/Kaern_ID" + str(ID)+".csv", index=False)


    #np.savetxt("ID_"+str(ID)+"/Demo_ID" + str(ID)+".csv", sdemo,fmt='%4d')


#f.write("\n")
#f.write("}")
#f.write("\n")
