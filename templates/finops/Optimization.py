import boto3
from handlers.CamHandler import CamHandler

class Optimization:
    def __init__(self):
        self.messages = []
        self.cam = CamHandler()

    def add(self, message):
      self.messages.append(message)
    
    def consolidation(self):
      
      addresses = []
      
      for msg in self.messages:
        addresses = addresses + self.cam.get_contacts_by_accountid(msg["account_id"])

      addresses = list(dict.fromkeys(addresses))
      
      if addresses:
        self.send(addresses)

    def send(self, addresses):
        try:
            ses_client = boto3.client('ses')
            
            CHARSET = "UTF-8"
          
            HTML_EMAIL_CONTENT_BODY = f"""
                               <!doctype html>
            <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"
            xmlns:o="urn:schemas-microsoft-com:office:office">

            <head>
            <title>
            </title>
            <!--[if !mso]><!-->
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <!--<![endif]-->
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style type="text/css">
                #outlook a {{
                    padding: 0;
                }}

                body {{
                    margin: 0;
                    padding: 0;
                    -webkit-text-size-adjust: 100%;
                    -ms-text-size-adjust: 100%;
                }}

                table,
                td {{
                    border-collapse: collapse;
                    mso-table-lspace: 0pt;
                    mso-table-rspace: 0pt;
                }}

                img {{
                    border: 0;
                    height: auto;
                    line-height: 100%;
                    outline: none;
                    text-decoration: none;
                    -ms-interpolation-mode: bicubic;
                }}

                p {{
                    display: block;
                    margin: 13px 0;
                }}
            </style>
            <!--[if mso]>
                                    <xml>
                                    <o:OfficeDocumentSettings>
                                    <o:AllowPNG/>
                                    <o:PixelsPerInch>96</o:PixelsPerInch>
                                    </o:OfficeDocumentSettings>
                                    </xml>
                                    <![endif]-->
            <!--[if lte mso 11]>
                                    <style type="text/css">
                                    .mj-outlook-group-fix {{ width:100% !important; }}
                                    </style>
                                    <![endif]-->
            <style type="text/css">
                @media only screen and (min-width:480px) {{
                    .mj-column-per-95 {{
                        width: 95% !important;
                        max-width: 95%;
                    }}
                }}
            </style>
            <style media="screen and (min-width:480px)">
                .moz-text-html .mj-column-per-95 {{
                    width: 95% !important;
                    max-width: 95%;
                }}
            </style>
            <style type="text/css">
                @media only screen and (max-width:480px) {{
                    table.mj-full-width-mobile {{
                        width: 100% !important;
                    }}

                    td.mj-full-width-mobile {{
                        width: auto !important;
                    }}
                }}
            </style>
            </head>

            <body style="word-spacing:normal;">
            <div style>
                <!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:800px;" width="800" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><v:rect style="width:800px;" xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false"><v:fill origin="0, -0.5" position="0, -0.5" src="https://cdn.cloud.toyota.com/email_templates/imgs/chofer_bg.png" type="frame" size="1,1" aspect="atleast" /><v:textbox style="mso-fit-shape-to-text:true" inset="0,0,0,0"><![endif]-->
                <div
                style="background:url(https://cdn.cloud.toyota.com/email_templates/imgs/chofer_bg.png) center top / cover no-repeat;background-position:center top;background-repeat:no-repeat;background-size:cover;margin:0px auto;max-width:800px;">
                <div style="line-height:0;font-size:0;">
                    <table align="center" background="https://cdn.cloud.toyota.com/email_templates/imgs/chofer_bg.png" border="0"
                    cellpadding="0" cellspacing="0" role="presentation"
                    style="background:url(https://cdn.cloud.toyota.com/email_templates/imgs/chofer_bg.png) center top / cover no-repeat;background-position:center top;background-repeat:no-repeat;background-size:cover;width:100%;">
                    <tbody>
                        <tr>
                        <td style="direction:ltr;font-size:0px;padding:20px 0;padding-bottom:0;text-align:center;">
                            <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="vertical-align:top;width:760px;" ><![endif]-->
                            <div class="mj-column-per-95 mj-outlook-group-fix"
                            style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;"
                                width="100%">
                                <tbody>
                                <tr>
                                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                    <table border="0" cellpadding="0" cellspacing="0" role="presentation"
                                        style="border-collapse:collapse;border-spacing:0px;">
                                        <tbody>
                                        <tr>
                                            <td style="width:45px;">
                                            <img alt height="auto"
                                                src="https://cdn.cloud.toyota.com/email_templates/imgs/chofer_logo.svg"
                                                style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;"
                                                width="45">
                                            </td>
                                        </tr>
                                        </tbody>
                                    </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                    <div style="font-family:helvetica;font-size:20px;line-height:1;text-align:left;color:white;">
                                        <span style="font-weight: bold;">Chofer</span> Cloud Portal</div>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="left"
                                    style="font-size:0px;padding:10px 25px;padding-bottom:40px;word-break:break-word;">
                                    <div style="font-family:helvetica;font-size:28px;line-height:1;text-align:left;color:white;">
                                        Potential Savings Oppurtunities</div>
                                    </td>
                                </tr>
                                </tbody>
                            </table>
                            </div>
                            <!--[if mso | IE]></td><td class="" style="vertical-align:top;width:760px;" ><![endif]-->
                            <div class="mj-column-per-95 mj-outlook-group-fix"
                            style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                            <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
                                <tbody>
                                <tr>
                                    <td style="background-color:#FFFFFF;vertical-align:top;padding-bottom:0;">
                                    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style width="100%">
                                        <tbody>
                                        <tr>
                                            <td align="left"
                                            style="font-size:0px;padding:10px 25px;padding-top:32px;padding-bottom:20px;word-break:break-word;">
                                            <div
                                                style="font-family:helvetica;font-size:24px;line-height:1;text-align:left;color:#000000;">
                                                Greetings from the Cloud Engineering Team</div>
                                            </td>
                                        </tr>
                                        </tbody>
                                    </table>
                                    </td>
                                </tr>
                                </tbody>
                            </table>
                            </div>
                            <!--[if mso | IE]></td></tr></table><![endif]-->
                        </td>
                        </tr>
                    </tbody>
                    </table>
                </div>
                </div>
                <!--[if mso | IE]></v:textbox></v:rect></td></tr></table><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:800px;" width="800" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
                <div style="margin:0px auto;max-width:800px;">
                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                    <tbody>
                    <tr>
                        <td style="direction:ltr;font-size:0px;padding:20px 0;padding-top:0;text-align:center;">
                        <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="vertical-align:top;width:760px;" ><![endif]-->
                        <div class="mj-column-per-95 mj-outlook-group-fix"
                            style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                            <table border="0" cellpadding="0" cellspacing="0" role="presentation"
                            style="background-color:#FFFFFF;vertical-align:top;" width="100%">
                            <tbody>
                                <tr>
                                <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                    <div style="font-family:helvetica;font-size:14px;line-height:1;text-align:left;color:#000000;">
                                        <p>
                                            We have identified Potential Savings Oppurtunities in your Cloud Accounts. For further information on the Violated resources and Account level distribution, please check out the <a href="https://chofer.cloud.toyota.com">Chofer Portal</a>. 
                                        </p>
                                    </div>
                                </td>
                                </tr>
                            </tbody>
                            </table>
                        </div>
                        <!--[if mso | IE]></td></tr></table><![endif]-->
                        </td>
                    </tr>
                    </tbody>
                </table>
                </div>
                <!--[if mso | IE]></td></tr></table><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:800px;" width="800" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
                <div style="margin:0px auto;max-width:800px;">
                <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                    <tbody>
                    <tr>
                        <td style="direction:ltr;font-size:0px;padding:20px 0;padding-top:0;text-align:center;">
                        <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="vertical-align:top;width:760px;" ><![endif]-->
                        <div class="mj-column-per-95 mj-outlook-group-fix"
                            style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                            <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;"
                            width="100%">
                            <tbody>
                                <tr>
                                <td align="left"
                                    style="font-size:0px;padding:10px 25px;padding-bottom:32px;word-break:break-word;">
                                    <div style="font-family:helvetica;font-size:14px;line-height:1;text-align:left;color:#000000;">
                                    Best Regards, <p>the Cloud Engineering Team</p>
                                    </div>
                                </td>
                                </tr>
                            </tbody>
                            </table>
                        </div>
                        <!--[if mso | IE]></td></tr></table><![endif]-->
                        </td>
                    </tr>
                    </tbody>
                </table>
                </div>
                <!--[if mso | IE]></td></tr></table><![endif]-->
            </div>
            </body>

            </html>
            """

            response = ses_client.send_email(
                Destination={
                    "ToAddresses": [
                        "imre.czegledi@toyota.com",
                    ],
                },
                Message={
                    "Body": {
                        "Html": {
                            "Charset": CHARSET,
                            "Data": HTML_EMAIL_CONTENT_BODY,
                        }
                    },
                    "Subject": {
                        "Charset": CHARSET,
                        "Data": "ACE-Notification",
                    },
                },
                Source="imre.czegledi@toyota.com",
            )
    
        except Exception as e:
            print(e)
