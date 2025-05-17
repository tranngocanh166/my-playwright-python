pipeline {
    agent any

    stages {
        stage('Setup Python & Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                python -m playwright install
                '''
            }
        }

        stage('Run Playwright Tests') {
            steps {
                sh '''
                source venv/bin/activate
                pytest my-playwright-python/tests
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/videos/**', allowEmptyArchive: true
            archiveArtifacts artifacts: '**/trace.zip', allowEmptyArchive: true
        }
    }
}
