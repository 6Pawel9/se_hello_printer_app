pipeline {
    agent any
    stages {
        stage('Deps') {
            steps {
	            sh 'make deps'
        	}
        }
    stages {
        stage('Test') {
            steps {
	            sh 'make test'
        	}
        }
    }
}
