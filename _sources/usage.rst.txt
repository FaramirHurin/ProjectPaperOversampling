Usage
======

Run
----
.. code-block:: bash

    git clone https://github.com/FaramirHurin/ADV-O.git
    cd ADV-O
    pip install -r requirements.txt
    python main.py

 
Output
------

.. code-block:: bash

    Table 6: Synthetic data: R2 scores for the predicted features for various regressors.
                                                x_terminal_id  y_terminal_id  TX_AMOUNT
    MLPRegressor(max_iter=2000, random_state=42)           0.85           0.59       0.94
    Ridge(random_state=42)                                 0.85           0.58       0.93
    RandomForestRegressor(random_state=42)                 0.85           0.59       0.90
    Naive                                                  0.39           0.54       0.91


    Table 7: Synthetic data: accuracy of oversampling algorithms. All oversampling algorithms have been tested using a Balanced Random Forest. No oversampling has been tested with a classic Random Forest ('Baseline'),  and a Balanced Random Forest ('Baseline balanced').
                Baseline  Baseline_balanced  SMOTE  Random  KMeansSMOTE  ADVO
    PRAUC           0.32               0.37   0.36    0.37         0.36  0.37
    PRAUC_Card      0.45               0.50   0.46    0.49         0.48  0.48
    Precision       0.34               0.23   0.27    0.26         0.25  0.27
    Recall          0.29               0.89   0.68    0.72         0.73  0.69
    F1 score        0.31               0.36   0.39    0.38         0.37  0.39
    PK50            0.76               0.36   0.56    0.30         0.40  0.42
    PK100           0.78               0.37   0.52    0.38         0.39  0.45
    PK200           0.74               0.38   0.50    0.44         0.36  0.55
    PK500           0.61               0.40   0.50    0.40         0.40  0.55
    PK1000          0.48               0.42   0.46    0.44         0.40  0.48
    PK2000          0.36               0.38   0.40    0.39         0.38  0.41


    Table 8: Synthetic data: AUC of absolute differences between kde
                x_terminal_id  y_terminal_id  TX_AMOUNT
    SMOTE                 0.11           0.10       0.18
    Random                0.05           0.11       0.02
    KMeansSMOTE           0.05           0.10       0.02
    ADVO                  0.09           0.12       0.03

