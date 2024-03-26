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

print(f'Música: {musica1.nome} - Cantor: {musica1.artista} - {musica1.duracao} segundos')
print(f'Música: {musica2.nome} - Banda: {musica2.artista} - {musica2.duracao} segundos')
print(f'Música: {musica3.nome} - Cantora: {musica3.artista} - {musica3.duracao} segundos')