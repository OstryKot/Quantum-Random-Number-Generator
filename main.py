from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Utworzenie prostego obwodu kwantowego
qc = QuantumCircuit(4, 4)

#bramka hadamarda na qubity 0,1,2,3
for i in range(4): 
    qc.h(i)

qc.measure_all()

print("Obwód kwantowy utworzony!")
print(qc)


print("Generator liczb losowych:")
print(qc.draw())


backend = AerSimulator()
result = backend.run(qc, shots=100).result()

counts = result.get_counts()

plot_histogram(counts).show()   
plt.show()  

print(counts)
print ("Przykładowka wynik", list(counts.keys())[:5])
