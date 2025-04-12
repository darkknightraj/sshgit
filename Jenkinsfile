pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/darkknightraj/sshgit.git',
                credentialsId: 'github-pat'
            }
        }
        
        stage('Build') {
            steps {
                script {
                    docker.build("my-python-app:${env.BUILD_ID}")
                }
            }
        }
        
        stage('Run') {
            steps {
                script {
                    docker.image("my-python-app:${env.BUILD_ID}").run('--rm -d -p 4000:80 --name myapp')
                }
            }
        }
    }
}
