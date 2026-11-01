// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Student Registry Smart Contract
 * @dev SPPU BCT Practical 2: Uses Arrays, Structs, and Fallback/Receive functions.
 */
contract StudentRegistry {
    struct Student {
        uint256 id;
        string name;
        uint8 age;
        string dept;
    }

    Student[] public students;

    // Fallback & Receive: Triggered on unknown function calls or direct Ether transfer
    fallback() external payable {}
    receive() external payable {}

    // Add a new student record to the dynamic array
    function addStudent(
        uint256 _id,
        string memory _name,
        uint8 _age,
        string memory _dept
    ) public {
        students.push(Student(_id, _name, _age, _dept));
    }

    // Retrieve a student record by array index
    function getStudent(uint256 index)
        public
        view
        returns (uint256, string memory, uint8, string memory)
    {
        require(index < students.length, "Index out of bounds");
        Student memory s = students[index];
        return (s.id, s.name, s.age, s.dept);
    }

    // Return total number of enrolled students
    function count() public view returns (uint256) {
        return students.length;
    }
}
