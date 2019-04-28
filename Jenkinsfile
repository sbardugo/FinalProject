pipeline {
    agent any 
    stages {
        stage('1') { 
            steps {
	 echo 'git clone to c:finalproject'
	 bat 'git clone https://github.com/sbardugo/FinalProject.git '
            }}
        stage('docker-compose up') { 
            steps {
	 bat 'docker-machine start default'
	 sleep (time:1, unit:"MINUTES") 
	 bat 'docker-compose -f finalproject//docker-compose.yml up -d'
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
        always {
            emailext body: 'pipeline final project test',attachLog: true, subject: 'pipeline final project test', to: 'shiranbardugo@gmail.com'
        }
    }
}
