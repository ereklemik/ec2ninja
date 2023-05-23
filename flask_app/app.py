import boto3
from flask import Flask, render_template
from ec2ninja.manager import start_instance, stop_instance, get_instance_info

app = Flask(__name__)
session = boto3.Session(region_name='eu-central-1')
# ec2_client = session.client('ec2', region_name='eu-central-1')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_instance/<instance_id>')
def start_ec2_instance(instance_id):
    status = start_instance(instance_id)
    if status == 'running':
        return render_template('result.html', message=f'EC2 instance {instance_id} is already running')
    return render_template('result.html', message=f'Starting EC2 instance: {instance_id}')

@app.route('/stop_instance/<instance_id>')
def stop_ec2_instance(instance_id):
    stopped = stop_instance(instance_id)
    if stopped:
        return render_template('result.html', message=f'EC2 instance {instance_id} has been stopped')
    return render_template('result.html', message=f'EC2 instance {instance_id} is already stopped')

@app.route('/instance_info/<instance_id>')
def get_ec2_instance_info(instance_id):
    instance_info = get_instance_info(instance_id)
    return render_template('instance_info.html', instance_info=instance_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)