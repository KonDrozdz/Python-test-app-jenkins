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
                sh 'mvn -B test' 
                junit '**/target/surefire-reports/*.xml'
                
                
                sh '''
                    echo "### Zawartość target ###"
                    ls -laR target/
                    echo "### Raporty testowe ###"
                    ls -la target/surefire-reports/ || true
                '''
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh """
                        ${SONARQUBE_SCANNER}/bin/sonar-scanner \
                        -Dsonar.projectKey=simple-java-app \
                        -Dsonar.sources=src/main/java \
                        -Dsonar.host.url=http://sonarqube:9000 \
                        -Dsonar.login=${SONARQUBE_TOKEN}
                    """
                }
            }
        }

        stage('Quality Gate Check') {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
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
