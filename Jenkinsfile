pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'svm_service'
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/khadraouiferyel/DockerFlaskProject.git'  // Remplace avec l'URL de ton dépôt
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    // Construire l'image Docker à partir du Dockerfile
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Run Flask in Docker') {
            steps {
                script {
                    // Lancer le container avec l'application Flask
                    docker.run("${DOCKER_IMAGE}:${DOCKER_TAG}", '-p 5001:5001')
                }
            }
        }

        stage('Test API') {
            steps {
                // Tester l'API (par exemple avec curl ou un autre outil)
                script {
                    sh 'curl -X POST http://localhost:5001/predict -d "{ \"audio_data\": \"<base64_encoded_audio_data>\" }"'
                }
            }
        }
        
        stage('Cleanup') {
            steps {
                script {
                    // Nettoyer les conteneurs après le test
                    sh 'docker container prune -f'
                }
            }
        }
    }

    post {
        always {
            cleanWs()  // Nettoyer l'espace de travail après l'exécution
        }
    }
}
