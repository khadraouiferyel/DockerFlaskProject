
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
                bat 'dir MicroService1Flask'  
            }
        }

        stage('Build') {
            steps {
                // Construire les images Docker
                script{
                    bat 'docker-compose build'
                    }
                
            }
        }

        stage('Deployment') {
            steps {
                // Lancer les conteneurs
                bat 'docker-compose up -d'
            }
        }
        stage('Test') {
            steps {
                script {
                    bat 'cd MicroService1Flask'
                    bat 'python -m unittest test_predict.py'
                }
            }
        }

    }
}
