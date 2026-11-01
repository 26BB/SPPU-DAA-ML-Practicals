# 🏦 Practical 1: Bank Smart Contract

## Problem Statement
Write a smart contract on a test network for a Bank account of a customer with the following operations:
1. Deposit money
2. Withdraw money
3. Show balance

---

## 🚀 How to Run in Remix IDE (Zero Setup)

1. Open **[Remix Ethereum IDE](https://remix.ethereum.org)** in any browser.
2. In the left sidebar file explorer under `contracts/`, create a new file named `Bank.sol`.
3. Copy and paste the code from [`Bank.sol`](./Bank.sol).
4. Press **`Ctrl + S`** to compile the contract.
5. Navigate to the **"Deploy & Run Transactions"** tab (Ethereum logo on the left):
   - **Environment:** Select `Remix VM (Cancun)` (provides 10 accounts with 100 free test ETH).
   - Click the orange **Deploy** button.
6. Under **"Deployed Contracts"** at the bottom left, expand `Bank`:
   - **Deposit:** Enter an amount (e.g. `5`) in the **Value** box at the top, select unit `Ether` (or `Wei`), and click the red **`deposit`** button.
   - **Show Balance:** Click **`showBalance`** $\rightarrow$ returns your current balance in Wei (`5000000000000000000`).
   - **Withdraw:** In the `withdraw` input field, pass the amount in Wei (e.g. `2000000000000000000`) and click **`withdraw`** $\rightarrow$ balance updates and Ether transfers back to your account.
