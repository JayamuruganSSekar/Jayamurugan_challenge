  node{
   stage('SCM Checkout'){
     git 'https://github.com/JayamuruganSSekar/Jayamurugan_challenge'
   }
   stage('Compile-Package'){  
      def mvn_version = 'M3'
      withEnv( ["PATH+MAVEN=${tool mvn_version}/bin"] ) {
      sh "mvn clean package"
}
   }
   stage('Email Notification'){
      mail bcc: '', body: '''Hi Welcome to jenkins email alerts
      Thanks
      Hari''', cc: '', from: '', replyTo: '', subject: 'Jenkins Job', to: 'hari.kammana@gmail.com'
   }
}


