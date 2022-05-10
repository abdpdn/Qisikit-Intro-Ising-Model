import numpy as np
import matplotlib.pyplot as plt

exact = np.load('data/exact_ising.npy')
qasm = np.load('data/ising_qasm_simulator_N_4.npy')
ibmqc = np.load('data/ising_ibm_qc_N_4.npy')

lmbd = np.arange(.2, 1.75, 0.1)

plt.style.use('seaborn-talk')
plt.plot(lmbd, exact, 'k', lw=2, label='exact')
plt.scatter(lmbd, qasm, c='r', marker = 'o', label='qasm')
plt.scatter(lmbd, ibmqc, c='b', marker = '*', label='ibmqc')
plt.legend(fontsize=14)
plt.xlabel('$\lambda$', fontsize=20)
plt.ylabel('$\\langle \sigma_z\\rangle$',fontsize=20)
plt.title('$N=4$', fontsize=20)
plt.tight_layout()
plt.savefig('plots/Ising_mag_vs_lam.pdf',dpi=500,bbox_inches='tight')
plt.show()

