## 21. Merge Two Sorted Lists

Given two sorted linked list, the idea is to create a merged list.

My solution creates a new linked list with the combination of the two list. The idea is to have two pointers, one to the list1 and the other, to list2. The pointers will transverse both list only once. 

The time complexity is O(m+n) in worst case scenario being m the length of list 1 and m the length of list 2. The space complexity is also O(m+n) because I'm adding extra space for the merged list. This list will have all elements in both lists.

Problem statement: https://leetcode.com/problems/merge-two-sorted-lists/