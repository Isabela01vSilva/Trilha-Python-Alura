from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Laranja', 5.00, 'Grande')
bebida_suco.aplicar_desconto()
prato_pao = Prato('Pão', 3.00, 'Pão Doce com creme')
prato_pao.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()