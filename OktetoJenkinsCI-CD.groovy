#!/usr/bin/env groovy

//Author: Carlos Alvarado
//Jenkins Pipeline to handle the Continuous Integration and Continuous Deployment in Okteto.
//As prerequisites, you should install the Custom tools plugin on Jenkins... 
//...get the okteto CLI and Kubectl and you need to get your Okteto Token as well, and save it on a Jenkins Credential


node {
    
    env.OKTETO_DIR = tool name: 'okteto', type: 'com.cloudbees.jenkins.plugins.customtools.CustomTool'
    env.HOME = "${WORKSPACE}"
    env.CONTAINER_IMAGE = 'registry.cloud.okteto.net/calvarado2004/django-personas'
    env.KUBECTL_DIR = tool name: 'kubectl', type: 'com.cloudbees.jenkins.plugins.customtools.CustomTool'
    env.GIT_PROJECT = 'https://github.com/calvarado2004/django-personas.git'
    
    stage ('Prepare Environment with Okteto ') {
        withCredentials([string(credentialsId: 'okteto-token', variable: 'SECRET')]) {
            cleanWs deleteDirs: true
            def output = sh returnStdout: true, script: '''
            ${OKTETO_DIR}/okteto login --token ${SECRET}
            ${OKTETO_DIR}/okteto namespace
            '''
            println output
        }
    }
    
    stage ('Download the source code from GitHub'){
            git url: "${GIT_PROJECT}"
    }
    
    stage ('Build and Push Image with Okteto'){
        withCredentials([string(credentialsId: 'okteto-token', variable: 'SECRET')]) {
            def output = sh returnStdout: true, script: '''${OKTETO_DIR}/okteto login --token ${SECRET}
            ${OKTETO_DIR}/okteto namespace
            cd ${HOME}/personas_django
            ${OKTETO_DIR}/okteto build -t ${CONTAINER_IMAGE}:${BUILD_TAG} .
            '''
            println output
        }
    }
    
    stage('Deploy the new image to okteto'){
        withCredentials([string(credentialsId: 'okteto-token', variable: 'SECRET')]) {
            def output = sh returnStdout: true, script: '''${OKTETO_DIR}/okteto login --token ${SECRET}
            cd ${HOME}/django-k8s
            ${OKTETO_DIR}/okteto namespace
            cat kubernetes.j2 | sed "s#{{ CONTAINER_IMAGE }}:{{ TAG_USED }}#${CONTAINER_IMAGE}:${BUILD_TAG}#g" > kubernetes.yaml
            ${KUBECTL_DIR}/kubectl apply -f kubernetes.yaml
            ${KUBECTL_DIR}/kubectl rollout status deployment.apps/personas-django-deployment
            '''
            println output
        }
    }
}