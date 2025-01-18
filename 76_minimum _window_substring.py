class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n  = len(s), len(t)

        if m < n:
            return ""
        
        # variaveis da solucao
        sol = [0, 0] # index da solucao atual, len
        found = 0
        min_sol_len = 2147483647 # inicializa o lenght minimo da solucao atual com o valor max de inteiro
        freq_t = {}
        window = {}
        sol_iterator = 0
        
        # Contando frequencia dos caracteres distintos em t
        for i in t:
            freq_t[i] = 1 + freq_t.get(i, 0)
                    
        for i in range(m):
            window[s[i]] = 1 + window.get(s[i], 0)
            if s[i] in freq_t and window[s[i]] <= freq_t[s[i]]:
                found += 1 
            
            # Verificando se achamos uma solucao
            if found == n and len(window) <= min_sol_len:
                print(window, found, "found")
                sol = [sol_iterator, i - sol_iterator + 1]
                min_sol_len = len(window)
                
            # Aplicando o Slide removendo caracteres da esquerda    
            if found == n:
                while found == n:
                    if i - sol_iterator + 1 < min_sol_len:
                        sol = [sol_iterator, i - sol_iterator + 1]
                    
                    window[s[sol_iterator]] -= 1
                    
                    if s[sol_iterator] in freq_t and window[s[sol_iterator]] < freq_t[s[sol_iterator]]:
                        found -= 1
                    sol_iterator += 1
        
        # print(sol)
        # print(s[sol[0]:sol[0] + sol[1]])
                
        if sol[1] < n:
            return ""
        else:
            return s[sol[0]:sol[0] + sol[1]]        
        

# s = 'AAADOBECODEBANC'
# t = 'AA'

# sol = Solution()
# asw = sol.minWindow(s, t)

# # print(asw)