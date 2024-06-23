pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                script {
                    bat 'python -m pip install boto3'
                }
            }
        }
        stage('Run Local Code') {
            steps {
                script {
                    bat '''
                    python athena_query.py
                    '''
                }
            }
        }
    }
}