pipeline {
    agent any // Bisa disesuaikan jika kamu menggunakan node/agent khusus

    stages {
        stage('Checkout Kode') {
            steps {
                // Mengambil kode terbaru dari repository
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                // Membuat virtual environment dan menginstal dependencies
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Jalankan QA Tests') {
            steps {
                // Menjalankan pytest dan menghasilkan laporan XML format JUnit
                sh '''
                    . venv/bin/activate
                    pytest tests/ --junitxml=reports/test-result.xml
                '''
            }
        }
    }

    post {
        always {
            // Membaca laporan tes terlepas dari tes tersebut gagal atau lulus
            junit 'reports/test-result.xml'
        }
        success {
            echo 'Semua tes berhasil dilewati! 🎉'
        }
        failure {
            echo 'Ada tes yang gagal. Segera periksa laporannya! 🚨'
            // Di sini kamu bisa menambahkan notifikasi ke Slack/Email atau Discord
        }
    }
}