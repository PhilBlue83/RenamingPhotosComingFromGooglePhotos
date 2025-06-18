#
#
# Auteur : Philippe B
# Date : 07 Fev 2025
# Version V2
# 
# Le script doit etre place dans le meme repertoire contenant les fichiers photos/videos et fichiers json
#
# Objet:
# Renommage des fichiers photos et videos (rapatries depuis Google Photos)
# en inserrant dans le nom du fichier les informations extraites du fichier associe (supplemental-metadata.json)
#     Date (Annee Mois Jour Heure Minutes Secondes),
#     Position Geo (lat, Long,alt)
#        Si les informations Geo sont indisponibles dans le json, la mention NoGeo sera inserree
#
# Renaming photo and video files (retrieved from Google Photos)
# by inserting the information extracted from the associated file (supplemental-metadata.json) into the file name
# Date (Year, Month, Day, Hour, Minutes, Seconds),
# Geo Position (lat, Long, alt)
# If the Geo information is unavailable in the json, the NoGeo label will be inserted
#
#

import os
import shutil
import json
from datetime import datetime
import time


obj = os.scandir('.')

for entry in obj:
    if entry.is_file():
        print("fichier lu : ",entry.name)
        OptionFichier = (str(entry.name))[-13:]
        # print("OptionFichier : ", OptionFichier)
        if OptionFichier == "metadata.json":
            PosMarqueur = (str(entry.name)).find(".supplemental-metadata")
            # print("PosMarqueur : ",PosMarqueur)
            ExtractNomFichier = (str(entry.name))[0:PosMarqueur]
            print("ExtractNomFichier : ",ExtractNomFichier)
            
            with open(entry.name, 'r') as file:
                data = json.load(file)
            
                lat = data['geoDataExif']['latitude']
                long = data['geoDataExif']['longitude']
                alt = int(data['geoDataExif']['altitude'])

                filetimestamp = int(data['photoTakenTime']['timestamp'])
            
            file.close()

            date_object = datetime.fromtimestamp(filetimestamp)
            #print("date_object : ",date_object)
            
            
            Extract_Annee =  (str(date_object))[0:4]
            Extract_Mois =  (str(date_object))[5:7]
            Extract_Jour =  (str(date_object))[8:10]
            Extract_heure = (str(date_object))[11:13] + (str(date_object))[14:16] + (str(date_object))[17:19]
            Date_extract = Extract_Annee + Extract_Mois + Extract_Jour + "_" + Extract_heure
            #print("Date_extract : ",Date_extract)
            
            Pos_Geo = str(lat) + "_" + str(long) + "_" + str(alt)
            if Pos_Geo == "0.0_0.0_0":
                Pos_Geo = "NoGeo"
            
            nom_fichier_modifie = Date_extract + "_" + Pos_Geo + "__" + ExtractNomFichier
            print("nom_fichier_modifie : ",nom_fichier_modifie)
            
            # os.rename(ExtractNomFichier,nom_fichier_modifie)
            shutil.copyfile(ExtractNomFichier,nom_fichier_modifie)
 
