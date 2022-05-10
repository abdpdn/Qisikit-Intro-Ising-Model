import numpy as np

lmbd = np.arange(0.0, 2.25, 0.25)
sigmaz = []


def exact(lam):
    if lam < 1:
        return lam / (2 * np.sqrt(1 + lam ** 2))
    if lam > 1:
        return 1 / 2 + lam / (2 * np.sqrt(1 + lam ** 2))
    return None


for lam in lmbd:
    sigmaz.append(exact(lam))

np.save(f'data/ising_exact.npy', sigmaz)

