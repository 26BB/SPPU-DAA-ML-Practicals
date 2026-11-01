# 🎓 SPPU BE Computer Engineering (Sem 7) — DAA, ML & BCT Practicals

A curated, self-contained repository with simplified, ready-to-run codes for **Design and Analysis of Algorithms (DAA)**, **Machine Learning (ML)**, and **Blockchain Technology (BCT)** practicals as per the Savitribai Phule Pune University (SPPU) BE Computer Engineering curriculum.

Designed specifically for **quick revision, lab exams, and zero-setup demonstration**, featuring 1-cell notebook implementations alongside modular standalone scripts and clean Solidity smart contracts.

---

## 📁 Repository Structure

```
SPPU-DAA-ML-Practicals/
├── DAA/
│   ├── EASY_1_CELL_DAA.ipynb              # All DAA practicals executable in 1 single cell each
│   ├── prac1_fibonacci.py                 # Iterative vs Recursive with Step/Call Counts & Plots
│   ├── prac2_huffman.py                   # Huffman Encoding with Min-Heap & Binary Codes
│   ├── prac3_fractional_knapsack.py       # Fractional Knapsack (Greedy Approach)
│   ├── prac4_01_knapsack.py               # 0/1 Knapsack (Dynamic Programming Matrix)
│   └── prac5_n_queens.py                  # N-Queens Problem with Backtracking
│
├── Machine_Learning/
│   ├── EASY_1_CELL_PRACTICALS.ipynb       # All ML practicals packaged into easy 1-cell blocks
│   ├── Practical 1/                       # Uber Fare Prediction (Regression)
│   │   ├── single_cell_code.py
│   │   ├── MLprac1.ipynb
│   │   └── uber.csv
│   ├── Practical 2/                       # KMeans & Elbow Method on Sales Data
│   │   ├── single_cell_code.py
│   │   ├── mlprac2.ipynb
│   │   └── sales_data_sample.csv
│   ├── Practical 3/                       # KNN Classifier on Pima Diabetes
│   │   ├── single_cell_code.py
│   │   ├── MLprac3.ipynb
│   │   └── diabetes.csv
│   ├── Practical 4/                       # Gradient Descent Optimization (y = (x+3)^2)
│   │   ├── single_cell_code.py
│   │   ├── MLprac4.ipynb
│   │   └── Churn_Modelling.csv
│   └── Practical 5/                       # Email Spam Classification (KNN & SVM)
│       ├── single_cell_code.py
│       ├── MLprac5.ipynb
│       └── emails.csv
│
└── Blockchain/
    ├── README.md                          # Quick guide & key viva questions
    ├── Practical 1/                       # Bank Account Smart Contract
    │   ├── Bank.sol                       # Minimal deposit, withdraw & balance contract
    │   └── README.md
    └── Practical 2/                       # Student Registry Smart Contract
        ├── StudentRegistry.sol            # Structs, Arrays, Fallback & Receive contract
        └── README.md
```

---

## ⚡ 1. Design & Analysis of Algorithms (DAA)

| Practical | Topic / Problem | Paradigm / Algorithm | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- | :--- |
| **Prac 1** | Fibonacci Numbers | Iterative vs Recursive | $O(N)$ vs $O(2^N)$ | $O(1)$ vs $O(N)$ |
| **Prac 2** | Huffman Encoding | Greedy (Min-Heap / Priority Queue) | $O(N \log N)$ | $O(N)$ |
| **Prac 3** | Fractional Knapsack | Greedy (Value-to-Weight Ratio) | $O(N \log N)$ | $O(1)$ |
| **Prac 4** | 0/1 Knapsack | Dynamic Programming (2D Table) | $O(N \cdot W)$ | $O(N \cdot W)$ |
| **Prac 5** | N-Queens Problem | Backtracking | $O(N!)$ | $O(N^2)$ |

### Quick Run:
```bash
# Run any practical directly:
python DAA/prac1_fibonacci.py
python DAA/prac2_huffman.py
python DAA/prac3_fractional_knapsack.py
python DAA/prac4_01_knapsack.py
python DAA/prac5_n_queens.py

# Or launch Jupyter Notebook:
jupyter notebook DAA/EASY_1_CELL_DAA.ipynb
```

---

## 🤖 2. Machine Learning (ML)

| Practical | Title | Models / Techniques Used | Metrics / Output |
| :--- | :--- | :--- | :--- |
| **Prac 1** | Uber Fare Prediction | Linear Regression, Random Forest, Outlier Handling | RMSE, $R^2$ Score |
| **Prac 2** | Sales Customer Clustering | K-Means Clustering, Elbow Method, WCSS | Optimal Cluster Count & Scatter Plot |
| **Prac 3** | Diabetes Classification | K-Nearest Neighbors ($K=5$), Feature Scaling | Confusion Matrix, Accuracy, Precision, Recall |
| **Prac 4** | Gradient Descent | Gradient Descent Optimization on $y = (x+3)^2$ | Local Minima Iterations, Cost Function Path |
| **Prac 5** | Email Spam Classification | KNN Classifier vs Support Vector Machine (SVM) | Accuracy, Confusion Matrix Comparison |

### Quick Run:
All datasets are included locally in their respective practical folders.

```bash
# Run single-cell scripts:
cd "Machine_Learning/Practical 1" && python single_cell_code.py
cd "Machine_Learning/Practical 2" && python single_cell_code.py
cd "Machine_Learning/Practical 3" && python single_cell_code.py
cd "Machine_Learning/Practical 4" && python single_cell_code.py
cd "Machine_Learning/Practical 5" && python single_cell_code.py

# Or launch the unified notebook:
jupyter notebook Machine_Learning/EASY_1_CELL_PRACTICALS.ipynb
```

---

## ⛓️ 3. Blockchain Technology (BCT)

| Practical | Topic / Problem Statement | Core Solidity Constructs | Execution Platform |
| :--- | :--- | :--- | :--- |
| **[Prac 1](./Blockchain/Practical%201/)** | Bank Account Smart Contract (Deposit, Withdraw, Balance) | `mapping`, `msg.sender`, `msg.value`, `payable`, `require` | Remix Ethereum IDE |
| **[Prac 2](./Blockchain/Practical%202/)** | Student Registry Smart Contract | `struct`, Dynamic `Array`, `fallback()`, `receive()` | Remix Ethereum IDE |

### Quick Run (Zero Setup in Remix IDE):
1. Open **[remix.ethereum.org](https://remix.ethereum.org)**.
2. Create `Bank.sol` or `StudentRegistry.sol` under `contracts/` and paste the code.
3. Hit **`Ctrl + S`** to compile.
4. Select **Remix VM (Cancun)** under **Deploy & Run Transactions** and click **Deploy**.
5. Test interactively using the auto-generated contract buttons.

---

## 🛠️ Prerequisites & Setup

Ensure you have Python 3.8+ installed:

```bash
# Clone the repository
git clone https://github.com/26BB/SPPU-DAA-ML-Practicals.git
cd SPPU-DAA-ML-Practicals

# Install common dependencies
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
```

---

## 👨‍💻 Author
- **Bhushan Bhosale** ([@26BB](https://github.com/26BB))
- Department of Computer Engineering
