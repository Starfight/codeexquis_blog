Title: Migration de capteur Domoticz
Date: 2019-01-20 20:58
Slug: migration-capteur-domoticz
Author: Nicolas Drufin
category: domotique
Summary: Comment faire pour migrer ses données météo vers un nouveau capteur

Dernièrement Weather Underground a publié un communiqué indiquant que le support de son API allait prendre fin en janvier 2019. Le site officiel de Domoticz a donc indiqué une procédure pour passer à un autre fournisseur de données météorologiques : Forecast.io. 

## Créer de nouveaux capteurs

La [procédure d'intégration de Forecast.io](https://www.domoticz.com/wiki/Weather_forecast_from_forecast.io_in_Domoticz) est assez simple à suivre et se passe comme n'importe quel nouveau capteur. On veuillera à bien mettre une limite de 5 minutes pour chaque appel pour ne pas surcharger l'API et risquer le blocage du compte associé.

## Migrer les données des capteurs Weather Underground

Afin de ne pas perdre les données déjà collectée avec Weather Underground, j'ai préféré dupliquer les données en les associant à l'id du capteur de Forecast.io. Dans mon cas, l'index de mon ancien capteur est 8, tandis que celui de mon nouveau est 19. On peut retrouver ces informations sur la page *Dispositifs* de Domoticz. Ensuite pour éviter les périodes de recouvrement, je met également la date de migration de capteur dans la requête : pour moi ce sera le 24 novembre 2018. 

Voici la requête pour cette manipulation :
```
INSERT INTO Temperature_Calendar(DeviceRowID,Temp_Min,Temp_Max,Temp_Avg,Chill_Min,Chill_Max,Humidity,Barometer,DewPoint,SetPoint_Min,SetPoint_Max,SetPoint_Avg,Date)
SELECT 19,Temp_Min,Temp_Max,Temp_Avg,Chill_Min,Chill_Max,Humidity,Barometer,DewPoint,SetPoint_Min,SetPoint_Max,SetPoint_Avg,Date
FROM Temperature_Calendar
WHERE DeviceRowID = 8 AND Date < datetime('2018-11-24')
```

Pour l'appliquer, on se place tout simplement dans le répértoire d'installation de domoticz sur le Raspberry Pi en ligne de commande, on se connecte à la base avec la commande `sqlite domoticz.db` et on copie colle la commande ci-dessus.
