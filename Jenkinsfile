pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/darkknightraj/sshgit.git',
                credentialsId: 'github-pat'  // Your GitHub credentials ID
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Stop/remove old container if running
                    sh 'docker stop myapp || true'
                    sh 'docker rm myapp || true'
                    
                    // Build new image
                    sh 'docker build -t my-python-app:1 .'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    // Run with restart policy (auto-recover on crashes)
                    sh 'docker run -d --restart unless-stopped -p 4000:80 --name myapp my-python-app:1'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Optional: Add cleanup steps if needed
        }
    }
}
