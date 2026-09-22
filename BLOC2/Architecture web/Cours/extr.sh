#!/bin/bash
# author : Berin

# Parcourt tous les fichiers .zip du dossier courant
counter=0
for zip_file in ./*.zip; do
    # Vérifie si le fichier existe pour éviter une erreur si aucun .zip n'est trouvé
    if [ -f "$zip_file" ]; then
        echo "Extraction de : $zip_file"
        
        # Extrait le contenu dans un dossier portant le nom de l'archive
        destination="${zip_file%.zip}"
        if unzip -q "$zip_file" -d "$destination"; then
            echo "Extraction réussie, suppression de $zip_file"
            rm "$zip_file"
			((counter++))
        else
            echo "Erreur lors de l'extraction de $zip_file. Le fichier n'a pas été supprimé."
        fi
    fi
done

echo -e "Opération terminée. Nombre de zip extrait : $counter"