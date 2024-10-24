
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
                sh 'git checkout source-branch'
                sh 'ls'
            }
        }


}
}
