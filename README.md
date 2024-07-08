# Data-Pipeline-for-Spotify-data-analysis

This project implements an ETL (Extract, Transform, Load) pipeline using Apache Kafka, AWS S3, AWS Glue, and AWS Athena.

## Repository structure

The repository is structured as follows:
### Folders
- albums/**: Contains album data and scripts for the Kafka producer and consumer.
- artist/**: Contains artist data and scripts for Kafka producer and consumer.
- tracks/**: Contains track data and scripts for Kafka producer and consumer.


### Scripts
- **producer.py**: Script for producing Kafka messages from CSV files.
- **consumer.py**: Script to consume Kafka messages and store them in an S3 bucket.

### Instances EC2
1. **Launch EC2 Instances**:
   - Create EC2 instances on AWS to host Kafka producers and consumers.
   - Configure the instances to access Kafka and S3 buckets.
2. **Connect to EC2 Instances**:
   - Connect to your EC2 instances via SSH.
   - Install the necessary dependencies (Kafka, Python, boto3, etc.).
3. **Execute Scripts on EC2**:
   - On each EC2 instance, run the producer and consumer scripts to send and receive Kafka messages.

### Kafka with upstash
1. **Configuring Kafka with upstash** :
   - Set up and start a Kafka cluster on upstash.com.
   - Create the corresponding topics on the cluster.
   - Make sure Kafka is accessible from your EC2 instances.
2. **Run Producers**:
   - Run the producer scripts on the EC2 instances to send messages to the respective topics.
3. **Run Consumers**:
   - Run the consumer scripts on EC2 instances to receive and process messages in the respective topics.
     

### AWS Glue
1. **Configure IAM Roles**:
   - Configure IAM roles to enable AWS Glue to access S3 buckets.
2. **Create and Run Glue Jobs**:
   - Create and run Glue jobs to transform and load data into a datalake.

### AWS Athena
1. **Crawler configuration**:
   - Configure a Glue crawler to detect patterns in the datalake.
2. **Query Data with Athena**:
   - Use Athena to query the data stored in the datalake.

### ETL process
1. **Kafka producers**: Read data from CSV files and publish messages in corresponding Kafka topics (`albums`, `artist`, `tracks`).
2. **Kafka Consumers**: Listen to messages in Kafka topics, transform them into DataFrame, and load them into CSV files in an S3 bucket.
3. **AWS Glue**: Used to create an ETL pipeline that transforms and loads data from the S3 staging bucket into the Data Lake.
4. **AWS Athena**: Used to query data from the Data Lake.

### Execution
1. Run the producers to publish the messages in Kafka.
2. Run consumers to consume messages from Kafka and store them in S3.
3. Configure AWS Glue to transform and load data into the Data Lake.
4. Use AWS Athena to query the data in the Data Lake.

## Installation
1. Clone the :
    ``bash
    https://github.com/Gastunechi/Data-Pipeline-for-Spotify-data-analysis.git
    ```
2. Install required dependencies (e.g. Kafka, Boto3, etc.)

## Usage
1. Configure Kafka producers and consumers.
2. Set up the necessary IAM roles and S3 buckets.
3. Configure and run AWS Glue jobs.
4. Use AWS Athena to run SQL queries on the transformed data.

Contributions are welcome! Please submit a pull request or open an issue to discuss what you'd like to change.

# Data Pipeline pour l'analyse de données Spotify

Ce projet implémente un pipeline ETL (Extract, Transform, Load) en utilisant Apache Kafka, AWS S3, AWS Glue, et AWS Athena.

## Structure du Repository

Le repository est structuré de la manière suivante :
### Dossiers
- **albums/**: Contient les données des albums et les scripts pour le producteur et le consommateur Kafka.
- **artist/**: Contient les données des artistes et les scripts pour le producteur et le consommateur Kafka.
- **tracks/**: Contient les données des pistes (tracks) et les scripts pour le producteur et le consommateur Kafka.


### Scripts
- **producer.py**: Script pour produire les messages Kafka à partir des fichiers CSV.
- **consumer.py**: Script pour consommer les messages Kafka et les stocker dans un bucket S3.


### Instances EC2
1. **Lancement des Instances EC2** :
   - Créez des instances EC2 sur AWS pour héberger les producteurs et consommateurs Kafka.
   - Configurez les instances pour qu'elles puissent accéder à Kafka et aux buckets S3.
2. **Connexion aux Instances EC2** :
   - Connectez-vous à vos instances EC2 via SSH.
   - Installez les dépendances nécessaires (Kafka, Python, boto3, etc.).
3. **Exécution des Scripts sur EC2** :
   - Sur chaque instance EC2, exécutez les scripts producteurs et consommateurs pour envoyer et recevoir des messages Kafka.

### Kafka avec upstash
1. **Configuration de Kafka avec upstash** :
   - Configurer et démarrer un cluster Kafka sur upstash.com.
   - Créez les topics correspondant sur le cluster.
   - Assurez-vous que Kafka est accessible depuis vos instances EC2.
2. **Exécution des Producteurs** :
   - Exécutez les scripts producteurs sur les instances EC2 pour envoyer des messages dans les topics respectifs.
3. **Exécution des Consommateurs** :
   - Exécutez les scripts consommateurs sur les instances EC2 pour recevoir et traiter les messages des topics respectifs.
  

### AWS Glue
1. **Configuration des Rôles IAM** :
   - Configurer des rôles IAM pour permettre à AWS Glue d'accéder aux buckets S3.
2. **Création et Exécution de Jobs Glue** :
   - Créez et exécutez des jobs Glue pour transformer et charger les données dans un datalake.
     
### AWS Athena
1. **Configuration du Crawler** :
   - Configurez un crawler Glue pour détecter les schémas dans le datalake.
2. **Requête des Données avec Athena** :
   - Utilisez Athena pour interroger les données stockées dans le datalake.


### Processus ETL
1. **Producteurs Kafka**: Lisent les données des fichiers CSV et publient les messages dans les topics Kafka correspondants (`albums`, `artist`, `tracks`).
2. **Consommateurs Kafka**: Écoutent les messages des topics Kafka, les transforment en DataFrame, et les chargent dans des fichiers CSV dans un bucket S3.
3. **AWS Glue**: Utilisé pour créer un pipeline ETL qui transforme et charge les données du bucket S3 staging vers le Data Lake.
4. **AWS Athena**: Utilisé pour interroger les données du Data Lake.

### Exécution
1. Exécutez les producteurs pour publier les messages dans Kafka.
2. Exécutez les consommateurs pour consommer les messages de Kafka et les stocker dans S3.
3. Configurez AWS Glue pour transformer et charger les données dans le Data Lake.
4. Utilisez AWS Athena pour interroger les données du Data Lake.

## Installation
1. Clonez le référentiel :
    ```bash
    https://github.com/Gastunechi/Data-Pipeline-for-Spotify-data-analysis.git
    ```
2. Installez les dépendances requises (par exemple, Kafka, Boto3, etc.)


Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour discuter de ce que vous aimeriez changer.


