import os
import pickle
pairs = []
real_world = os.listdir('VulDatasets/real_world_vulgen/vulgen_test_final/') # your dataset path

if os.path.exists('vulgen_test_final.pkl'):
    f = open('vulgen_test_final.pkl','rb')
    pairs = pickle.load(f)
    f.close()
    import pdb
    pdb.set_trace()
else:
    for file in real_world:
        if '.pkl' in file:
            f = open('VulDatasets/real_world_vulgen/vulgen_test_final/'+file, 'rb')
            parsed_data = pickle.load(f)
            for i,pair in enumerate(parsed_data):
                print(i)
                pairs.append(parsed_data[pair][0])
    f = open('vulgen_test_final.pkl','wb')
    pickle.dump(pairs,f)
    f.close()
