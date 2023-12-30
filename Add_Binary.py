class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        # Traverse both strings from right to left
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            # Get the corresponding digits from a and b
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            # Calculate the sum and carry
            current_sum = digit_a + digit_b + carry
            carry = current_sum // 2

            # Append the remainder to the result (0 or 1)
            result.append(str(current_sum % 2))

            # Move to the next digits in both strings
            i -= 1
            j -= 1

        # Reverse the result and join as a string
        return ''.join(result[::-1])

# Example usage:
sol = Solution()
a = "11"
b = "1"
result = sol.addBinary(a, b)
print(result)
