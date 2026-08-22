# DSA in Python

> A growing, hands-on collection of data structures and algorithm practice in Python.

This repository is organized by topic and problem pattern. It includes LeetCode solutions, foundational exercises, helper files, and small experiments. The overview below mirrors the folders on disk as of **22 August 2026**.

## At A Glance

| Metric | Current count |
| --- | ---: |
| Topic folders | 14 |
| Practice files | 140 |


## Topic Map

| Topic | Files | Focus |
| --- | ---: | --- |
| [Array](Array/) | 29 | Searching, sorting, rotation, subarrays, and two pointers |
| [Binary Tree](Binary%20Tree/) | 17 | Traversals, views, construction, and tree properties |
| [DP](DP/) | 4 | One-dimensional dynamic programming and string segmentation |
| [Frequency_map](Frequency_map/) | 5 | Counting, lookup tables, and frequency-based decisions |
| [Greedy Algorithm](Greedy%20Algorithm/) | 3 | Local choices, reachability, and resource allocation |
| [Heap](Heap/) | 1 | Priority-based selection and top-k problems |
| [Intervals](Intervals/) | 1 | Range compression and interval summaries |
| [Leetcode](Leetcode/) | 29 | Mixed interview-style problems across several patterns |
| [Linked List](Linked%20List/) | 15 | Pointer movement, mutation, cycles, and reordering |
| [Queue](Queue/) | 0 | Reserved for future queue implementations and problems |
| [Recursion](Recursion/) | 8 | Base cases, recursive state, and backtracking foundations |
| [Sliding Window](Sliding%20Window/) | 3 | Fixed and variable-size window techniques |
| [Stack](Stack/) | 5 | Matching, monotonic behavior, and simulation |
| [Strings](Strings/) | 20 | Parsing, matching, transformation, and character maps |

## Suggested Practice Route

1. Start with the helper files in `Array`, `Frequency_map`, `Recursion`, and `Stack`.
2. Build pattern fluency with `Array`, `Strings`, `Sliding Window`, `Greedy Algorithm`, and `Intervals`.
3. Move into pointer-heavy structures in `Linked List` and `Binary Tree`.
4. Finish with `DP`, `Heap`, and the mixed `Leetcode` set.
5. Add small edge-case examples while studying each solution.

## How To Run

From the repository root:

```powershell
python ".\Array\Two Sum problem.py"
```

Because many filenames contain spaces, quote the path when running a file. Most files are standalone practice scripts; LeetCode-style files generally expose a `Solution` class or a method intended for the platform harness.

## Complete Catalog

The catalog is grouped by folder so it stays easy to scan. Filenames are preserved exactly as they appear on disk, including spaces, capitalization, and historical typos.

<details>
<summary><strong>Array</strong> · 29 files</summary>

[`Array/`](Array/) contains foundational array exercises and the following problem files:

- [`1.0 arr.py`](Array/1.0%20arr.py)
- [`1464. Maximum Product of Two Elements in an Array.py`](Array/1464.%20Maximum%20Product%20of%20Two%20Elements%20in%20an%20Array.py)
- [`164. Maximum Gap.py`](Array/164.%20Maximum%20Gap.py)
- [`169. Majority Element.py`](Array/169.%20Majority%20Element.py)
- [`1752. Check if Array Is Sorted and Rotated.py`](Array/1752.%20Check%20if%20Array%20Is%20Sorted%20and%20Rotated.py)
- [`2.0arr.py`](Array/2.0arr.py)
- [`215. Kth Largest Element in an Array.py`](Array/215.%20Kth%20Largest%20Element%20in%20an%20Array.py)
- [`2nd largest elemnet.py`](Array/2nd%20largest%20elemnet.py)
- [`3.0arr.py`](Array/3.0arr.py)
- [`34. Find First and Last Position of Element in Sorted Array.py`](Array/34.%20Find%20First%20and%20Last%20Position%20of%20Element%20in%20Sorted%20Array.py)
- [`4.0 arr.py`](Array/4.0%20arr.py)
- [`80. Remove Duplicates from Sorted Array II.py`](Array/80.%20Remove%20Duplicates%20from%20Sorted%20Array%20II.py)
- [`Buy Sell stock.py`](Array/Buy%20Sell%20stock.py)
- [`check sorted array.py`](Array/check%20sorted%20array.py)
- [`consecutive secqunce.py`](Array/consecutive%20secqunce.py)
- [`Find missing number.py`](Array/Find%20missing%20number.py)
- [`Find the Maximum Subarray Sum.py`](Array/Find%20the%20Maximum%20Subarray%20Sum.py)
- [`Largest element.py`](Array/Largest%20element.py)
- [`Linear Search.py`](Array/Linear%20Search.py)
- [`Max Consecutive Ones.py`](Array/Max%20Consecutive%20Ones.py)
- [`Merge two sorted list.py`](Array/Merge%20two%20sorted%20list.py)
- [`Move zeros to end.py`](Array/Move%20zeros%20to%20end.py)
- [`Rearrange Array Elements by Sign.py`](Array/Rearrange%20Array%20Elements%20by%20Sign.py)
- [`Remove duplicates.py`](Array/Remove%20duplicates.py)
- [`Rotate 2d array.py`](Array/Rotate%202d%20array.py)
- [`Rotate an array 1th place.py`](Array/Rotate%20an%20array%201th%20place.py)
- [`Rotate array by k places.py`](Array/Rotate%20array%20by%20k%20places.py)
- [`Three sum.py`](Array/Three%20sum.py)
- [`Two Sum problem.py`](Array/Two%20Sum%20problem.py)

</details>

<details>
<summary><strong>Binary Tree</strong> · 17 files</summary>

[`Binary Tree/`](Binary%20Tree/) covers helper code, traversals, views, construction, and tree transformations.

- [`1.0 BinaryTree.py`](Binary%20Tree/1.0%20BinaryTree.py)
- [`104. Maximum Depth of Binary Tree.py`](Binary%20Tree/104.%20Maximum%20Depth%20of%20Binary%20Tree.py)
- [`105. Construct Binary Tree from Preorder and Inorder Traversal.py`](Binary%20Tree/105.%20Construct%20Binary%20Tree%20from%20Preorder%20and%20Inorder%20Traversal.py)
- [`106. Construct Binary Tree from Inorder and Postorder Traversal.py`](Binary%20Tree/106.%20Construct%20Binary%20Tree%20from%20Inorder%20and%20Postorder%20Traversal.py)
- [`114. Flatten Binary Tree to Linked List.py`](Binary%20Tree/114.%20Flatten%20Binary%20Tree%20to%20Linked%20List.py)
- [`117. Populating Next Right Pointers in Each Node II.py`](Binary%20Tree/117.%20Populating%20Next%20Right%20Pointers%20in%20Each%20Node%20II.py)
- [`124. Binary Tree Maximum Path Sum.py`](Binary%20Tree/124.%20Binary%20Tree%20Maximum%20Path%20Sum.py)
- [`129. Sum Root to Leaf Numbers.py`](Binary%20Tree/129.%20Sum%20Root%20to%20Leaf%20Numbers.py)
- [`144. Binary Tree Preorder Traversal.py`](Binary%20Tree/144.%20Binary%20Tree%20Preorder%20Traversal.py)
- [`199. Binary Tree Right Side View.py`](Binary%20Tree/199.%20Binary%20Tree%20Right%20Side%20View.py)
- [`222. Count Complete Tree Nodes.py`](Binary%20Tree/222.%20Count%20Complete%20Tree%20Nodes.py)
- [`226. Invert Binary Tree.py`](Binary%20Tree/226.%20Invert%20Binary%20Tree.py)
- [`2415. Reverse Odd Levels of Binary Tree.py`](Binary%20Tree/2415.%20Reverse%20Odd%20Levels%20of%20Binary%20Tree.py)
- [`637. Average of Levels in Binary Tree.py`](Binary%20Tree/637.%20Average%20of%20Levels%20in%20Binary%20Tree.py)
- [`662. Maximum Width of Binary Tree.py`](Binary%20Tree/662.%20Maximum%20Width%20of%20Binary%20Tree.py)
- [`94. Binary Tree Inorder Traversal.py`](Binary%20Tree/94.%20Binary%20Tree%20Inorder%20Traversal.py)
- [`987. Vertical Order Traversal of a Binary Tree.py`](Binary%20Tree/987.%20Vertical%20Order%20Traversal%20of%20a%20Binary%20Tree.py)

</details>

<details>
<summary><strong>DP</strong> · 4 files</summary>

- [`139. Word Break.py`](DP/139.%20Word%20Break.py)
- [`198. House Robber.py`](DP/198.%20House%20Robber.py)
- [`213. House Robber II.py`](DP/213.%20House%20Robber%20II.py)
- [`70. Climbing Stairs.py`](DP/70.%20Climbing%20Stairs.py)

</details>

<details>
<summary><strong>Frequency_map</strong> · 5 files</summary>

- [`1.0 hash.py`](Frequency_map/1.0%20hash.py)
- [`2.0 hash.py`](Frequency_map/2.0%20hash.py)
- [`3.0 hash.py`](Frequency_map/3.0%20hash.py)
- [`3517. Smallest Palindromic Rearrangement I.py`](Frequency_map/3517.%20Smallest%20Palindromic%20Rearrangement%20I.py)
- [`4.0 hash.py`](Frequency_map/4.0%20hash.py)

</details>

<details>
<summary><strong>Greedy Algorithm</strong> · 3 files</summary>

- [`455. Assign Cookies.py`](Greedy%20Algorithm/455.%20Assign%20Cookies.py)
- [`55. Jump Game.py`](Greedy%20Algorithm/55.%20Jump%20Game.py)
- [`860. Lemonade Change.py`](Greedy%20Algorithm/860.%20Lemonade%20Change.py)

</details>

<details>
<summary><strong>Heap</strong> · 1 file</summary>

- [`215. Kth Largest Element in an Array.py`](Heap/215.%20Kth%20Largest%20Element%20in%20an%20Array.py)

</details>

<details>
<summary><strong>Intervals</strong> · 1 file</summary>

- [`228. Summary Ranges.py`](Intervals/228.%20Summary%20Ranges.py)

</details>

<details>
<summary><strong>Leetcode</strong> · 29 files</summary>

[`Leetcode/`](Leetcode/) contains the mixed problem set, including recent additions such as 3622.

- [`1189. Maximum Number of Balloons.py`](Leetcode/1189.%20Maximum%20Number%20of%20Balloons.py)
- [`13. Roman to Integer.py`](Leetcode/13.%20Roman%20to%20Integer.py)
- [`1344. Angle Between Hands of a Clock.py`](Leetcode/1344.%20Angle%20Between%20Hands%20of%20a%20Clock.py)
- [`1441. Build an Array With Stack Operations.py`](Leetcode/1441.%20Build%20an%20Array%20With%20Stack%20Operations.py)
- [`1732. Find the Highest Altitude.py`](Leetcode/1732.%20Find%20the%20Highest%20Altitude.py)
- [`1979. Find Greatest Common Divisor of Array.py`](Leetcode/1979.%20Find%20Greatest%20Common%20Divisor%20of%20Array.py)
- [`2144. Minimum Cost of Buying Candies With Discount.py`](Leetcode/2144.%20Minimum%20Cost%20of%20Buying%20Candies%20With%20Discount.py)
- [`2220. Minimum Bit Flips to Convert Number Solved.py`](Leetcode/2220.%20Minimum%20Bit%20Flips%20to%20Convert%20Number%20Solved.py)
- [`2540. Minimum Common Value.py`](Leetcode/2540.%20Minimum%20Common%20Value.py)
- [`2544. Alternating Digit Sum.py`](Leetcode/2544.%20Alternating%20Digit%20Sum.py)
- [`27. Remove Element.py`](Leetcode/27.%20Remove%20Element.py)
- [`287. Find the Duplicate Number.py`](Leetcode/287.%20Find%20the%20Duplicate%20Number.py)
- [`29. Divide Two Integers.py`](Leetcode/29.%20Divide%20Two%20Integers.py)
- [`3120. Count the Number of Special Characters I.py`](Leetcode/3120.%20Count%20the%20Number%20of%20Special%20Characters%20I.py)
- [`3121. Count the Number of Special Characters II.py`](Leetcode/3121.%20Count%20the%20Number%20of%20Special%20Characters%20II.py)
- [`326. Power of Three.py`](Leetcode/326.%20Power%20of%20Three.py)
- [`3300. Minimum Element After Replacement With Digit Sum.py`](Leetcode/3300.%20Minimum%20Element%20After%20Replacement%20With%20Digit%20Sum.py)
- [`342. Power of Four.py`](Leetcode/342.%20Power%20of%20Four.py)
- [`3622. Check Divisibility by Digit Sum and Product.py`](Leetcode/3622.%20Check%20Divisibility%20by%20Digit%20Sum%20and%20Product.py)
- [`3633. Earliest Finish Time for Land and Water Rides.py`](Leetcode/3633.%20Earliest%20Finish%20Time%20for%20Land%20and%20Water%20Rides.py)
- [`397. Integer Replacement.py`](Leetcode/397.%20Integer%20Replacement.py)
- [`4000. Largest Integer With Given Digit Sum.py`](Leetcode/4000.%20Largest%20Integer%20With%20Given%20Digit%20Sum.py)
- [`645. Set Mismatch.py`](Leetcode/645.%20Set%20Mismatch.py)
- [`67. Add Binary.py`](Leetcode/67.%20Add%20Binary.py)
- [`7. Reverse Integer.py`](Leetcode/7.%20Reverse%20Integer.py)
- [`78. Subsets.py`](Leetcode/78.%20Subsets.py)
- [`788. Rotated Digits.py`](Leetcode/788.%20Rotated%20Digits.py)
- [`uglynumber.py`](Leetcode/uglynumber.py)
- [`uglynumberII.py`](Leetcode/uglynumberII.py)

</details>

<details>
<summary><strong>Linked List</strong> · 15 files</summary>

- [`1.0 linkedList.py`](Linked%20List/1.0%20linkedList.py)
- [`143. Reorder List.py`](Linked%20List/143.%20Reorder%20List.py)
- [`148. Sort List.py`](Linked%20List/148.%20Sort%20List.py)
- [`2.Add Two Numbers.py`](Linked%20List/2.Add%20Two%20Numbers.py)
- [`2095. Delete the Middle Node of a Linked List.py`](Linked%20List/2095.%20Delete%20the%20Middle%20Node%20of%20a%20Linked%20List.py)
- [`237. Delete Node in a Linked List.py`](Linked%20List/237.%20Delete%20Node%20in%20a%20Linked%20List.py)
- [`61. Rotate List.py`](Linked%20List/61.%20Rotate%20List.py)
- [`83. Remove Duplicates from Sorted List.py`](Linked%20List/83.%20Remove%20Duplicates%20from%20Sorted%20List.py)
- [`length of cycle.py`](Linked%20List/length%20of%20cycle.py)
- [`List cycle.py`](Linked%20List/List%20cycle.py)
- [`Middle of the Linked List.py`](Linked%20List/Middle%20of%20the%20Linked%20List.py)
- [`odd even linked list.py`](Linked%20List/odd%20even%20linked%20list.py)
- [`palindrome linked list.py`](Linked%20List/palindrome%20linked%20list.py)
- [`remove element from last.py`](Linked%20List/remove%20element%20from%20last.py)
- [`Remove Linked List Elements.py`](Linked%20List/Remove%20Linked%20List%20Elements.py)

</details>

<details>
<summary><strong>Queue</strong> · 0 files</summary>

This folder is currently empty and reserved for queue practice.

</details>

<details>
<summary><strong>Recursion</strong> · 8 files</summary>

- [`1-N using recursion.py`](Recursion/1-N%20using%20recursion.py)
- [`array reverse.py`](Recursion/array%20reverse.py)
- [`Factorial recursion.py`](Recursion/Factorial%20recursion.py)
- [`fibonacci series.py`](Recursion/fibonacci%20series.py)
- [`functional recursion.py`](Recursion/functional%20recursion.py)
- [`Head tail recursion.py`](Recursion/Head%20tail%20recursion.py)
- [`palindrome string.py`](Recursion/palindrome%20string.py)
- [`palindrome.py`](Recursion/palindrome.py)

</details>

<details>
<summary><strong>Sliding Window</strong> · 3 files</summary>

- [`1004. Max Consecutive Ones III.py`](Sliding%20Window/1004.%20Max%20Consecutive%20Ones%20III.py)
- [`1423. Maximum Points You Can Obtain from Cards.py`](Sliding%20Window/1423.%20Maximum%20Points%20You%20Can%20Obtain%20from%20Cards.py)
- [`209. Minimum Size Subarray Sum.py`](Sliding%20Window/209.%20Minimum%20Size%20Subarray%20Sum.py)

</details>

<details>
<summary><strong>Stack</strong> · 5 files</summary>

- [`1.0 stack.py`](Stack/1.0%20stack.py)
- [`155. Min Stack.py`](Stack/155.%20Min%20Stack.py)
- [`20. Valid Parentheses.py`](Stack/20.%20Valid%20Parentheses.py)
- [`232. Implement Queue using Stacks.py`](Stack/232.%20Implement%20Queue%20using%20Stacks.py)
- [`735. Asteroid Collision.py`](Stack/735.%20Asteroid%20Collision.py)

</details>

<details>
<summary><strong>Strings</strong> · 20 files</summary>

- [`125. Valid Palindrome.py`](Strings/125.%20Valid%20Palindrome.py)
- [`14. Longest Common Prefix.py`](Strings/14.%20Longest%20Common%20Prefix.py)
- [`2000. Reverse Prefix of Word.py`](Strings/2000.%20Reverse%20Prefix%20of%20Word.py)
- [`205. Isomorphic Strings.py`](Strings/205.%20Isomorphic%20Strings.py)
- [`2553. Separate the Digits in an Array.py`](Strings/2553.%20Separate%20the%20Digits%20in%20an%20Array.py)
- [`290. Word Pattern.py`](Strings/290.%20Word%20Pattern.py)
- [`3612. Process String with Special Operations I.py`](Strings/3612.%20Process%20String%20with%20Special%20Operations%20I.py)
- [`387. First Unique Character in a String.py`](Strings/387.%20First%20Unique%20Character%20in%20a%20String.py)
- [`392. Is Subsequence.py`](Strings/392.%20Is%20Subsequence.py)
- [`43. Multiply Strings.py`](Strings/43.%20Multiply%20Strings.py)
- [`451. Sort Characters By Frequency.py`](Strings/451.%20Sort%20Characters%20By%20Frequency.py)
- [`520. Detect Capital.py`](Strings/520.%20Detect%20Capital.py)
- [`58. Length of Last Word.py`](Strings/58.%20Length%20of%20Last%20Word.py)
- [`599. Minimum Index Sum of Two Lists.py`](Strings/599.%20Minimum%20Index%20Sum%20of%20Two%20Lists.py)
- [`796. Rotate String.py`](Strings/796.%20Rotate%20String.py)
- [`Largest Odd Number in String.py`](Strings/Largest%20Odd%20Number%20in%20String.py)
- [`leetcode-1021.py`](Strings/leetcode-1021.py)
- [`Longest Substring Without Repeating Characters.py`](Strings/Longest%20Substring%20Without%20Repeating%20Characters.py)
- [`Reverse Words in a String III.py`](Strings/Reverse%20Words%20in%20a%20String%20III.py)
- [`reverse words.py`](Strings/reverse%20words.py)

</details>

## Naming Notes

Filenames are intentionally left unchanged so links remain stable. A few names contain abbreviations, spaces, or historical typos; the catalog reflects the filesystem rather than silently renaming study material.

## Contributing

Add a focused solution to the most relevant topic folder. Keep examples runnable where practical, use descriptive filenames for new work, and update the counts and catalog in this README when adding or removing a file.

## License

This repository is for learning and practice. If you reuse code, please provide attribution.
