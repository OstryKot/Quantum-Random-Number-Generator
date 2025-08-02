from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Utworzenie prostego obwodu kwantowego
qc = QuantumCircuit(2, 2)
qc.h(0)  # Bramka Hadamarda na qubit 0
qc.cx(0, 1)  # CNOT między qubit 0 i 1
qc.measure_all()

print("Obwód kwantowy utworzony!")
print(qc)

# Symulacja
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit, shots=1000).result()
counts = result.get_counts()

print("Wyniki symulacji:", counts)
plot_histogram(counts).show()
plt.show()



