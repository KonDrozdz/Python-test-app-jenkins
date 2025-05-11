pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/KonDrozdz/Python-test-app-jenkins.git'
            }
        }

        stage('Verify Structure') {
            steps {
                sh '''
                    echo "### Pełna struktura projektu ###"
                    find . -type f
                    echo "### Zawartość src/test ###"
                    ls -laR src/test/java/
                '''
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean compile'
            }
        }

        stage('Test') {
            steps {
                sh 'mvn -B test' // -B for batch mode
                junit '**/target/surefire-reports/*.xml'
                
                // Dodatkowa diagnostyka
                sh '''
                    echo "### Zawartość target ###"
                    ls -laR target/
                    echo "### Raporty testowe ###"
                    ls -la target/surefire-reports/ || true
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