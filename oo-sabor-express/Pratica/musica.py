class Music:
    nome = ''
    artista = ''
    duracao = ''

musica1 = Music()
musica1.nome = 'Please don´t change'
musica1.artista = 'Jung ook'
musica1.duracao = '2:30'

musica2 = Music()
musica2.nome = 'Bohemian Rhapsody'
musica2.artista = 'Queen'
musica2.duracao = '3:55'

musica3 = Music()
musica3.nome = 'Training season'
musica3.artista = 'Dua Lipa'
musica3.duracao = '3:29'

print(vars(musica1))
print(vars(musica2))
print(vars(musica3))