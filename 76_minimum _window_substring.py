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
        
        # print(freq_t)
                    
        for i in range(m):
            window[s[i]] = 1 + window.get(s[i], 0)
            if s[i] in freq_t and window[s[i]] <= freq_t[s[i]]:
                found += 1 
            
            # Verificando se achamos uma solucao
            if found >= n and i+1 <= min_sol_len:
                # print(window, found, "found")
                sol = [sol_iterator, i - sol_iterator + 1]
                min_sol_len = i + 1
                
            # Aplicando o Slide removendo caracteres da esquerda    
            # print("found: ", found, "   n: ", n, window)
            # print('sol ', sol)

            while found == n:
                # print('got here, i equals ', i, 'and min_sol_len ', min_sol_len)
                if i - sol_iterator + 1 < min_sol_len:
                    sol = [sol_iterator, i - sol_iterator + 1]
                    min_sol_len = sol[1]
                
                window[s[sol_iterator]] -= 1
                
                if s[sol_iterator] in freq_t and window[s[sol_iterator]] < freq_t[s[sol_iterator]]:
                    found -= 1
                sol_iterator += 1
            # print("window",window)
            # print("found: ", found, "   n: ", n)
        
        # print(sol)
        # print(s[sol[0]:sol[0] + sol[1]])
                
        if sol[1] < n:
            return ""
        else:
            return s[sol[0]:sol[0] + sol[1]]        
        

# s = 'aa'
# t = 'aa'

# sol = Solution()
# asw = sol.minWindow(s, t)

# print(asw)