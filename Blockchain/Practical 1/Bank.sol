// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Bank Smart Contract
 * @dev SPPU BCT Practical 1: Deposit money, withdraw money, and show balance.
 */
contract Bank {
    mapping(address => uint256) public balanceOf;

    // Deposit money into the bank
    function deposit() public payable {
        require(msg.value > 0, "Deposit should be greater than zero.");
        balanceOf[msg.sender] += msg.value;
    }

    // Withdraw money from the bank
    function withdraw(uint256 amount) public {
        require(balanceOf[msg.sender] >= amount, "Insufficient balance.");
        balanceOf[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
    }

    // Check account balance of the caller
    function showBalance() public view returns (uint256) {
        return balanceOf[msg.sender];
    }
}
