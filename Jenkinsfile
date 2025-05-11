pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'mvn clean compile'
            }
        }

        stage('Test') {
            steps {
                sh 'mvn test'
                junit '**/target/surefire-reports/*.xml'
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
