pipeline {
  agent any
  stages {
    stage('Build-Image') {
      steps {
        sh 'docker build -t srirammk18/mysql .'
      }
    }
      stage ('Push-Image') {
        steps {
        withDockerRegistry([ credentialsId: "dockerhub_id", url: "" ]) {
          sh 'docker push srirammk18/mysql'
        }
      }
    }
  }
}
