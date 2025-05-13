pipeline {
  agent any

  environment {
    VENV_DIR = 'venv'
  }

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/tranngocanh166/my-playwright-python.git'
      }
    }

    stage('Set up Virtual Environment') {
      steps {
        sh 'python -m venv $VENV_DIR'
        sh '. $VENV_DIR/bin/activate && pip install --upgrade pip && pip install -r requirements.txt'
        sh '. $VENV_DIR/bin/activate && playwright install'
      }
    }

    stage('Run Playwright Tests') {
      steps {
        sh '. $VENV_DIR/bin/activate && pytest tests/ --headed --tracing=retain-on-failure --video=on'
      }
    }

    stage('Archive Traces and Videos') {
      steps {
        archiveArtifacts artifacts: '**/test-results/**/*.*', allowEmptyArchive: true
      }
    }
  }
}
