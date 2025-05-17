pipeline {
    agent any
 
    environment {
        VENV_DIR = 'venv'
    }
 
    stages {
        stage('Clone Source Code') {
            steps {
                git 'https://github.com/tranngocanh166/my-playwright-python.git'
            }
        }
 
        stage('Setup Python venv') {
            steps {
                bat 'python -m venv %VENV_DIR%'
                bat '%VENV_DIR%\\Scripts\\activate && pip install --upgrade pip'
            }
        }
 
        stage('Install Dependencies') {
            steps {
                bat '%VENV_DIR%\\Scripts\\activate && pip install -r requirements.txt'
                bat '%VENV_DIR%\\Scripts\\activate && playwright install'
            }
        }
 
        stage('Run Playwright Tests') {
            steps {
                bat '%VENV_DIR%\\Scripts\\activate && pytest tests/ --headed'
            }
        }
    }
 
    post {
        always {
            echo "🎯 Build finished."
        }
        success {
            echo "✅ Tests ran successfully."
        }
        failure {
            echo "❌ Test run failed."
        }
    }
}