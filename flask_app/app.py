from flask import Flask
from ec2ninja.manager import start_instance, stop_instance, get_instance_info

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the EC2Ninja Flask App!'


@app.route('/start_instance/<instance_id>')
def start_ec2_instance(instance_id):
    status = start_instance(instance_id)
    if status == 'running':
        return f'EC2 instance {instance_id} is already running'
    return f'Starting EC2 instance: {instance_id}'

@app.route('/stop_instance/<instance_id>')
def stop_ec2_instance(instance_id):
    stopped = stop_instance(instance_id)
    if stopped:
        return f'EC2 instance {instance_id} has been stopped'
    return f'EC2 instance {instance_id} is already stopped'

@app.route('/instance_info/<instance_id>')
def get_ec2_instance_info(instance_id):
    instance_info = get_instance_info(instance_id)
    return str(instance_info)

if __name__ == '__main__':
    app.run(debug=True)