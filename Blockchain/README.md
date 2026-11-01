# ⛓️ Blockchain Technology (BCT) Practicals

SPPU BE Computer Engineering (Semester 7) — Laboratory Practice III / Elective.

---

## 📋 Practicals Overview

| Practical | Topic / Problem Statement | Core Solidity Constructs | Execution Platform |
| :--- | :--- | :--- | :--- |
| **[Practical 1](./Practical%201/Bank.sol)** | Bank Account Smart Contract (Deposit, Withdraw, Show Balance) | `mapping`, `msg.sender`, `msg.value`, `payable`, `require` | Remix Ethereum IDE |
| **[Practical 2](./Practical%202/StudentRegistry.sol)** | Student Registry System | `struct`, Dynamic `Array`, `fallback()`, `receive()` | Remix Ethereum IDE |

---

## ⚡ Zero-Setup Execution via Remix IDE

No local blockchain or node installations needed:

1. Open **[remix.ethereum.org](https://remix.ethereum.org)**.
2. Create `<filename>.sol` under the `contracts/` directory.
3. Paste the contract code and hit **`Ctrl + S`** to compile.
4. Go to **Deploy & Run Transactions** $\rightarrow$ set Environment to **Remix VM (Cancun)** $\rightarrow$ click **Deploy**.
5. Test contract functions directly using the generated UI buttons under **Deployed Contracts**.

---

## 🎯 Key Viva & Exam Questions

1. **What is `payable` in Solidity?**
   - It is a modifier required on functions and addresses that intend to receive Ether. Without `payable`, sending Ether to that function results in an immediate transaction revert.

2. **What is the difference between `fallback()` and `receive()`?**
   - `receive()` is executed when Ether is sent directly to the contract with empty `calldata`.
   - `fallback()` is executed if no function signature matches the call data, or if `receive()` does not exist when Ether is sent.

3. **What is the difference between `memory` and `storage`?**
   - `storage` is permanently written onto the blockchain state (high gas cost).
   - `memory` is temporary execution memory wiped after the transaction finishes (low gas cost).

4. **Why use `mapping` instead of arrays for balances?**
   - Mappings offer $O(1)$ constant time lookup for any Ethereum address and do not consume gas iterating through an index.
