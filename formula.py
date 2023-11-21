# Trabalho: definição de horários de cursos em um evento
# Objetivo: fazer um programa que diga se é possível agendar os cursos na quantidade de slots disponíveis e, se possível,
# dizer em que horário devem ser alocados.

# Número de cursos: k
# Número de slots de tempo: m; 
# conjunto P: pares de cursos com inscrições em comum.
# Participantes podem se inscrever em mais de um curso, mas não no mesmo horário

#Restrições:
#1. Cada minicurso deve ser ofertado em pelo menos um slot.
#2. Cada minicurso deve ser ofertado em no máximo um slot.
#3. Minicursos com inscrições em comum não podem ser ofertados no mesmo slot.
#Entrada:

# Minicursos:
#1 HTML
#2 PHP
#3 MySQL
#4 Swift
# Slots: 3
# Pares de minicursos com inscrições em comum:
#1 2
#2 3
#2 4
#3 4
#Saída:
#1 s1
#2 s3
#3 s1
#4 s2
