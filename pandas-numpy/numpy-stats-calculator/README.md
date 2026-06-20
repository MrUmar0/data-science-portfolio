NumPy Stats Calculator

A beginner data science project that generates monthly sales data and calculates key statistical metrics using NumPy.

What it does


Generates 12 months of random sales data using NumPy
Calculates basic stats — Mean, Median, Std, Variance
Finds Min and Max sales
Computes 25th, 50th, 75th Percentiles
Normalizes data to 0-1 range using Min-Max scaling


How to run


Install dependency:


   pip install numpy


Run the script:


   python numpy_stats_calculator.py

Concepts used

ConceptFunctionMeannp.mean()Mediannp.median()Standard Deviationnp.std()Variancenp.var()Min / Maxnp.min(), np.max()Percentilesnp.percentile()NormalizationMin-Max formulaRandom Datanp.random.randint()

Folder structure

data-science/numpy/
├── numpy_stats_calculator.py
└── README.md