pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'master', url: 'https://github.com/khadraouiferyel/DockerFlaskProject.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Assurez-vous que le fichier Dockerfile est dans le répertoire racine du projet
                    docker.build("svm_service:latest", "-f MicroService1Flask/Dockerfile .")

                }
            }
        }
        
        stage('Run Flask in Docker') {
            steps {
                script {
                    // Lancement du conteneur Docker avec un port mappé
                    docker.image("svm_service").run("-d -p 5001:5001")
                }
            }
        }
        
        stage('Test API') {
            steps {
                script {
                    // Ajouter les commandes pour tester l'API ici
                    // Ex: sh 'curl http://localhost:5001/test-endpoint'
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
