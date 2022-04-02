import pickle
# Restore from a file
f = open('kitti_infos_trainval.pkl', 'rb')
data = pickle.load(f)
print(data)
