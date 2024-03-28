from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Guinga', 10)
restaurante_praca.receber_avaliacao('Duda', 8)
restaurante_praca.receber_avaliacao('Anna', 4)
restaurante_sushi = Restaurante('Sushi', 'Japones')

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()