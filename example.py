#!/usr/bin/python
# -*- coding: utf-8 -*-

from cobregratis.bank_billet import BankBillet
from pyactiveresource.connection import UnauthorizedAccess
import sys

def main():
  BankBillet.user = 'token encontrado no perfil do usuário'
  BankBillet.password = 'X'
  try:
    # Criando um boleto
    amount = 230.50
    expire_at = '2015-07-22'
    name = 'Rafael Lima'
    bank_billet = BankBillet.create({'amount':amount,'expire_at':expire_at,'name':name})
    print bank_billet.external_link
    
    # Buscando informações sobre um boleto passando seu ID
    bank_billet = BankBillet.find(1)
    print bank_billet.external_link

    # Listando uma série de boletos
    bank_billets = BankBillet.find()
    if not bank_billets:
      print "Nenhum boleto bancário"
    else:
      for bank_billet in bank_billets:
        print "Nosso Número: %s" % bank_billet.our_number
        print "Vencimento: %s" % bank_billet.expire_at
        print "Valor: %s" % bank_billet.amount
        print "Sacado: %s" % bank_billet.name
        print "URL: %s" % bank_billet.external_link
        print "================================="
  except UnauthorizedAccess:
    print "Access Denied"

if __name__ == '__main__':
  main()