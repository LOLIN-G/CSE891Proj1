import scipy.io as scio

file = './sf_125k_7_125000.mat'
data = scio.loadmat(file)
print(data)