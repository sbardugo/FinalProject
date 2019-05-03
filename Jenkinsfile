pipeline {
    agent any 
    stages {
        stage('git pull') { 
            steps {
	 echo 'git pull to c:finalproject'
	 bat 'git pull https://github.com/sbardugo/FinalProject.git '
            }}
        stage('docker-compose up') { 
            steps {
	 bat 'docker-machine start default'
	 sleep (time:1, unit:"MINUTES") 
	 bat 'docker-compose -f docker-compose.yml up -d'
	 sleep (time:1, unit:"MINUTES") 
            }}
            stage('testapp') { 
            steps {
	 bat 'python finalproject//TestScript.py'
            }}
             stage('testappwitouhtworld') { 
            steps {
	 bat 'python finalproject//testwithoutword.py'      
    }}
    }
post {
        success {
            emailext body: 'pipeline final project success',attachLog: true, subject: 'pipeline final project success', to: 'shiranbardugo@gmail.com'
        }
	aborted {
            emailext body: 'pipeline final project aborted',attachLog: true, subject: 'pipeline final project aborted', to: 'shiranbardugo@gmail.com'
        }
	failure {
            emailext body: 'pipeline final project failure',attachLog: true, subject: 'pipeline final project failure', to: 'shiranbardugo@gmail.com'
        }
    }
}
