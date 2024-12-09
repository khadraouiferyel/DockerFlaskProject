
pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Récupère le code source depuis le dépôt
                git branch: 'main', url: 'https://github.com/khadraouiferyel/DockerFlaskProject.git' 
            }
        }

        stage('Debug') {
            steps {
                bat 'dir MicroService1Flask'  // Verify the files in the MicroService1Flask directory
            }
        }

        stage('Build Services') {
            steps {
                // Construire les images Docker
                script{
                    bat 'docker-compose build'
                    }
                
            }
        }

        stage('Run Services') {
            steps {
                // Lancer les conteneurs
                bat 'docker-compose up'
            }
        }

    }
}
