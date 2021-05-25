import boto3
import pandas as pd
from handlers.S3BucketHelper import S3BucketHelper
from handlers.CamHandler import CamHandler

class ChargebackCredits:
    def __init__(self, month_year, cloud_type, s3_bucket_cb_control, credit_csv_file):
        self.Month_Year = month_year
        self.Cloud_Type = cloud_type
        self.s3helper = S3BucketHelper()
        self.cam = CamHandler()
        self.s3bucket = s3_bucket_cb_control
        self.credit_csv_file = credit_csv_file

    
    def sendAll(self):

        df = self.s3helper.readCsvFile(self.s3bucket, self.credit_csv_file)

        for idx, row in df.iterrows():
            acctnum=row['Account#']
            Gross_Charge = row['Spend']
            Credit_Applied = row['Credit']
            Final_Charge = row['Chargeback']
            Percent_Saved = row['PercentSave']
            account_name = row['Account Name']
            addresses = self.cam.get_contacts_by_account_name(account_name)
            addresses = list(dict.fromkeys(addresses))
            print(f'method=sendAll; Sending with params for {idx}')
            print('method=sendAll; addresses, Cloud_Type, Month_Year, acctnum, Gross_Charge, Credit_Applied,Final_Charge, Percent_Saved')
            print('method=sendAll; value=data; ',addresses, self.Cloud_Type, self.Month_Year, acctnum, Gross_Charge, Credit_Applied,Final_Charge, Percent_Saved)
        
            if addresses:
                self.send(addresses, self.Cloud_Type, self.Month_Year, acctnum, Gross_Charge, Credit_Applied,Final_Charge, Percent_Saved)
                    



    def send(self, addresses, Cloud_Type, Month_Year, Account_Id, Gross_Charge, Credit_Applied,Final_Charge, Percent_Saved):
        try:
            ses_client = boto3.client('ses')
            
            CHARSET = "UTF-8"
          
            HTML_EMAIL_CONTENT_BODY = f"""
                <!doctype html>
                <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

                <head>
                <title>
                </title>
                <!--[if !mso]><!-- -->
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
                <!--[if !mso]><!-->
                <link href="https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700" rel="stylesheet" type="text/css">
                <style type="text/css">
                    @import url(https://fonts.googleapis.com/css?family=Ubuntu:300,400,500,700);
                </style>
                <!--<![endif]-->
                <style type="text/css">
                    @media only screen and (min-width:480px) {{
                    .mj-column-per-95 {{
                        width: 95% !important;
                        max-width: 95%;
                    }}

                    .mj-column-per-100 {{
                        width: 100% !important;
                        max-width: 100%;
                    }}
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

                <body>
                <div style="">
                    <!--[if mso | IE]>
                    <table
                        align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:800px;" width="800"
                    >
                        <tr>
                        <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                    
                        <v:rect  style="width:800px;" xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false">
                        <v:fill  origin="0, -0.5" position="0, -0.5" src="https://cdn.cloud.toyota.com/email_templates/imgs/chofer_bg.png" type="frame" size="1,1" aspect="atleast" />
                        <v:textbox style="mso-fit-shape-to-text:true" inset="0,0,0,0">
                    <![endif]-->
                    <div style="background:url(https://cdn.cloud.toyota.com/email_templates/imgs/chofer_bg.png) center top / cover no-repeat;background-position:center top;background-repeat:no-repeat;background-size:cover;margin:0px auto;max-width:800px;">
                    <div style="line-height:0;font-size:0;">
                        <table align="center" background="https://cdn.cloud.toyota.com/email_templates/imgs/chofer_bg.png" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:url(https://cdn.cloud.toyota.com/email_templates/imgs/chofer_bg.png) center top / cover no-repeat;background-position:center top;background-repeat:no-repeat;background-size:cover;width:100%;">
                        <tbody>
                            <tr>
                            <td style="direction:ltr;font-size:0px;padding:20px 0;padding-bottom:0;text-align:center;">
                                <!--[if mso | IE]>
                                <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                
                        <tr>
                    
                            <td
                            class="" style="vertical-align:top;width:760px;"
                            >
                        <![endif]-->
                                <div class="mj-column-per-95 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                    <tr>
                                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="border-collapse:collapse;border-spacing:0px;">
                                        <tbody>
                                            <tr>
                                            <td style="width:45px;">
                                                <img alt="" height="auto" src="https://cdn.cloud.toyota.com/email_templates/imgs/chofer_logo.svg" style="border:0;display:block;outline:none;text-decoration:none;height:auto;width:100%;font-size:13px;" width="45" />
                                            </td>
                                            </tr>
                                        </tbody>
                                        </table>
                                    </td>
                                    </tr>
                                    <tr>
                                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                        <div style="font-family:helvetica;font-size:20px;line-height:1;text-align:left;color:white;"><span style="font-weight: bold;">Chofer</span> Cloud Portal</div>
                                    </td>
                                    </tr>
                                    <tr>
                                    <td align="left" style="font-size:0px;padding:10px 25px;padding-bottom:40px;word-break:break-word;">
                                        <div style="font-family:helvetica;font-size:28px;line-height:1;text-align:left;color:white;">Cloud Chargeback Credit - {Month_Year}</div>
                                    </td>
                                    </tr>
                                </table>
                                </div>
                                <!--[if mso | IE]>
                            </td>
                        
                            <td
                            class="" style="vertical-align:top;width:760px;"
                            >
                        <![endif]-->
                                <div class="mj-column-per-95 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
                                    <tbody>
                                    <tr>
                                        <td style="background-color:#FFFFFF;vertical-align:top;padding-bottom:0;">
                                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="" width="100%">
                                            <tr>
                                            <td align="left" style="font-size:0px;padding:10px 25px;padding-top:32px;padding-bottom:20px;word-break:break-word;">
                                                <div style="font-family:helvetica;font-size:24px;line-height:1;text-align:left;color:#000000;">Congrats! Your {Cloud_Type} charges have special savings for {Month_Year}</div>
                                            </td>
                                            </tr>
                                        </table>
                                        </td>
                                    </tr>
                                    </tbody>
                                </table>
                                </div>
                                <!--[if mso | IE]>
                            </td>
                        
                        </tr>
                    
                                </table>
                                <![endif]-->
                            </td>
                            </tr>
                        </tbody>
                        </table>
                    </div>
                    </div>
                    <!--[if mso | IE]>
                        </v:textbox>
                    </v:rect>
                    
                        </td>
                        </tr>
                    </table>
                    
                    <table
                        align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:800px;" width="800"
                    >
                        <tr>
                        <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                    <![endif]-->
                    <div style="margin:0px auto;max-width:800px;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                        <tbody>
                        <tr>
                            <td style="direction:ltr;font-size:0px;padding:20px 0;padding-top:0;text-align:center;">
                            <!--[if mso | IE]>
                                <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                
                        <tr>
                    
                            <td
                            class="" style="vertical-align:top;width:760px;"
                            >
                        <![endif]-->
                            <div class="mj-column-per-95 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#FFFFFF;vertical-align:top;" width="100%">
                                <tr>
                                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                    <div style="font-family:helvetica;font-size:14px;line-height:1;text-align:left;color:#000000;">
                                        <p> The Advanced Cloud Engineering (ACE) team is pleased to inform you of a credit you are getting against your {Cloud_Type} cloud spend for {Month_Year}. </p>
                                        <p>Details of your Cloud Account’s April Spend and the Credit you are getting are as follows. </p>
                                    </div>
                                    </td>
                                </tr>
                                </table>
                            </div>
                            <!--[if mso | IE]>
                            </td>
                        
                        </tr>
                    
                                </table>
                                <![endif]-->
                            </td>
                        </tr>
                        </tbody>
                    </table>
                    </div>
                    <!--[if mso | IE]>
                        </td>
                        </tr>
                    </table>
                    
                    <table
                        align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:800px;" width="800"
                    >
                        <tr>
                        <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                    <![endif]-->
                    <div style="margin:0px auto;max-width:800px;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                        <tbody>
                        <tr>
                            <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                            <!--[if mso | IE]>
                                <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                
                        <tr>
                    
                            <td
                            class="" style="vertical-align:top;width:800px;"
                            >
                        <![endif]-->
                            <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                <tr>
                                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                    <table cellpadding="0" cellspacing="0" width="100%" border="0" style="color:#000000;font-family:Ubuntu, Helvetica, Arial, sans-serif;font-size:13px;line-height:22px;table-layout:auto;width:100%;border:none;">
                                        <tr style="border-bottom:1px solid #ecedee;text-align:left;padding:15px 0;">
                                        <th style="padding: 0 15px 0 0;">AccountId</th>
                                        <th style="padding: 0 15px 0 0;"> Gross Charge</th>
                                        <th>Credit Applied</th>
                                        <th>Final Charge</th>
                                        <th>% saved</th>
                                        </tr>
                                        <tr>
                                        <td>{Account_Id}</td>
                                        <td>{Gross_Charge}</td>
                                        <td>{Credit_Applied}</td>
                                        <td>{Final_Charge}</td>
                                        <td>{Percent_Saved}</td>
                                        </tr>
                                    </table>
                                    </td>
                                </tr>
                                </table>
                            </div>
                            <!--[if mso | IE]>
                            </td>
                        
                        </tr>
                    
                                </table>
                                <![endif]-->
                            </td>
                        </tr>
                        </tbody>
                    </table>
                    </div>
                    <!--[if mso | IE]>
                        </td>
                        </tr>
                    </table>
                    
                    <table
                        align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:800px;" width="800"
                    >
                        <tr>
                        <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                    <![endif]-->
                    <div style="margin:0px auto;max-width:800px;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                        <tbody>
                        <tr>
                            <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                            <!--[if mso | IE]>
                                <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                
                        <tr>
                    
                            <td
                            class="" style="vertical-align:top;width:760px;"
                            >
                        <![endif]-->
                            <div class="mj-column-per-95 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="background-color:#FFFFFF;vertical-align:top;" width="100%">
                                <tr>
                                    <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                    <div style="font-family:helvetica;font-size:14px;line-height:1;text-align:left;color:#000000;">
                                        <p> Please be assured that the ACE team is constantly working with our Cloud Service Providers to get the best discounts and credits for all TMNA Cloud Accounts. </p>
                                        <p> For further account level distribution of the chargebacks, please check out the <a href="https://chofer.cloud.toyota.com">Chofer Portal</a>. </p>
                                    </div>
                                    </td>
                                </tr>
                                </table>
                            </div>
                            <!--[if mso | IE]>
                            </td>
                        
                        </tr>
                    
                                </table>
                                <![endif]-->
                            </td>
                        </tr>
                        </tbody>
                    </table>
                    </div>
                    <!--[if mso | IE]>
                        </td>
                        </tr>
                    </table>
                    
                    <table
                        align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:800px;" width="800"
                    >
                        <tr>
                        <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                    <![endif]-->
                    <div style="margin:0px auto;max-width:800px;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                        <tbody>
                        <tr>
                            <td style="direction:ltr;font-size:0px;padding:20px 0;padding-top:0;text-align:center;">
                            <!--[if mso | IE]>
                                <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                
                        <tr>
                    
                            <td
                            class="" style="vertical-align:top;width:760px;"
                            >
                        <![endif]-->
                            <div class="mj-column-per-95 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:top;" width="100%">
                                <tr>
                                    <td align="left" style="font-size:0px;padding:10px 25px;padding-bottom:32px;word-break:break-word;">
                                    <div style="font-family:helvetica;font-size:14px;line-height:1;text-align:left;color:#000000;">Best Regards, <p>the Cloud Engineering Team</p>
                                    </div>
                                    </td>
                                </tr>
                                </table>
                            </div>
                            <!--[if mso | IE]>
                            </td>
                        
                        </tr>
                    
                                </table>
                                <![endif]-->
                            </td>
                        </tr>
                        </tbody>
                    </table>
                    </div>
                    <!--[if mso | IE]>
                        </td>
                        </tr>
                    </table>
                    
                    <table
                        align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:800px;" width="800"
                    >
                        <tr>
                        <td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;">
                    <![endif]-->
                    <div style="background:#f7f7f7;background-color:#f7f7f7;margin:0px auto;max-width:800px;">
                    <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#f7f7f7;background-color:#f7f7f7;width:100%;">
                        <tbody>
                        <tr>
                            <td style="direction:ltr;font-size:0px;padding:20px 0;text-align:center;">
                            <!--[if mso | IE]>
                                <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                
                        <tr>
                    
                            <td
                            class="" style="vertical-align:top;width:800px;"
                            >
                        <![endif]-->
                            <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:top;width:100%;">
                                <table border="0" cellpadding="0" cellspacing="0" role="presentation" width="100%">
                                <tbody>
                                    <tr>
                                    <td style="vertical-align:top;padding-right:0;">
                                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="" width="100%">
                                        <tr>
                                            <td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                            <div style="font-family:helvetica;font-size:14px;line-height:1;text-align:center;color:#9b9c9d;">Visit Chofer Cloud Portal</div>
                                            </td>
                                        </tr>
                                        </table>
                                    </td>
                                    </tr>
                                </tbody>
                                </table>
                            </div>
                            <!--[if mso | IE]>
                            </td>
                        
                        </tr>
                    
                                </table>
                                <![endif]-->
                            </td>
                        </tr>
                        </tbody>
                    </table>
                    </div>
                    <!--[if mso | IE]>
                        </td>
                        </tr>
                    </table>
                    <![endif]-->
                </div>
                </body>

                </html>
            """

            print(f'sending email to {addresses}')

            response = ses_client.send_email(
                Destination={
                    "ToAddresses": addresses,
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
                Source="advanced_cloud_engineering@toyota.com",
            )
    
        except Exception as e:
            print(e)
