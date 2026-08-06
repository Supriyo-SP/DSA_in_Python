import random


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        Return True if s can be segmented into words from wordDict.
        """
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                end = i + len(word)
                if end <= len(s) and s[i:end] == word and dp[end]:
                    dp[i] = True
                    break

        return dp[0]


def generate_random_test_case():
    word_bank = ["leet", "code", "apple", "pen", "cats", "sand", "dog", "and", "cat", "an", "car", "banana", "a", "b", "c", "d"]
    parts = [random.choice(word_bank) for _ in range(random.randint(1, 4))]
    s = "".join(parts)

    extra_words = [random.choice(word_bank) for _ in range(random.randint(0, 2))]
    word_dict = sorted(set(parts + extra_words))
    return s, word_dict


def run_random_tests(count=10):
    solver = Solution()
    for idx in range(1, count + 1):
        s, word_dict = generate_random_test_case()
        result = solver.wordBreak(s, word_dict)
        print(f"Test {idx}: s={s!r}, wordDict={word_dict}, result={result}")


if __name__ == "__main__":
    solver = Solution()

    print("Example 1:")
    print(solver.wordBreak("leetcode", ["leet", "code"]))
    print()

    print("Example 2:")
    print(solver.wordBreak("catsanddog", ["cat", "cats", "sand", "and", "dog"]))
    print()

    print("Random test cases:")
    run_random_tests()