class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        resultado = []
        min_len = min(len(word1), len(word2))

        for i in range(min_len):
            resultado.append(word1[i])
            resultado.append(word2[i])

        resultado.append(word1[min_len:])
        resultado.append(word2[min_len:])

        return ''.join(resultado)
