
pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Récupère le code source depuis le dépôt
                git branch: 'master', url: 'https://github.com/khadraouiferyel/DockerFlaskProject.git' 
            }
        }

        stage('Check Docker') {
            steps {
                script {
                    sh 'docker --version'
                    sh 'docker-compose --version'
                }
            }
        }

        stage('Debug') {
            steps {
                // Lister les fichiers pour vérifier le contenu du répertoire
                bat 'dir' // Windows
            }
        }

        stage('Build Services') {
            steps {
                // Construire les images Docker
                bat 'docker-compose build'
            }
        }

        stage('Run Services') {
            steps {
                // Lancer les conteneurs
                bat 'docker-compose up -d'
            }
        }

    }
}
