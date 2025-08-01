pipeline {
    agent any
    parameters {
        string(name: "TICKETS_NOT_ENTERED", defaultValue: "1", description: "Ticket without park admission")
        string(name: "TICKETS_ENTERED", defaultValue: "1", description: "Ticket with park admission")
        string(name: "PASSES_NOT_ENTERED", defaultValue: "1", description: "Pass without park admission")
        string(name: "PASSES_ENTERED", defaultValue: "1", description: "Pass with park admission")
    }
    stages {
        stage ('Setup Python venv') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/ctivate
                pip install -r requirements.txt
                '''
            }
        }

        stage ('Local Try Out Jenkins') {
            steps {
                sh '''
                    source venv/bin/activate
                    behave --no-capture --no-capture-stderr --no-logcapture --show-timings
                '''
            }
        }
    }
}