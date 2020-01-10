import numpy as np

data1 = np.linspace(1, 10, 11)
data2 = np.logspace(0, 4, 11)
data3 = np.linspace(0.01, 0.02, 11)

np.savetxt('build/output.csv',
    np.column_stack([data1, data2, data3]),
    fmt='%.0f, %.0f, %.3f',
    header='data1, data2, data3')
