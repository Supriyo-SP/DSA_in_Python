# DSA in Python

[![Language](https://img.shields.io/badge/language-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-Active-2EA043)](#)
[![Focus](https://img.shields.io/badge/focus-DSA-FF7A00)](#)
[![Practice](https://img.shields.io/badge/practice-daily-7C3AED)](#)
[![LeetCode](https://img.shields.io/badge/LeetCode-Supriyofury-FFA116?logo=leetcode&logoColor=white)](https://leetcode.com/u/Supriyofury/)

> A personal DSA notebook in Python, organized by topic for fast revision, interview prep, and steady problem solving.

Most linked-list files now include a small `ListNode` helper, one or two runnable test cases, and a short problem description at the top so they can be executed directly.

## Snake Run

<p align="center">
	<svg width="100%" viewBox="0 0 960 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A playful snake eating DSA topics">
		<defs>
			<linearGradient id="bgGlow" x1="0%" y1="0%" x2="100%" y2="100%">
				<stop offset="0%" stop-color="#0f172a" />
				<stop offset="55%" stop-color="#111827" />
				<stop offset="100%" stop-color="#052e16" />
			</linearGradient>
			<linearGradient id="snakeSkin" x1="0%" y1="0%" x2="100%" y2="0%">
				<stop offset="0%" stop-color="#bef264" />
				<stop offset="100%" stop-color="#22c55e" />
			</linearGradient>
			<filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">
				<feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#000000" flood-opacity="0.35" />
			</filter>
		</defs>

		<rect x="16" y="16" width="928" height="228" rx="28" fill="url(#bgGlow)" />
		<text x="48" y="56" fill="#f8fafc" font-size="28" font-family="Verdana, Geneva, sans-serif" font-weight="700">
			Snake Run: the topics get gobbled one by one
		</text>
		<text x="48" y="84" fill="#94a3b8" font-size="14" font-family="Verdana, Geneva, sans-serif">
			Arrays, Lists, Stack, Strings, and friends are on the menu.
		</text>

		<g filter="url(#softShadow)" font-family="Verdana, Geneva, sans-serif" font-weight="700" font-size="16">
			<g transform="translate(70 150)">
				<rect width="110" height="42" rx="21" fill="#1d4ed8">
					<animate attributeName="opacity" values="1;0.35;1" dur="7.2s" begin="0s" repeatCount="indefinite" />
				</rect>
				<text x="55" y="27" text-anchor="middle" fill="#eff6ff">Array</text>
			</g>
			<g transform="translate(210 108)">
				<rect width="98" height="42" rx="21" fill="#7c3aed">
					<animate attributeName="opacity" values="1;0.35;1" dur="7.2s" begin="1.2s" repeatCount="indefinite" />
				</rect>
				<text x="49" y="27" text-anchor="middle" fill="#f5f3ff">List</text>
			</g>
			<g transform="translate(348 150)">
				<rect width="112" height="42" rx="21" fill="#b45309">
					<animate attributeName="opacity" values="1;0.35;1" dur="7.2s" begin="2.4s" repeatCount="indefinite" />
				</rect>
				<text x="56" y="27" text-anchor="middle" fill="#fff7ed">Stack</text>
			</g>
			<g transform="translate(504 108)">
				<rect width="122" height="42" rx="21" fill="#0f766e">
					<animate attributeName="opacity" values="1;0.35;1" dur="7.2s" begin="3.6s" repeatCount="indefinite" />
				</rect>
				<text x="61" y="27" text-anchor="middle" fill="#ecfeff">Strings</text>
			</g>
			<g transform="translate(668 150)">
				<rect width="110" height="42" rx="21" fill="#dc2626">
					<animate attributeName="opacity" values="1;0.35;1" dur="7.2s" begin="4.8s" repeatCount="indefinite" />
				</rect>
				<text x="55" y="27" text-anchor="middle" fill="#fef2f2">Queue</text>
			</g>
			<g transform="translate(812 108)">
				<rect width="118" height="42" rx="21" fill="#16a34a">
					<animate attributeName="opacity" values="1;0.35;1" dur="7.2s" begin="6s" repeatCount="indefinite" />
				</rect>
				<text x="59" y="27" text-anchor="middle" fill="#f0fdf4">Trees</text>
			</g>
		</g>

		<path id="snakePath" d="M60 194 C150 92, 250 92, 340 194 S530 296, 620 194 S790 92, 900 194" fill="none" stroke="url(#snakeSkin)" stroke-width="26" stroke-linecap="round" stroke-dasharray="20 12">
			<animate attributeName="stroke-dashoffset" from="0" to="-320" dur="2.8s" repeatCount="indefinite" />
		</path>

		<g filter="url(#softShadow)">
			<g>
				<animateMotion dur="7.2s" repeatCount="indefinite" rotate="auto">
					<mpath href="#snakePath" />
				</animateMotion>
				<circle cx="0" cy="0" r="22" fill="#bef264" />
				<circle cx="8" cy="-5" r="3" fill="#052e16" />
				<circle cx="8" cy="5" r="3" fill="#052e16" />
				<path d="M14 12 L24 16" stroke="#fb7185" stroke-width="3" stroke-linecap="round" />
			</g>
		</g>
	</svg>
</p>

The snake is here for fun only, but the topics really do get eaten in this notebook.

## What's Inside

- Topic-first folders for quick navigation
- Single-file solutions that are easy to read and run
- Runnable linked-list examples with lightweight test cases for local verification
- Coverage across arrays, hashing, recursion, linked lists, stacks, strings, and sliding window patterns
- A growing set of LeetCode and classic interview problems

## LeetCode Profile

I also keep my LeetCode practice here:

- [Supriyofury on LeetCode](https://leetcode.com/u/Supriyofury/)

## Folder Guide

| Folder | Focus | Status |
| --- | --- | --- |
| Array/ | searching, rotation, subarray patterns, two-sum, three-sum, max subarray | Done |
| Frequency_map/ | hashing and frequency-based patterns | Done |
| Greedy Algorithm/ | greedy strategies and scheduling-style problems | Done |
| Recursion/ | recursion basics, factorial, Fibonacci, palindrome checks | Done |
| Linked List/ | list operations, cycles, middle, odd-even, deletion, runnable examples | Done |
| strings/ | string algorithms, prefix/suffix patterns, substring problems | Done |
| Stack/ | stack operations, parentheses, min stack, queue using stacks | Done |
| Sliding Window/ | window-based counting and max/min patterns | In progress |
| Leetcode/ | mixed problem-solving practice and numbered LeetCode solutions | In progress |
| Queue/ | queue problems | Not started |

## Progress Roadmap

- [x] Arrays: search, rotation, subarray, two-sum, three-sum
- [x] Hashing/Frequency Map: counting and map-based patterns
- [x] Greedy: assign cookies and related problems
- [x] Recursion: basics, factorial, Fibonacci, palindrome
- [x] Linked Lists: middle, cycle, deletion, reorder, sort, runnable examples
- [x] Strings: prefix, subsequence, substring, reverse-word patterns
- [x] Stack: valid parentheses, min stack, queue using stacks, asteroid collision
- [x] Sliding Window: max consecutive ones patterns
- [x] LeetCode practice: assorted number theory, arrays, and set problems
- [ ] Trees: traversals, BST operations
- [ ] Graphs: BFS, DFS, shortest paths
- [ ] Dynamic Programming: 1D/2D patterns, knapsack
- [ ] Bit Manipulation: common tricks and interview problems

## How To Use

1. Pick a topic folder.
2. Open any `.py` file to review the solution.
3. Run files directly with Python if you want to test locally.
4. Linked-list files can be executed as-is because they include their own node helpers and sample inputs.

Example:

```bash
python "Array/Two Sum problem.py"
```

Linked list example:

```bash
python "Linked List/2095. Delete the Middle Node of a Linked List.py"
```

## Contributing

Add new problems, refine existing solutions, or improve naming and structure. Keep filenames descriptive and place each solution in the most relevant folder.

## License

This repository is for learning and practice. If you reuse code, please provide attribution 😀.
