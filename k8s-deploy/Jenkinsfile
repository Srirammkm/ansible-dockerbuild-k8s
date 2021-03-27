pipeline {
  environment {
  IBM_CLOUD_REGION = 'us-south'
  IKS_CLUSTER = 'c0uvrhfd0v1b3bd432lg'
  registry = "srirammk18/py-db"
  registryCredential = 'dockerhub_id'
  dockerImage = ''
  }
  agent any 
  stages {
    stage('Build with Docker') {
      steps {
        script {
        dockerImage = docker.build registry + ":final"
        }
      }
    }
    stage('Push the image to ICR') {
      steps {
        script {
          docker.withRegistry( '', registryCredential ) {
          dockerImage.push()
          }
        }
      }
    }
    stage('Authenticate with IBM Cloud CLI') {
      steps {
        sh '''
            ibmcloud login --apikey ${IBM_API_KEY} -r "${IBM_CLOUD_REGION}" -g Default
            ibmcloud ks cluster config --cluster ${IKS_CLUSTER}
            '''
      }
    }
    stage('Deploy to IKS') {
      steps {
        sh '''
            ibmcloud ks cluster config --cluster ${IKS_CLUSTER}
            kubectl config current-context
            kubectl apply -f service.yml
            kubectl apply -f ingress.yml
            kubectl apply -f db-deploy.yml
            kubectl apply -f db-service.yml
            kubectl apply -f persistentvolume.yml
            kubectl apply -f pvc.yml
            kubectl apply -f py-service.yml
            kubectl apply -f deployment.yml
            '''
      }
    }
  }
}
