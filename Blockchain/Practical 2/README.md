# 🎓 Practical 2: Student Data Smart Contract

## Problem Statement
Write a program in Solidity to create Student data using the following constructs:
1. **Arrays** (`Student[] public students`)
2. **Structures** (`struct Student { ... }`)
3. **Fallback / Receive function** (`fallback()`, `receive()`)
Deploy this smart contract on an Ethereum test network / Remix IDE.

---

## 🚀 How to Run in Remix IDE (Zero Setup)

1. Open **[Remix Ethereum IDE](https://remix.ethereum.org)**.
2. In the left sidebar under `contracts/`, create a file named `StudentRegistry.sol`.
3. Paste the code from [`StudentRegistry.sol`](./StudentRegistry.sol).
4. Press **`Ctrl + S`** to compile.
5. In the **"Deploy & Run Transactions"** tab:
   - **Environment:** Select `Remix VM (Cancun)`.
   - Click **Deploy**.
6. Under **"Deployed Contracts"**:
   - **Add Student:** Expand **`addStudent`**, enter `101, "Alice", 21, "Comp"` and click **transact**.
   - **View Student:** Enter `0` in **`students`** or **`getStudent`** $\rightarrow$ returns student details.
   - **Total Count:** Click **`count`** $\rightarrow$ returns `1`.
   - **Trigger Fallback:** At the bottom under **"Low level interactions"**, enter `1` Ether in the Value box at the top, leave calldata empty, and click **Transact** $\rightarrow$ contract receives Ether and invokes the fallback/receive function.
