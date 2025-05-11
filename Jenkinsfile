pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/KonDrozdz/Python-test-app-jenkins.git'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean compile'
            }
        }

        stage('Test') {
            steps {
                sh 'mvn test'
                junit '**/target/surefire-reports/*.xml'
                
                // Diagnostyka
                sh '''
                    echo "### Struktura po testach ###"
                    find . -name "*.java"
                    echo "### Raporty testowe ###"
                    ls -laR target/surefire-reports/
                '''
            }
        }

        stage('Package') {
            steps {
                sh 'mvn package'
                archiveArtifacts 'target/*.jar'
            }
        }
    }

    post {
        always {
            echo 'Pipeline zakończony'
        }
    }
}