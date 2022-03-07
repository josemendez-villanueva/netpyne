"""
init.py

Starting script to run NetPyNE-based M1 model.

Usage:
    python init.py # Run simulation, optionally plot a raster

MPI usage:
    mpiexec -n 4 nrniv -python -mpi init.py
"""


from netpyne import sim

netParams, cfg = sim.loadFromIndex('index.npjson', method='python')
print("Starting sim ...")
sim.createSimulateAnalyze(netParams, cfg)

# Check the model output: sim.checkOutput is used for testing purposes.  Please comment out the following line if you are exploring the example.
sim.checkOutput('M1detailed')
