"""

frase = ('Curso em video Python')
frase tem 21 caracteres (bloco 0 até o bloco 20)
len(frase) = mostra o comprimento da frase (qtd caracteres)
frase.count('o') = conta a quantidades da letra o na frase.
frase.find('deo') = diz em que posição começa e termina (inicio, bloco final -1)
'Curso' in frase = procura a palavra 'curso' na frase, retorna com True or False
frase.replace('Python', 'Android') = muda a palavra Python por Android na frase.
frase.replace(' ', '')


frase.upper() = transforma tudo em maiúsculo
frase.lower() = transforma tudo em minúsculo
frase.title() = transforma a primeira letra de cada palavra em maiúsculo (o resto da palavra fica em minusculo) (ex: Curso Em Video Python)
frase.capitalize() = Deixa só o primeiro caractere maísculo e o resto minúsuclo (ex: Curso em video Python)
frase.strip() = remove espaços excedentes no início e do fim da frase
frase.rstrip() = remove todos espaços excedentes na direita (right) da frase (final da frase)
frase.lstrip() = remove todos espaços excedentes na esquerda (left) da frase

frase.split() = divide a frase (string) seguindo o padrão dos espaços entre as palavras
ex = split('Curso em video') = ('Curso') ('em') ('video')

'-',join(frase)
ex = ('Curso-em-video')

"""

frase = 'Curso em Video Python'
dividido = (frase.split())
print(dividido[2][3])

#print(frase.replace('Python', 'Android'))
