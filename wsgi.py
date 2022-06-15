from main import app

if __name__ == "__main__":
    context = ('/etc/letsencrypt/archive/www.irrigation.cc/fullchain1.pem',
               '/etc/letsencrypt/archive/www.irrigation.cc/privkey1.pem')
    app.run(
            host="0.0.0.0",
            ssl_context = context
            )