# Système de Notification des Prix d'Actions et Actualités

## Présentation
Ce script surveille les fluctuations des prix des actions et envoie des alertes par e-mail lorsqu'il y a une variation significative. Il utilise l'API Alpha Vantage pour obtenir les données sur les prix des actions de la société Tesla Inc (TSLA) et l'API News pour récupérer les actualités liées à Tesla Inc. Lorsque le prix des actions de Tesla varie de plus de 3% par rapport à la journée précédente, le script envoie un e-mail contenant les trois premiers articles d'actualité sur Tesla.

## Fichiers
- main.py : Ce fichier contient la logique principale du système de notification des prix d'actions et des actualités. Il interroge l'API Alpha Vantage pour obtenir les données sur les prix des actions, vérifie les variations de prix et envoie des e-mails contenant des actualités si une variation significative est détectée.
- .env : Ce fichier stocke des informations sensibles telles que les clés API, l'adresse e-mail de l'utilisateur, et le mot de passe de l'e-mail en tant que variables d'environnement.

## Exécution
Pour exécuter le système de notification des prix d'actions et des actualités :
- Assurez-vous que Python et les bibliothèques requises répertoriées dans requirements.txt sont installés.
- Configurez les variables d'environnement dans le fichier .env, y compris les clés API Alpha Vantage et News, l'adresse e-mail de l'utilisateur, ainsi que le mot de passe de l'e-mail.
- Lancez le fichier main.py. Le programme récupère les données sur les prix des actions, analyse les variations et envoie des e-mails d'actualités si une variation significative est détectée.

## Installation et Configuration
- Python : Version 3.9.6
- Bibliothèques Python :
    - requests
    - smtplib
- API Alpha Vantage : Obtenez une clé API auprès d'Alpha Vantage et définissez-la comme valeur pour ALPHAVANTAGE_API_KEY dans le fichier .env.
    - ℹ️ IMPORTANT ℹ️ : le endpoint visé de l'API Alpha Vantage est désormais premium et nécessite de souscrire à un plan premium.
- API News : Obtenez une clé API auprès de News API et définissez-la comme valeur pour NEWS_API_KEY dans le fichier .env.
- Adresse E-mail : Définissez votre adresse e-mail dans la variable MY_EMAIL dans le fichier main.py.
- Mot de Passe E-mail : Définissez le mot de passe de votre adresse e-mail dans la variable MY_PASSWORD dans le fichier .env.
- Adresse de Test E-mail : Définissez une adresse e-mail de test dans la variable EMAIL_TEST dans le fichier .env.
- Personnalisez la logique dans main.py pour ajuster les seuils de notification ou ajouter des fonctionnalités supplémentaires selon vos besoins.

## Remarques
Ce projet a été réalisé dans le cadre du cours [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/) de Angela Yu sur la plateforme Udemy.
