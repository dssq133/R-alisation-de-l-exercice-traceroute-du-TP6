import argparse
import subprocess
import sys


def traceroute(destination, progressive=False, output_file=None):
    """Effectue un traceroute avec ou sans affichage progressif et possibilité de sauvegarde dans un fichier."""
    try:
        # Utilisation de tracert sur Windows, traceroute sur Linux/Mac
        command = ["tracert", destination] if sys.platform == "win32" else ["traceroute", destination]

        if progressive:
            # Affichage progressif au fur et à mesure
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            for line in iter(process.stdout.readline, ""):
                print(line.strip())  # Afficher ligne par ligne
            process.wait()
        else:
            # Exécution complète du traceroute
            process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output = process.stdout
            print(output)

            # Si un fichier est spécifié, sauvegarder le résultat
            if output_file:
                with open(output_file, 'w') as f:
                    f.write(output)
                    print(f"Résultat sauvegardé dans {output_file}")

    except Exception as e:
        print(f"Une erreur est survenue : {e}")


def main():
    # Gestion des arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Script Python pour effectuer un traceroute.")
    parser.add_argument("destination", help="URL ou adresse IP cible pour effectuer le traceroute.")
    parser.add_argument("-p", "--progressive", action="store_true", help="Affichage progressif des résultats.")
    parser.add_argument("-o", "--output-file", type=str, help="Nom du fichier où enregistrer les résultats.")
    args = parser.parse_args()

    # Appel de la fonction traceroute avec les arguments appropriés
    traceroute(destination=args.destination, progressive=args.progressive, output_file=args.output_file)


if __name__ == "__main__":
    main()
