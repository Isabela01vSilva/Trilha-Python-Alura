class Music:
    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Music.musicas.append(self)
        
    def listar_musicas():
        for musica in Music.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

musica1 = Music('Please dont change', 'Jung ook', '2:30')
musica2 = Music('Bohemian Rhapsody', 'Queen', '3:55')
musica3 = Music('Training season', 'Dua Lipa', '3:29')

Music.listar_musicas()