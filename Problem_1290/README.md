# 1290. Convert Binary Number in a Linked List to Integer

Tag: `Linked List`, `Math`

Link: [Problem 1290. Convert Binary Number in a Linked List to Integer](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/?envType=daily-question&envId=2025-07-14)

## Intuitive

Very simple problem, just go through the nodes in the linked list.

For every node, left shift the current result (equivalent to multiply by 2) and add the value of the current node.