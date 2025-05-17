pipeline {
    agent any
 
    environment {
        VENV_DIR = 'venv'
    }
 
    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/tranngocanh166/my-playwright-python.git'
            }
        }
 
        stage('Create Virtual Env') {
            steps {
                bat 'python -m venv %VENV_DIR%'
            }
        }
 
        stage('Install Dependencies') {
            steps {
                bat '''
                    call %VENV_DIR%\\Scripts\\activate.bat
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    playwright install
                '''
            }
        }
 
        stage('Run Tests') {
            steps {
                bat '''
                    call %VENV_DIR%\\Scripts\\activate.bat
                    pytest tests/ --headed
                '''
            }
        }
    }
 
    post {
        success {
            echo "✅ Playwright tests completed successfully!"
        }
        failure {
            echo "❌ Playwright tests failed!"
        }
    }
}