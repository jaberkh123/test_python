pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/jaberkh123/test_python.git'
            }
        }

        stage('Create and Checkout Target Branch') {
            steps {
                // Check if target branch exists, if not create it
                script {
                    sh 'git branch '
                    def branches = sh(script: 'git branch ', returnStdout: true).trim()
                    if (!branches.contains("target")) {
                        sh 'git checkout -b target' // Create new branch
                    } else {
                        sh 'git checkout target' // Checkout existing branch
                    }
                }
            }
        }

        stage('Commit Changes') {
            steps {
                sh 'git remote set-url origin git@github.com:jaberkh123/test_python.git'
                sh 'git remote -v'
                sh 'ls'
                sh 'touch nething2'
                sh 'echo jaber > nething '
                sh 'git config user.name jaberkh123'
                sh 'git config user.email jaber.khorramshahi@gmail.com'
                sh 'git add .'
                sh 'git commit -m "Copy file from source-branch"'
                sh 'git push origin target' // Push to remote
            }
        }        
    }
}
