pipeline {
    agent any

    environment {
        GITHUB_REPO = 'https://github.com/jaberkh123/test_python.git' // آدرس مخزن GitHub شما
        BRANCH_NAME = 'new-python-feature' // نام برنچ جدید برای فایل‌های پایتون
    }

    stages {
        stage('Upload Python Files to GitHub') {
            steps {
                script {
                    // مسیر فایل‌های پایتون در سیستم محلی شما
                    dir('C:\\Users\\jaber\\Desktop\\send.py') {
                        sh """
                            git init
                            git remote add origin ${GITHUB_REPO}
                            git checkout -b ${BRANCH_NAME}
                            git add .
                            git commit -m "Uploading Python files from local system"
                            git push origin ${BRANCH_NAME}
                        """
                    }
                }
            }
        }
}
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
