import smtplib
import sys
import json

from email.mime.text import MIMEText

config = json.loads(open('mail_config.json').read())

success_msg = MIMEText('New Patch Deployed successfully.')
failure_msg = MIMEText('New Patch failed, so restored previous patch.')
success_msg['Subject'] = "Patch deployment status"
failure_msg['Subject'] = "Patch deployment status"
success_msg['From']    = config["mail_from"]
success_msg['To']      = config["mail_to"]

failure_msg['From']    = config["mail_from"]
failure_msg['To']      = config["mail_to"]


s = smtplib.SMTP(config['smtp_hostname'], 587)

s.login(config['smtp_login'], config['smtp_password'])
if sys.argv[1] == "success":
   s.sendmail(success_msg['From'], success_msg['To'], success_msg.as_string())
elif sys.argv[1] == "fail":
   s.sendmail(failure_msg['From'], failure_msg['To'], failure_msg.as_string())
s.quit()
