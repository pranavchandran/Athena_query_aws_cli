pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
    }

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
                    set AWS_ACCESS_KEY_ID=%AWS_ACCESS_KEY_ID%
                    set AWS_SECRET_ACCESS_KEY=%AWS_SECRET_ACCESS_KEY%
                    python athena_query.py
                    '''
                }
            }
        }
    }
}