import os
import random
random.seed(1000)
files=os.listdir('./generated_formatted/')
random.shuffle(files)
iii=0
for i,f in enumerate(files):
    print(iii)
    if iii > 100:
        break
    if '_gen.c' in f:
        iii+=1
        print('\n\n\n\n\n',f)
        p=os.popen('diff ./generated_formatted/'+f[:-1].replace('_gen.c','_nonvul.c')+' ./generated_formatted/'+f)
        print(p.read())
        fx=open('./generated_formatted/'+f)
        gen=fx.read()
        fx.close()
        fx=open('./generated_formatted/'+f[:-1].replace('_gen.c','_vul.c'))
        vul=fx.read()
        fx.close()
        passx=False
        if gen==vul:
            print('pass')
            passx=True
        x=input()
        if x=='y' or passx:
            os.system('cp ./generated_formatted/'+f+' ./success/')
