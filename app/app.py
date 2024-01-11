from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configuration de la base de données
db_config = {
    'host': 'mysql_db',
    'user': 'root',
    'password': 'root',
    'database': 'projet_db',
}

# Fonction utilitaire pour établir une connexion à la base de données
def get_db():
    return mysql.connector.connect(**db_config)

# Route pour la liste des chaussures les plus chères
@app.route('/chaussures')
def chaussures_cheres():
    try:
        # Utilisez la fonction utilitaire pour obtenir une connexion à la base de données
        connection = get_db()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT nom, prix FROM chaussures ORDER BY prix DESC")
        chaussures = cursor.fetchall()

        # Ajoutez des logs pour déboguer
        print("Résultats:", chaussures)

        if not chaussures:
            print("Aucune chaussure trouvée dans la base de données.")
            return "Aucune chaussure trouvée dans la base de données."

        return render_template('chaussures.html', chaussures=chaussures)

    except Exception as e:
        # Affichez l'erreur détaillée
        print("Erreur MySQL:", e)
        return f"Erreur lors de l'exécution de la requête SQL: {e}"

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

# ...

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
