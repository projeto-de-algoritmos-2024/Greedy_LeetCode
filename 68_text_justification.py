class Solution:
    def fullJustify(self, words, maxWidth: int):
        output_list = []
        current_line = []
        current_length = 0

        for word in words:
            current_word_size = len(word)
            if current_length + len(word) + len(current_line) > maxWidth:
                # Formata linha atual
                spaces = maxWidth - current_length
                if len(current_line) == 1:
                    output_list.append(current_line[0] + ' ' * spaces) # Justificando a esquerda quando so tem uma palavra
                else:
                    spaces_between = spaces // (len(current_line) - 1)
                    extra_spaces = spaces % (len(current_line) - 1)

                    # Criando a linha atual com espaços
                    line = ''
                    for i in range(len(current_line) - 1):
                        line += current_line[i]
                        line += ' ' * (spaces_between + (1 if i < extra_spaces else 0))
                    line += current_line[-1] 
                    output_list.append(line)
                
                # Reseta as variaveis
                current_line = []
                current_length = 0

            current_line.append(word)
            current_length += len(word)

        last_line = ' '.join(current_line)
        last_line += ' ' * (maxWidth - len(last_line))
        output_list.append(last_line)

        return output_list

sol = Solution()

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

max_sum = sol.fullJustify(words, maxWidth)

print(max_sum)