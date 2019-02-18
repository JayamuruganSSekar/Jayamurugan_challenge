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
   stage('Deploy to tomcat using Ansible'){
     sh "cd"
     sh "git clone https://github.com/JayamuruganSSekar/Jayamurugan_challenge"
     sh "cd Jayamurugan_challenge/playbooks"
     sh "ansible-playbook tomcat_deployment.yml"
     
   }
}


