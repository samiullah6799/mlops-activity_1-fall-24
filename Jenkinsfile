pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/dev']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/samiullah6799/mlops-activity_1-fall-24.git']])
            }
        }
        stage('Installation') {
            steps {
              echo "Installation"
            }
      }

      stage('Testing') {
            steps {
              echo "Testing"
            }
      }

      stage('Deployment') {
            steps {
              echo "Deployment"
            }
      }
    }
}
