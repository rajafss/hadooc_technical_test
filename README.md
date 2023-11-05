# hadooc_technical_test


test technique:

1.create file .py: hériter le modèle "account.payment" : pour créer une relation many2one avec 'sale.order'

2.create file .py: hériter le modèle "sale.order": créer une relation one2many avec 'account.payment'

3.créez le bouton de make_payment pour créer des valeurs de paiement et vérifier le montant valide s'il est inferieur ou egal au total_amount de la vente
    - création wizard

4.create file xml: hériter form view du model "sale.order" 
  - créer un bouton Register Payment pour pour ajouter un payment
  - créer une page de paiement pour lister les paiements en utilisant le champ one2many
  - créer deux compute field pour générer le total_payment and remaining amount

5.créer le rapport pdf du reçu
    création  action reports: sale_payment_report_action
    création template reports
6.créer le bouton action print pour imprimer le rapport de réception pdf dans account.payment model
