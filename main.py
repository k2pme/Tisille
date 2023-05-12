from .data.email import send_email
from subprocess import call

call(send_email("subject", "body", "nzadouapp@gmail.com", "cmantsila0@gmail.com", "mlfxcbzjmsliioaj"))