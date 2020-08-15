# Services

## SSL Error for MacOS

1. For `urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)>`
   - RUN `_certifi.py` file
   - alertatively RUN `pip install certifi`

## Sendgrid API Key

1. Ask admin for .env file with api key
   - RUN `backend/source .env`

## Sendgrid Email Templates

1. Dashboard > Email API > Dynamic Templates
   - Create email template
   - Make note of Template ID: `d-23de07b37b2c429480a92926287e2055`
   - Use case located in `sendgrid_test.py`
