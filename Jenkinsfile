
pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // کلون کردن مخزن
                
                git branch: 'main', url: 'https://github.com/jaberkh123/test_python.git'
            }
        }

        stage('Checkout Branch') {
            steps {
                // تغییر به برنچ مورد نظر
                sh 'git checkout main'
                sh 'ls'
            }
        }


        stage('Checkout Target') {
            steps {
                // تغییر به برنچ هدف
                sh 'git checkout target'
            }
        }
        stage('Commit Changes') {
            steps {
                // افزودن تغییرات
                sh 'git config user.name "jaberkh123"'
                sh 'git config user.email "jaber.khorramshahi@gmail.com"'
                sh 'git add .'
                // کامیت کردن تغییرات
                sh 'git commit -m "Copy file from source-branch"'
            }
        }        
}
}
