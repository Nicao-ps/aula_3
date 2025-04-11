# **Exercício 01**

print('')
print('**********************************************************************')
print('')
print('Dia de desconto na loja! 13% OFF em qualquer camiseta adquirida!')
print('')
print('**********************************************************************')
print('')

discont = 0.13
value_item = float(input('Informe o preço de sua peça: '))
value_discont = discont * value_item
value_new = value_item - value_discont

print('')
print('')
print('----------------------------------------------------------------------')
print('')
print('Preço original da peça:', 'R$ '+'{:.2f}'.format(value_item))
print('')
print('Desconto aplicado na compra:', 'R$ '+'{:.2f}'.format((value_discont)))
print('')
print('Preço final da peça:', 'R$ '+'{:.2f}'.format((value_new)))
print('')
print('----------------------------------------------------------------------')
print('')
