import numpy as np
import os
from parseTrackletXML import parseXML


# 3. Boucler sur chaque fichier (chaque frame de ta simulation)
for index_frame, nom_fichier in enumerate(fichiers_bin):
    
    # Construire le chemin complet du fichier .bin actuel
    chemin_complet = os.path.join(dossier_velodyne, nom_fichier)
    
    # 4. Charger les données binaires du LiDAR
    # Dans KITTI, chaque point est stocké sur 4 floats (X, Y, Z, Réflectance)
    donnees_brutes = np.fromfile(chemin_complet, dtype=np.float32)
    
    # Redimensionner le tableau pour avoir une ligne par point (4 colonnes)
    nuage_points = donnees_brutes.reshape(-1, 4)
    
    # 5. Isoler uniquement les coordonnées spatiales X, Y, Z
    points_xyz = nuage_points[:, :3]


# Charger toutes les boîtes de la séquence
tracklets = parseXML('C:\\Users\\bozz1\\OneDrive\\Documents\\ENSISA\\2A\\Projet Détection d’éléments dynamiques dans les mesures LiDAR 3D\\data\\2011_09_26\\2011_09_26_drive_0002_sync\\tracklet_labels.xml')

for tracklet in tracklets:
    objet_type = tracklet.objectType  # 'Car', 'Pedestrian'...
    h, w, l = tracklet.size           # Dimensions de la boîte
    
    # Parcourir les frames où cet objet est visible
    first_frame = tracklet.firstFrame
    for i, translation in enumerate(tracklet.trans):
        frame_actuelle = first_frame + i
        x, y, z = translation
        roll, pitch, yaw = tracklet.rots[i]
        
        # Ici, tu as toutes les coordonnées pour créer ta boîte 3D 
        # et tester si tes points LiDAR sont dedans à la 'frame_actuelle' !
    
    
    
        
# =====================================================================
# 1. CONFIGURATION DES CHEMINS (À MODIFIER AVEC TES DOSSIERS)
# =====================================================================

# 1. Chemin vers ton dossier contenant les fichiers .bin
# (Remplace par ton vrai chemin absolu ou relatif)
DOSSIER_VELODYNE = "C:\\Users\\bozz1\\OneDrive\\Documents\\ENSISA\\2A\\Projet Détection d’éléments dynamiques dans les mesures LiDAR 3D\\data\\2011_09_26\\2011_09_26_drive_0002_sync\\velodyne_points\\data"
FICHIER_XML = "C:\\Users\\bozz1\\OneDrive\\Documents\\ENSISA\\2A\\Projet Détection d’éléments dynamiques dans les mesures LiDAR 3D\\data\\2011_09_26\\2011_09_26_drive_0002_sync\\tracklet_labels.xml"


# =====================================================================
# 2. CHARGEMENT ET TRI DES FICHIERS LIDAR (.BIN)
# =====================================================================
# On liste et on trie par ordre alphabétique pour respecter la chronologie
fichiers_bin = sorted([f for f in os.listdir(DOSSIER_VELODYNE) if f.endswith('.bin')])
print(f"[{len(fichiers_bin)} fichiers .bin trouvés dans le dossier]")

# =====================================================================
# 3. BOUCLE PRINCIPALE : TRAITEMENT FRAME PAR FRAME
# =====================================================================
for index_frame, nom_fichier in enumerate(fichiers_bin):
    
    # Construction du chemin vers le fichier .bin actuel
    chemin_complet_bin = os.path.join(DOSSIER_VELODYNE, nom_fichier)
    
    # Lecture globale du fichier binaire (liste plate de float32)
    donnees_brutes = np.fromfile(chemin_complet_bin, dtype=np.float32)
    
    # Rangement par colonnes de 4 (X, Y, Z, Réflectance)
    nuage_points = donnees_brutes.reshape(-1, 4)
    
    # Extraction des coordonnées spatiales uniquement (X, Y, Z)
    points_xyz = nuage_points[:, :3]
    
    # Création d'un tableau de labels de la même taille, rempli de 0 par défaut
    # 0 = Sol / Vide, 1 = Voiture, 2 = Piéton, etc.
    labels_points = np.zeros(len(points_xyz), dtype=np.int32)
    
    print(f"--- Frame {index_frame} ({nom_fichier}) : {len(points_xyz)} points chargés ---")

    # =================================================================
    # TODO: ÉTAPE PROCHAINE - EXTRACTION ET INJECTION DES BOÎTES XML
    # =================================================================
    # C'est ici que ton code ira chercher dans le XML les boîtes actives 
    # à cette 'index_frame' spécifique pour modifier 'labels_points'.
    # =================================================================
    
    # Exemple pour voir que le script tourne (on affiche juste les 5 premiers points)
    # print("Exemple de points (X, Y, Z) :", points_xyz[:5])
    
    # Pour tester ton script au début sans bloquer ton PC, tu peux enlever le dièse ci-dessous
    # break        